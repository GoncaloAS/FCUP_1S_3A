import datetime as dt, json
from xlsx import load
sh=load('/Users/goncalosousa/Downloads/Polarize Rail (2).xlsx')
M=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
base=dt.date(1899,12,30)
levels=[(base+dt.timedelta(int(r['Q'])),float(r['R']),r['P']) for r in sh['Total'] if r.get('Q','').isdigit() and 'R' in r]
def bb_at(d):
  cur=None
  for s,b,n in levels:
    if d>=s: cur=(b,n)
  return cur
days=[]
for y,suf in ((2025,' 2025'),(2026,'')):
  for i,m in enumerate(M):
    for r in sh[m+suf][1:]:
      if r.get('B') and r.get('D') is not None and r.get('A','').isdigit():
        d=dt.date(y,i+1,int(r['A'])); b=bb_at(d)
        days.append((d,int(float(r['B'])),float(r['D']),b))
days.sort()
nobb=[x for x in days if x[3] is None]
print('days',len(days),'first',days[0][0],'last',days[-1][0],'no level:',len(nobb), nobb[:3])
days=[x for x in days if x[3]]
H=sum(x[1] for x in days); BB=sum(x[2]/x[3][0] for x in days)
print('hands',H,'bb',round(BB),'bb/100',round(BB/H*100,2))
by={}
for d,h,g,(b,n) in days: by.setdefault(n,[0,0]); by[n][0]+=h; by[n][1]+=g/b
for n,(h,bb) in by.items(): print(n,h,round(bb),round(bb/h*100,2))
# monthly hands
mon={}
for d,h,g,_ in days: mon.setdefault(d.strftime('%Y-%m'),0); mon[d.strftime('%Y-%m')]+=h
print(mon)
acc=0;hh=0;pts=[(0,0)]
for d,h,g,(b,n) in days: hh+=h; acc+=g/b; pts.append((hh,round(acc,1)))
json.dump({'pts':pts,'first':str(days[0][0]),'last':str(days[-1][0]),'hands':H,'bb':BB},open('poker.json','w'))
