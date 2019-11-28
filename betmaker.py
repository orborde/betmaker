#! /usr/bin/env python3

import sys

_, A, B, pmt = sys.argv

def pct(x):
    x = float(x)
    assert x > 0
    assert x < 100
    return x

A=pct(A)
B=pct(B)
pmt = float(pmt)

high = max(A,B)
low  = min(A,B)

print('high:', high)
print('low: ', low)

bet = (high+low)/2
print('bet prob:', bet)

ph = high/100
pl = low/100
pb = bet/100

highmax_high, highmax_low = (
    pmt,
    (1 - pb)/pb * pmt,
)

lowmax_high, lowmax_low = (
    pb/(1-pb) * pmt,
    pmt,
)

if highmax_low > pmt:
    pmt_high, pmt_low = lowmax_high, lowmax_low
else:
    pmt_high, pmt_low = highmax_high, highmax_low

print('high pmt:', pmt_high)
print('low pmt: ', pmt_low)

ev_high = ph * pmt_low  - (1-ph)*pmt_high
ev_low  = pl * pmt_high - (1-pl)*pmt_low

assert ev_high > 0
assert ev_low > 0

print('high ev:', ev_high)
print('low ev:', ev_low)
