# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 08:41:31 2021

@author: Michelle
"""

import pyactr as actr

addition = actr.ACTRModel()

actr.chunktype("number", "number, next")
actr.chunktype("add", "arg1, arg2, sum, count")

# Shortcut to declarative memory
dm = addition.decmem

# add numbers from 0 to 10 to declarative memory
for i in range(11):
    dm.add(actr.makechunk(nameofchunk=str(i), typename="number", number=i, next=i+1))

# Set up goal
goal_chunk = actr.makechunk(nameofchunk="goal", typename="add", arg1=5, arg2=2)
goal = addition.set_goal("goal")
goal.add(goal_chunk)

addition.productionstring(name="initialize_addition", string="""
    =goal>
        isa     add
        arg1    =num1
        arg2    =num2
        sum     None
    ==>
    =goal>
        isa     add
        sum     =num1
        count   0
    +retrieval>
        isa     number
        number  =num1
    """)

addition.productionstring(name="increment_sum", string="""
    =goal>
        isa     add
        sum     =sum
        count   =count
        arg2    ~=count
    =retrieval>
        isa     number
        number  =sum
        next    =newsum
    ==>
    =goal>
        isa add
        sum =newsum
    +retrieval>
        isa number
        number =count
    """)

addition.productionstring(name="increment_count", string="""
    =goal>
        isa     add
        sum     =sum
        count   =count
    =retrieval>
        isa number
        number  =count
        next    =next
    ==>
    =goal>
        isa add
        count =next
    +retrieval>
        isa number
        number =sum
    """)

addition.productionstring(name="terminate_addition", string="""
    =goal>
        isa add
        count =num
        arg2 =num
        sum =answer
    =retrieval>
        isa number
        number =answer
    ==>
    =goal>
        isa add
        count None
    """)
    #!output! =answer - meant to be last line in the string        
    # clean goal buffer?

simulate = addition.simulation()
simulate.run()

print('goal', addition.goals)
print('retrieval', addition.retrieval)