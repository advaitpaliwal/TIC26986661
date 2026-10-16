#!/bin/sh
PY=~/Scratch/planet-hunt/tic240488148-companions/.venv/bin/python
H=~/Scratch/planet-hunt/revision-82149/fpp
for m in masked search; do for k in 0 1 2 3 4 5 6 7 8 9; do echo "$m $k"; done; done | xargs -P 4 -L 1 sh -c 'OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 "$0" -I -u '"$H"'/run_fpp.py "$1" "$2" > '"$H"'/out/run_$1_$2.log 2>&1' "$PY"
