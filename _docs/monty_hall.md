---
title: Monty Hall Problem simulated in Python
date: 2017-10-01
tags: [python, probability]
published: false
---

# Monty Hall Problem siulated in Python

In light of the recent news that [Monty Hall has passed
away](http://www.reuters.com/article/us-people-montyhall/lets-make-a-deal-host-monty-hall-dead-at-96-idUSKCN1C60U0),
I thought I would get around to posting some simulations I had written a while
ago.

## The Monty Hall Problem

The [Monty Hall Problem](https://en.wikipedia.org/wiki/Monty_Hall_problem) is a
puzzle that challenges what appears to be a 

###

## Python Simulation

```python
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

### Chart

## References
