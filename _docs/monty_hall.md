layout: default
---

# Monty Hall

Monty Hall is a long standing

## Simulation Code

```
#!/usr/bin/env python

import random

def monty(rounds=1000, doors=3, doors_to_open=1):
    assert (doors_to_open + 2 <= doors)

    initial_wins = 0
    switch_wins = 0

    for r in xrange(1,rounds+1):
        d = ["car"] + ["goat"] * (doors-1)
        random.shuffle(d)

        # player's choice
        c = random.randrange(doors)

        if d[c] == "car":
            initial_wins += 1

        # host will open some number of doors
        opened = 0
        while opened < doors_to_open:
            o = random.randrange(doors)
            if o == c or d[o] == "car" or d[o] == "open":
                continue
            else:
                d[o] = "open"
                opened += 1

        # look for a new door that is closed, and isn't player's current pick
        while True:
            new_door = random.randrange(doors)
            if (new_door != c and d[new_door] != "open"):
                c = new_door
                break
        
        if d[c] == "car":
            switch_wins += 1
    return initial_wins, switch_wins

print("doors,doors_to_open,stick_wins,switch_wins")
for d in range(3,101):
    for dto in range(1,d-1):
        stick, switch = monty(rounds=10000, doors=d, doors_to_open=dto)
        print("%s,%s,%s,%s"%(d,dto,stick,switch))

```

## Results
 % |
 w |
 i | ------ switch
 n | 
 s | ------ initial
   +-----------------
      % doors open  
     

## Conclusions

## Links

* Monty Hall wiki
* Other simulations
