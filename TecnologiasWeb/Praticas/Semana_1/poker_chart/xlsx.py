import zipfile, re, sys, xml.etree.ElementTree as ET
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def load(path):
  z=zipfile.ZipFile(path)
  ss=[]
  if 'xl/sharedStrings.xml' in z.namelist():
    for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',NS):
      ss.append(''.join(t.text or '' for t in si.iter('{%s}t'%NS['m'])))
  wb=ET.fromstring(z.read('xl/workbook.xml'))
  rels=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
  rmap={r.get('Id'):r.get('Target') for r in rels}
  sheets={}
  for s in wb.find('m:sheets',NS):
    t=rmap[s.get('{%s}id'%NS['r'])]; t=t.lstrip('/'); t=t if t.startswith('xl/') else 'xl/'+t
    rows=[]
    for row in ET.fromstring(z.read(t)).iter('{%s}row'%NS['m']):
      r={}
      for c in row.findall('m:c',NS):
        col=re.match(r'[A-Z]+',c.get('r')).group(); v=c.find('m:v',NS); ty=c.get('t')
        if ty=='inlineStr': val=''.join(x.text or '' for x in c.iter('{%s}t'%NS['m']))
        elif v is None: continue
        elif ty=='s': val=ss[int(v.text)]
        else: val=v.text
        r[col]=val
      rows.append(r)
    sheets[s.get('name')]=rows
  return sheets
