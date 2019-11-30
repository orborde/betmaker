# betmaker
Put bets together with your friends

# Example usage

Alice thinks some proposition is 90% likely. Bob thinks it's only 70% likely. They're each willing to lose a maximum of $100 betting on their disagreement.

```
$ ./betmaker.py 90 70 100
high: 90.0
low:  70.0
bet prob: 80.0
high pmt: 100.0
low pmt:  24.999999999999993
high ev: 12.499999999999995
low ev: 62.5
```

Betmaker suggests a bet as follows:
If the proposition resolves as "No", Alice pays Bob $100.
If "Yes", Bob pays Alice $25.
