---
title: Simulating the Monty Hall Problem
date: 2017-10-01
tags: [code]
published: true
layout: default
fav: true
---

# Monty Hall Problem simulated in Python

In light of the recent news that [Monty Hall has passed
away](http://www.reuters.com/article/us-people-montyhall/lets-make-a-deal-host-monty-hall-dead-at-96-idUSKCN1C60U0),
I thought I would get around to posting a simulation I had written a while ago.

## The Monty Hall Problem

The [Monty Hall Problem](https://en.wikipedia.org/wiki/Monty_Hall_problem) is a puzzle that seems to contradict common sense. The problem can be stated as such:

*On a game show, there are 3 doors. Behind one door is a car, while the other doors hide goats. The contestant chooses one door, after which, the host opens one door, revealing a goat. The contestant is then offered the choice of either sticking with their current choice, or switching to the other door. What is the best decision?*

It is important to note the following conditions are always met:

* The host knows what is behind each door, and will always reveal a goat.
* The contestant is *always* offered a chance to switch.

### Solution

**Switch!** At first glance, it appears that the contestant's chance of wining has increased from 33% to 50%, so switching or not, shouldn't make any difference. However, it can be shown that switching actually increases the contestant's chances of wining to 66% !


## Python Simulation

I have written the following Python code to simulate the problem, attempting to
generalise the solution for any number of doors, along with the host opening
any number of doors. 

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

### Operation

This simulation will run many rounds of this scenario with random placement of
cars and goats, and count the number of times the contestant randomly chooses
the correct door first (winning if they don't switch), versus having the
contestant switch to a randomly selected unopened door after the host reveals a
goat. 

### Results

The results of this simulation can be found in the file,
[monty_hall_10k.csv](/monty_hall_10k.csv). Each row contains the number of doors
available, the number of doors opened by the host, then the number of times the
contestant wins without switching, and the number of times the contestant wins
with switching. Each scenario (number of doors, and number of doors opened by
the host) is run 10,000 times.

### Observations

Unsurprisingly, there are only a very few cases in this scenario where sticking
is the correct course of action -- switching almost always results in a higher
chance of wining the car. Only when a very small percentage of doors are opened
does this appear, and never consistently.


The game is set to the host's favour until over 95% of the doors are opened.
Only then will the contestant have a greater than 50% chance of wining the car,
and then, only when he switches.

![Wins by the percentage of doors opened](/img/monty_hall_wins_by_percentage_doors_opened.png)

**Sample Splunk Query**
```
source="monty_hall_10k.csv"
| eval perc_doors = round(doors_to_open/doors,2) 
| eval perc_switch = round(switch_wins/10000,2) 
| eval perc_stick = round(stick_wins/10000,2)
| chart avg(perc_switch) as "Switch Wins", avg(perc_stick) as "Stick Win",  over perc_doors
| rename perc_doors as "% Doors opened"
```

If we describe the problem as there being 100 doors, of which the host opens 98
of them, is it more intuitive that the contestant should switch? They have a
99% chance of wining the car if they do so. Yet it still feels as though they
have a 50-50 choice between the door they hold and the remaining door.


## Future ideas

Here are a few ideas for altering the game, which may alter the contestant's best decision.

* What if there are more than one car hidden behind the doors?

* If there are multiple prizes, what if the number of prizes is not specified? What if there is an upper or lower bound is specified, for example, up to 3 cars, or at least 3 cars are behind the doors.

* What happens if the host doesn't know what's behind each door?

* What happens when there are multiple prizes of different degrees (car, holiday, goat)? Should one switch if the host reveals a car? What are the best rules for a host in chosing what to reveal?
