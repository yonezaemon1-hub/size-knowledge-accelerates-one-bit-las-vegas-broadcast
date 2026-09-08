#!/usr/bin/env python3
import csv
from fractions import Fraction
from pathlib import Path
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'; FIG=ROOT/'figures'; FIG.mkdir(exist_ok=True)

def read_rows(path):
    with path.open(encoding='utf-8') as f:
        return list(csv.DictReader(f))

rows=read_rows(DATA/'bias_comparison_n2_n20.csv')
n=[int(r['n']) for r in rows]
fair=[float(r['log2E_fair']) for r in rows]
dy=[float(r['log2E_dyadic']) for r in rows]
cert=[float(r['log2E_certificate']) for r in rows]
num=[float(r['log2E_numeric_opt']) for r in rows]

plt.figure(figsize=(7.2,4.6))
plt.plot(n,fair,marker='o',label='fair p=1/2')
plt.plot(n,dy,marker='s',label='dyadic size-aware')
plt.plot(n,cert,marker='^',label='certificate-optimal p*')
plt.plot(n,num,marker='x',label='numerically located minimum')
plt.xlabel('network size n'); plt.ylabel(r'$\log_2 W_n(p)$'); plt.legend(); plt.tight_layout()
plt.savefig(FIG/'runtime_comparison.pdf'); plt.savefig(FIG/'runtime_comparison.png',dpi=220); plt.close()

land=read_rows(DATA/'bias_landscape_n10.csv')
px=[float(r['p']) for r in land]; ly=[float(r['log2E']) for r in land]
r10=next(r for r in rows if int(r['n'])==10)
pdy=float(Fraction(r10['p_dyadic_exact'])); pc=float(Fraction(r10['p_certificate_exact'])); po=float(r10['p_numeric_opt'])
plt.figure(figsize=(7.2,4.6))
plt.plot(px,ly,label='Bellman value, n=10')
plt.scatter([po],[float(r10['log2E_numeric_opt'])],label='numerically located minimum')
plt.scatter([pc],[float(r10['log2E_certificate'])],label='certificate optimum')
plt.scatter([pdy],[float(r10['log2E_dyadic'])],label='dyadic')
plt.xlabel('survival probability p'); plt.ylabel(r'$\log_2 W_{10}(p)$'); plt.legend(); plt.tight_layout()
plt.savefig(FIG/'bias_landscape_n10.pdf'); plt.savefig(FIG/'bias_landscape_n10.png',dpi=220); plt.close()
print('PASS_FIGURE_EXPORT')
