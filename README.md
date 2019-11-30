# betmaker
Put bets together with your friends

# Example usage

Alice thinks some proposition is 90% likely. Bob thinks it's only 70% likely. They're each willing to lose a maximum of $100 betting on their disagreement.

```
$ ./betmaker.py 90 70 100
Inputs:
  high player: 90%
  low  player: 70%

Proposed bet:
  NO:  high pays low  $100.00
  YES: low  pays high $25.00

  Implied probability: 80%

Expected values:
  high player expects: $12.50
  low  player expects: $62.50
```
