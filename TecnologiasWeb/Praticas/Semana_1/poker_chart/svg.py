import json
d=json.load(open('poker.json')); p=d['pts']
W,H=480,210; L,R,T,B=44,8,10,26
xmax=600000; ymin,ymax=-2000,26000
X=lambda x: L+(W-L-R)*x/xmax
Y=lambda y: T+(H-T-B)*(ymax-y)/(ymax-ymin)
f=lambda v: ('%.1f'%v).rstrip('0').rstrip('.')
path='M'+' '.join(f'{f(X(x))} {f(Y(y))}' for x,y in p)
o=[]
o.append(f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" aria-labelledby="chart-title">')
o.append('  <title id="chart-title">Cumulative result in big blinds over about 568,000 hands, rising from 0 to about 24,000.</title>')
for v in (0,10000,20000):
  o.append(f'  <line class="{"zero" if v==0 else "grid"}" x1="{L}" x2="{W-R}" y1="{f(Y(v))}" y2="{f(Y(v))}"/>')
  o.append(f'  <text x="{L-6}" y="{f(Y(v)+4)}" text-anchor="end">{v//1000 if v else 0}{"k" if v else ""}</text>')
for v in range(0,600001,100000):
  o.append(f'  <text x="{f(X(v))}" y="{H-8}" text-anchor="middle">{v//1000 if v else 0}{"k" if v else ""}</text>')
o.append(f'  <path class="line" d="{path}"/>')
o.append('</svg>')
open('chart.svg.html','w').write('\n'.join(o))
print(len(path))
