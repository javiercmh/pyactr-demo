# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 08:41:31 2021

@author: Michelle
"""

import pyactr as actr

addition = actr.ACTRModel()

actr.chunktype("number", "number, next")
actr.chunktype("add", "arg1, arg2, sum, count")

# Set up declaritive memory
dm = addition.decmem

zero = actr.makechunk(nameofchunk="zero", typename="number", number="zero", next="one")
one = actr.makechunk(nameofchunk="one", typename="number", number="one", next="two")
two = actr.makechunk(nameofchunk="two", typename="number", number="two", next="three")
three = actr.makechunk(nameofchunk="three", typename="number", number="three", next="four")
four = actr.makechunk(nameofchunk="four", typename="number", number="four", next="five")
five = actr.makechunk(nameofchunk="five", typename="number", number="five", next="six")
six = actr.makechunk(nameofchunk="six", typename="number", number="six", next="seven")
seven = actr.makechunk(nameofchunk="seven", typename="number", number="seven", next="eight")
eight = actr.makechunk(nameofchunk="eight", typename="number", number="eight", next="nine")
nine = actr.makechunk(nameofchunk="nine", typename="number", number="nine", next="ten")
ten = actr.makechunk(nameofchunk="ten", typename="number", number="ten")


dm.add(zero)
dm.add(one)
dm.add(two)
dm.add(three)
dm.add(four)
dm.add(five)
dm.add(six)
dm.add(seven)
dm.add(eight)
dm.add(nine)
dm.add(ten)

#Set up goal
goal_chunk = actr.makechunk(nameofchunk="goal", typename="add", arg1="five", arg2="two")
goal = addition.set_goal("goal")
goal.add(goal_chunk)

#print(dm)
#print(goal)

addition.productionstring(name="initialize_addition", string="""
        =goal>
        isa  add
        arg1 =num1
        arg2 =num2
        sum nil
        ==>
        =goal>
        isa add
        sum =num1
        count =zero
        +retrieval>
        isa number
        number =num1""")

addition.productionstring(name="terminate_addition", string="""
        =goal>
        isa  add
        count =num
        arg2 =num
        sum =answer
        =retrieval>
        isa number
        number =answer
        ==>
        =goal>
        isa add
        count nil
        """)
        #!output! =answer - meant to be last line in the string
        

addition.productionstring(name="increment_count", string="""
        =goal>
        isa  add
        sum =sum
        count =count
        =retrieval>
        isa number
        number =count
        next =newcount
        ==>
        =goal>
        isa add
        count =newcount
        +retrieval>
        isa number
        number =sum""")
        
addition.productionstring(name="increment_sum", string="""
        =goal>
        isa  add
        sum =sum
        count =count
        arg2 =count
        =retrieval>
        isa number
        number =sum
        next =newsum
        ==>
        =goal>
        isa add
        sum =newsum
        +retrieval>
        isa number
        number =count""")

simulate = addition.simulation()
simulate.run()
