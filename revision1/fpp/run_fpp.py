# Rerun of hunt7/fpp/26986661/run_fpp.py with frozen settings (same target pickle, MOLUSC file, N=1e6, filt TESS,
# exptime 30 min, nsamples 20, seeds 1000-1009, 10-min bins over +-0.25 d, dur 0.0492779 d, no neighbours removed).
# Changes: tdepth = fitted depth 3971.43 ppm (deep/26986661/fit/all6/result.json); ephemeris = fitted;
# MODE 'masked': light curve = masked wotan detrend, six sectors (lc_masked_6s.npz); MODE 'search': original search LC.
# usage: run_fpp.py MODE RUN_INDEX
import sys, json, pickle, os, time, numpy as np, warnings; warnings.filterwarnings('ignore')
H='~/Scratch/planet-hunt'; HERE=H+'/revision-82149/fpp'; os.chdir(HERE)
sys.path.insert(0,H+'/hunt5b/trc'); sys.path.insert(0,H+'/hunt5b/trc/vendor')
import gaia_patch
import triceratops.triceratops as tr
import triceratops.marginal_likelihoods as ml, types
class _F:
    def __init__(s,d): s.d=d
    def __getitem__(s,k):
        if isinstance(k,str): return types.SimpleNamespace(values=s.d[k].to_numpy(copy=True))
        return _F(s.d[np.asarray(k)])
_rc=ml.read_csv
ml.read_csv=lambda f,*a,**kw: _F(_rc(f,*a,**kw)) if 'molusc' in str(f) else _rc(f,*a,**kw)
mode,k=sys.argv[1],int(sys.argv[2]); tic=26986661
R=json.load(open(H+'/deep/26986661/fit/all6/result.json'))
P=R['P_d'][0]; T0=R['T0_BJD_TDB'][0]-2457000; tdepth=R['depth_ppm'][0]*1e-6
z=np.load(HERE+'/lc_masked_6s.npz' if mode=='masked' else H+'/hunt7/lc/26986661.npz'); t,f=z['t'],z['f']
tg=pickle.load(open(H+'/hunt7/fpp/26986661/out/target_26986661.pkl','rb'))
n_stars=len(tg.stars)
assert tg.trilegal_fname=='26986661_gaia_background.csv'; tg.trilegal_fname=H+'/hunt7/fpp/26986661/26986661_gaia_background.csv'
ph=t-T0-np.round((t-T0)/P)*P; w=np.abs(ph)<0.25
edges=np.arange(-0.25,0.25+1e-9,10/1440); idx=np.digitize(ph[w],edges)
tb=np.array([ph[w][idx==i].mean() for i in np.unique(idx)]); fb=np.array([f[w][idx==i].mean() for i in np.unique(idx)])
dur=0.049277859571508216; oot=np.abs(tb)>dur; err=float(np.std(fb[oot]))
box=float(np.median(fb[oot])-fb[np.abs(tb)<dur/2*0.8].mean())
tg.calc_depths(tdepth=tdepth, all_ap_pixels=tg._aps)
np.random.seed(1000+k); t0=time.time()
tg.calc_probs(time=tb, flux_0=fb, flux_err_0=err, P_orb=P, contrast_curve_file=None, filt='TESS',
              N=1000000, parallel=True, exptime=30/1440, nsamples=20, verbose=0, molusc_file=H+'/hunt7/fpp/26986661/molusc_out/molusc_for_trc.csv')
tag=f'{mode}_{k}'
tg.probs.to_csv(f'out/probs_{tag}.csv', index=False)
json.dump(dict(mode=mode,run=k,seed=1000+k,P=P,T0=T0,tdepth_ppm=tdepth*1e6,box_depth_ppm=box*1e6,err_ppm=err*1e6,nbins=len(tb),n_stars=n_stars,removed=[],
               FPP=float(tg.FPP),NFPP=float(tg.NFPP),sec=time.time()-t0),open(f'out/res_{tag}.json','w'))
print(tag,tg.FPP,tg.NFPP,round(time.time()-t0),flush=True)
