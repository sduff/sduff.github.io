title: Proactive Maintenance Goals
#url:
#template:
tags: ai
#sitemap settings
#sm_f: weekly
#sm_p: 0.5


Starting in 2011, I undertook research into the notion of _Proactive Maintenance Goals_
for _Intelligent Agents_. This page gives a brief summary of what Proactive
maintenance goals are, how they are used and a list of my publications.

## Overview

Many _Intelligent Agents_ are programmed through the notion of _goals_. At
a high level, an agent is most commonly given the task of accomplishing some
task by being given an 'achievement goal'; it is then up to the agent to
determine the best way to accomplish such a goal. For example, an agent may be
given the goal of moving a parcel from one office to another. The agent could
reason to contact a courier to transport it, to circulate an email asking office
staff if they are going to the other office, or if the agent was embodied,
perhaps carrying the parcel itself.

### Achievement Goals
This describes achievement goals, which are goals that have a definite end state
(e.g., the parcel is safely delivered to the other office). In contrast to this,
there also exist _maintenance goals_ (Other goals are also possible, but for
now, I'll just focus on these two). Maintenance goals differ from achievement
goals in that they persist, and describe a state that should or should not
exist, for example, don't run out of fuel.

### Reactive Maintenance Goals
_Reactive Maintenance Goals_ were popular in many agent programming frameworks,
and were structured in a similar was to an achievement goal. If some state
occurred, then an achievement goal of rectifying the state was initiated. If the
fuel tank was less than 10% capacity, go to a fuel station and refuel.

### Proactive Maintenance Goals

The problem with reactive maintenance goals is that an agent can find itself
performing wasteful actions. An agent may almost have accomplished an
achievement goal, only for a reactive maintenance goal to be triggered,
requiring the agent to make effort towards recovery at the expense of the
achievement goals.

My supervisors and myself proposed the notion of _Proactive Maintenance Goals_
to address this issue. Rather than waiting for a trigger, the proactive
maintenance goal would be considered as part of adopting an achievement goal. An
agent would consider the outcome of the achievement goal and if its maintenance
goals would still be satisfied. Delivering the parcel to the other office could
consume 10% of the agent's battery, which would leave it to far from a charger.
Rather than starting the journey to the office, only to have to return and
charge and then restart the journey, proactive maintenance goals would ensure
that the agent recharged prior to the trip to the other office.

## Outcomes

Our initial research into proactive maintenance goals 
integrated the concept of into a basic agent framework and our research was
experimentally validated, showing significant improvements when compared with
reactive maintenance goals. 

We later integrated proactive maintenance goals into a high-level agent language
with formal semantics, to further develop how proactive maintenance goals
influence agent behaviour.

## Applications

There are many applications where proactive maintenance goals are preferred over
reactive ones.

* _Drones_ - maintaining safe distances from people, buildings and other objects
* _Driverless Cars_ - maintaining safe and legal speeds, battery levels
* _Autonomic Computing_ - ensuring sufficient resources are always available,
  even during automated upgrades or administrative tasks

## Publications

My published work on Proactive Maintenance Goals.

* _Simon Duff_, _John Thangarajah_ and _James Harland_,
[Maintenance Goals in Intelligent Agents](http://onlinelibrary.wiley.com/doi/10.1111/coin.12000/full). 
[Computational Intelligence](http://onlinelibrary.wiley.com/journal/10.1111/%28ISSN%291467-8640),
July, 2012.

* _Simon Duff_ and _James Harland_,
[Formalising Proactive Maintenance Goals](http://www.di.unito.it/~baldoni/DALT-2008/papers/paper_21.pdf) , 
[Declarative Agent Languages and Technologies (DALT 2008)](http://www.di.unito.it/~baldoni/DALT-2008/),
Portugal, September, 2008.

* _Simon Duff_, _James Harland_ and _John Thangarajah_, 
[On Proactivity and Maintenance Goals](http://goanna.cs.rmit.edu.au/~johthan/publications/proactivity-duff.pdf),
[Proceedings of the Fifth International Conference on Autonomous Agents and Multi-Agent Systems (AAMAS'06)](http://www.ifaamas.org/AAMAS/aamas06/main.html),
Hakodate, May, 2006. 
