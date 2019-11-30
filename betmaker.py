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

print('Inputs:')
print('  high player: %.0f%%' % high)
print('  low  player: %.0f%%' % low)
print()

bet = (high+low)/2

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

print('Proposed bet:')
print('  NO:  high pays low  $%.2f' % pmt_high)
print('  YES: low  pays high $%.2f' % pmt_low)
print()
print('  Implied probability: %.0f%%' % bet)
print()

ev_high = ph * pmt_low  - (1-ph)*pmt_high
ev_low  = pl * pmt_high - (1-pl)*pmt_low

assert ev_high > 0
assert ev_low > 0

print('Expected values:')
print("  high player expects: $%.2f" % ev_high)
print('  low  player expects: $%.2f' % ev_low)
