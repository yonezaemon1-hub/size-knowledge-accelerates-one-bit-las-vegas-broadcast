#!/usr/bin/env python3
from __future__ import annotations

import csv
import math
from fractions import Fraction
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
DATA.mkdir(exist_ok=True)
mp.mp.dps = 90

FAIR_REFERENCE = {
    2: 10, 3: 58, 4: 602, 5: 14106,
    6: 755610, 7: 87665306, 8: 21246839962,
}


def solve_fraction(A, b):
    n = len(b)
    M = [list(A[i]) + [b[i]] for i in range(n)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if M[r][col] != 0)
        if pivot != col:
            M[col], M[pivot] = M[pivot], M[col]
        piv = M[col][col]
        for j in range(col, n + 1):
            M[col][j] /= piv
        for r in range(n):
            if r == col:
                continue
            fac = M[r][col]
            if fac:
                for j in range(col, n + 1):
                    M[r][j] -= fac * M[col][j]
    return [M[i][-1] for i in range(n)]


def bellman_fraction(n: int, p: Fraction):
    p = Fraction(p); d = 1 - p
    A = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    b = [Fraction(1) for _ in range(n)]
    for k in range(1, n):
        for j in range(k + 1):
            prob = Fraction(math.comb(k, j)) * p**j * d**(k-j)
            A[k-1][j] -= prob  # next state = 1+j -> zero-based index j
    for j in range(1, n + 1):
        prob = Fraction(math.comb(n, j)) * p**j * d**(n-j)
        A[n-1][j-1] -= prob
    return solve_fraction(A, b)


def frac_to_mp(x: Fraction):
    return mp.mpf(x.numerator) / x.denominator


def bellman_values_mp(n: int, p):
    p = mp.mpf(p); d = 1 - p
    A = mp.matrix(n); b = mp.matrix(n, 1)
    for i in range(n):
        for j in range(n): A[i, j] = 0
        A[i, i] = 1; b[i] = 1
    for k in range(1, n):
        for j in range(k + 1):
            prob = mp.mpf(math.comb(k, j)) * p**j * d**(k-j)
            A[k-1, j] -= prob
    for j in range(1, n + 1):
        prob = mp.mpf(math.comb(n, j)) * p**j * d**(n-j)
        A[n-1, j-1] -= prob
    x = mp.lu_solve(A, b)
    return [x[i] for i in range(n)]


def log2e_mp(n: int, p):
    return mp.log(bellman_values_mp(n, p)[0], 2)


def golden_min(n: int, a='0.05', b='0.9999', iterations=70):
    a = mp.mpf(a); b = mp.mpf(b)
    gr = (mp.sqrt(5) - 1) / 2
    c = b - gr * (b-a); d = a + gr * (b-a)
    fc = log2e_mp(n, c); fd = log2e_mp(n, d)
    for _ in range(iterations):
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - gr * (b-a); fc = log2e_mp(n, c)
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b-a); fd = log2e_mp(n, d)
    x = (a+b)/2
    return x, log2e_mp(n, x)


def log2_fraction(x: Fraction):
    return mp.log(frac_to_mp(x), 2)


def main():
    fair_rows = []
    for n in range(2, 13):
        val = bellman_fraction(n, Fraction(1, 2))[0]
        assert val.denominator == 1
        if n in FAIR_REFERENCE:
            assert val.numerator == FAIR_REFERENCE[n]
        exponent = Fraction(n * (n + 1), 2)
        ratio = frac_to_mp(val) / mp.power(2, frac_to_mp(exponent))
        fair_rows.append((n, str(val.numerator), mp.nstr(log2_fraction(val), 18), mp.nstr(ratio, 18)))
    with (DATA / 'fair_exact_regression.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(['n','exact_E_T','log2_E_T','normalized_by_2_n_nplus1_over2']); w.writerows(fair_rows)

    comp_rows = []
    for n in range(2, 21):
        k = math.ceil(math.log2((n + 1) / 2))
        p_dy_f = Fraction(2**k - 1, 2**k)
        p_cert_f = Fraction(n - 1, n + 1)
        fair_f = bellman_fraction(n, Fraction(1, 2))[0]
        dy_f = bellman_fraction(n, p_dy_f)[0]
        cert_f = bellman_fraction(n, p_cert_f)[0]
        p_opt, l_opt = golden_min(n)
        l_fair = log2_fraction(fair_f)
        l_dy = log2_fraction(dy_f)
        l_cert = log2_fraction(cert_f)
        comp_rows.append((n, k,
            str(p_dy_f), str(p_cert_f), mp.nstr(p_opt,16), mp.nstr(1-p_opt,16),
            mp.nstr(l_fair,16), mp.nstr(l_dy,16), mp.nstr(l_cert,16), mp.nstr(l_opt,16),
            mp.nstr(l_cert-l_opt,12), mp.nstr(l_dy-l_opt,12),
            str(dy_f.numerator), str(dy_f.denominator), str(cert_f.numerator), str(cert_f.denominator)))
    with (DATA / 'bias_comparison_n2_n20.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['n','k_n','p_dyadic_exact','p_certificate_exact','p_numeric_opt','delta_numeric_opt',
                    'log2E_fair','log2E_dyadic','log2E_certificate','log2E_numeric_opt',
                    'cert_minus_opt_bits','dyadic_minus_opt_bits',
                    'dyadic_E_numerator','dyadic_E_denominator','certificate_E_numerator','certificate_E_denominator'])
        w.writerows(comp_rows)

    n = 10
    landscape=[]
    for i in range(100, 951, 5):
        p = mp.mpf(i)/1000
        landscape.append((mp.nstr(p,8), mp.nstr(log2e_mp(n,p),18)))
    with (DATA / 'bias_landscape_n10.csv').open('w', newline='', encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['p','log2E']); w.writerows(landscape)

    print('PASS_BELLMAN_EXPERIMENTS')
    print('EXACT_RATIONAL_BELLMAN: fair/dyadic/certificate, n=2..20')
    print('FAIR_REFERENCE_MATCH: n=2..8 exact integers')
    print('NUMERIC_BIAS_OPTIMIZATION: 90-digit Bellman solve + golden search, n=2..20')

if __name__ == '__main__': main()
