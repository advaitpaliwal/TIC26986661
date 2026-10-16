import json, glob, csv, collections, statistics as st
R=[json.load(open(f)) for f in sorted(glob.glob('out/res_masked_*.json'))]
F=[r['FPP'] for r in R]; N=[r['NFPP'] for r in R]
sc=collections.defaultdict(list)
for r in R:
    d=collections.defaultdict(float)
    for row in csv.DictReader(open(f"out/probs_masked_{r['run']}.csv")): d[row['scenario']]+=float(row['prob'])
    for k,v in d.items(): sc[k].append(v)
ids=set()
for r in R:
    for row in csv.DictReader(open(f"out/probs_masked_{r['run']}.csv")): ids.add(row['ID'])
out=dict(n_runs=len(R),FPP_mean=st.mean(F),FPP_std=st.stdev(F),FPP_min=min(F),FPP_max=max(F),runs_le_0035=sum(f<=0.035 for f in F),runs_le_0015=sum(f<=0.015 for f in F),
 NFPP_max=max(N),tdepth_ppm=R[0]['tdepth_ppm'],box_depth_ppm=R[0]['box_depth_ppm'],err_ppm=R[0]['err_ppm'],n_stars=R[0]['n_stars'],removed=R[0]['removed'],ids_in_probs=sorted(ids),
 scenario_mean={k:st.mean(v) for k,v in sc.items()}, per_run_FPP=F)
json.dump(out,open('summary.json','w'),indent=1); print(json.dumps(out,indent=1))
