# Masked-detrend light curve for the TRICERATOPS rerun at the fitted depth.
# Same detrending as deep/26986661/fit/all6/prep.py (wotan biweight 0.5 d, transit mask 3*D0 on search ephemeris,
# quality==0, one pipeline per sector incl. S1751), but keeps |phase|<0.25 d so the frozen TRICERATOPS binning
# (10-min bins over +-0.25 d) is unchanged.
import numpy as np, json
from astropy.io import fits
from wotan import flatten, transit_mask
PH='~/Scratch/planet-hunt'; LC=PH+'/hunt7/lc/26986661'
R=json.load(open(PH+'/hunt7/res/26986661.json')); P0,T00=R['P'],R['T0']
D0=json.load(open(PH+'/hunt7/raw_gate_26986661.json'))['duration_days']
S1751=PH+'/deep/26986661/sectors/data1751/mastDownload/HLSP/hlsp_tess-spoc_tess_phot_0000000026986661-s1751_tess_v1_lc/hlsp_tess-spoc_tess_phot_0000000026986661-s1751_tess_v1_lc.fits'
FILES=[('spoc_s21','PDCSAP_FLUX'),('qlp_s45','KSPSAP_FLUX'),('spoc_s46','PDCSAP_FLUX'),('spoc_s48','PDCSAP_FLUX'),('spoc_s72','PDCSAP_FLUX'),('spoc_s1751','PDCSAP_FLUX')]
T,F,S=[],[],[]
for nm,fc in FILES:
    h=fits.open(S1751 if nm=='spoc_s1751' else f'{LC}/{nm}.fits'); d=h[1].data; s=h[0].header['SECTOR']
    m=(d['QUALITY']==0)&np.isfinite(d[fc])&np.isfinite(d['TIME'])
    t,f=d['TIME'][m].astype(float),d[fc][m].astype(float); f=f/np.nanmedian(f)
    msk=transit_mask(time=t,period=P0,duration=3*D0,T0=T00)
    tr=flatten(t[~msk],f[~msk],method='biweight',window_length=0.5,return_trend=True)[1]
    g=np.isfinite(tr); f=f/np.interp(t,t[~msk][g],tr[g])
    r=f-1; sig=1.4826*np.median(np.abs(r[~msk]-np.median(r[~msk])))
    w=(r<5*sig)&(r>-10*sig)
    T+=[t[w]];F+=[f[w]];S+=[np.full(w.sum(),s)]
    print(nm,s,int(w.sum()),round(sig*1e6))
np.savez('lc_masked_6s.npz',t=np.concatenate(T),f=np.concatenate(F),s=np.concatenate(S))
