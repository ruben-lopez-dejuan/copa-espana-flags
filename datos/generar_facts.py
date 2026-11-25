import json,glob,os,sys,textwrap
from collections import defaultdict,Counter
base=sys.argv[1]; out=sys.argv[2]
EV={'333':'3x3x3','222':'2x2x2','444':'4x4x4','555':'5x5x5','666':'6x6x6','777':'7x7x7','333bf':'3x3x3 a ciegas','333fm':'FMC','333oh':'3x3x3 a una mano','clock':'Clock','minx':'Megaminx','pyram':'Pyraminx','skewb':'Skewb','sq1':'Square-1','444bf':'4x4x4 a ciegas','555bf':'5x5x5 a ciegas','333mbf':'Multi-Blind'}
w=json.load(open(base+'/wcif.json',encoding='utf8'))
P=[p for p in w['persons'] if (p.get('registration') or {}).get('status')=='accepted' and p['wcaId']]
titles=defaultdict(lambda:defaultdict(list)); pod=Counter(); attended=defaultdict(set); chk=[]
for f in sorted(glob.glob(base+'/champs/*.json')):
    rs=json.load(open(f,encoding='utf8')); cid=os.path.basename(f)[:-5]; year=int(cid[-4:]); fmc=cid.startswith('FMC')
    byev=defaultdict(list)
    for r in rs:
        if not fmc: attended[r['wca_id']].add(year)
        if r['round_type_id'] in('f','c') and r['country_iso2']=='ES' and r['best']>0: byev[r['event_id']].append(r)
    for ev,l in byev.items():
        if ev not in EV: continue
        ps=[r['pos'] for r in l]
        for r in l:
            rk=1+sum(q<r['pos'] for q in ps)
            if rk<=3: pod[r['wca_id']]+=1
            if rk==1: titles[r['wca_id']][ev].append(year)
def join(l): return l[0] if len(l)==1 else ', '.join(l[:-1])+' y '+l[-1]
facts={}; nr=[]
for p in P:
    es=p['countryIso2']=='ES'; F=[]; i=p['wcaId']
    pb={(b['eventId'],b['type']):b for b in p['personalBests'] if b['eventId'] in EV}
    if es:
        rec=defaultdict(list)
        for (e,t),b in pb.items():
            if b['nationalRanking']==1: rec[e].append(t)
        for e in EV:
            if e in rec:
                ts=sorted(rec[e],reverse=True); s=' y '.join('single' if t=='single' else 'media' for t in ts)
                F.append(f'Récord de España de {EV[e]} ({s})'); nr.append((p['name'],e,[(t,pb[(e,t)]['best']) for t in ts]))
    T=titles.get(i,{})
    tl=sorted(T.items(),key=lambda x:(-len(x[1]),-max(x[1])))
    for e,ys in tl[:2]: F.append(f'Título de España de {EV[e]}: {join([str(y) for y in sorted(ys)])}')
    nt=sum(map(len,T.values()))
    if nt>2 and len(tl)>1: F.append(f'{nt} títulos nacionales en total')
    if pod[i]>=3: F.append(f'{pod[i]} podios nacionales en Campeonatos de España')
    ra=[]
    for (e,t),b in pb.items():
        pref='single' if e in('333bf','444bf','555bf','333mbf') else 'average'
        if t==pref: ra.append((e,b,'' if e=='333mbf' else (' (single)' if t=='single' else ' (media)')))
    wr=sorted([x for x in ra if x[1]['worldRanking'] and x[1]['worldRanking']<=100],key=lambda x:x[1]['worldRanking'])
    for e,b,s in wr[:1]: F.append(f"N.º {b['worldRanking']} del mundo en {EV[e]}{s}")
    if es:
        for e,b,s in sorted([x for x in ra if 2<=x[1]['nationalRanking']<=25],key=lambda x:x[1]['nationalRanking'])[:2]: F.append(f"N.º {b['nationalRanking']} de España en {EV[e]}{s}")
    prev=len(attended.get(i,()))
    if prev: F.append(f'{prev+1}.ª participación en el Campeonato de España')
    if F: facts[i]=['\n'.join(textwrap.wrap(x,38)) for x in F[:4]]
json.dump(facts,open(out,'w',encoding='utf8',newline='\n'),ensure_ascii=False,indent=2)
print('people',len(P),'with facts',len(facts),'facts',sum(map(len,facts.values())),'titles holders',sum(1 for p in P if titles.get(p['wcaId'])))
for x in nr: print(x)
for i in list(facts)[:400]:
    if len(facts[i])==4 and i in titles: print(i,facts[i])
