"""
An example of a model using retrieval and goal buffers. It corresponds to
the simplest model in ACT-R tutorials, Unit 1, 'count'.
"""

import pyactr as actr

counting = actr.ACTRModel()

actr.chunktype("countOrder", "first, second")
actr.chunktype("countFrom", "start, end, count")

# creates variable for declarative memory (easier to access)
dm = counting.decmem 

dm.add(actr.chunkstring(string="""
    isa     countOrder
    first   1
    second  2
"""))
dm.add(actr.chunkstring(string="""
    isa     countOrder
    first   2
    second  3
"""))
dm.add(actr.chunkstring(string="""
    isa     countOrder
    first   3
    second  4
"""))
dm.add(actr.chunkstring(string="""
    isa     countOrder
    first   4
    second  5
"""))

#creating goal buffer
counting.goal.add(actr.chunkstring(string="""
    isa     countFrom
    start   2
    end     4
"""))

#production rules follow; using productionstring, they are similar to Lisp ACT-R

counting.productionstring(name="start", string="""
    =g>
    isa     countFrom
    start   =x
    count   None
    ==>
    =g>
    isa     countFrom
    count   =x
    +retrieval>
    isa countOrder
    first   =x
""")

counting.productionstring(name="increment", string="""
    =g>
    isa     countFrom
    count   =x
    end     ~=x
    =retrieval>
    isa     countOrder
    first   =x
    second  =y
    ==>
    =g>
    isa     countFrom
    count   =y
    +retrieval>
    isa     countOrder
    first   =y
""")

counting.productionstring(name="stop", string="""
    =g>
    isa     countFrom
    count   =x
    end     =x
    ==>
    ~g>
""")

if __name__ == "__main__":
    counting_sim = counting.simulation()
    counting_sim.run()