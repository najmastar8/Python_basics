#Generators are used to create iterators, but with a different approach.
# Generators are simple functions which return an iterable set of items, one at a time, in a special way.
#When an iteration over a set of item starts using the for statement,the generator is run.
# Once the generator's function code reaches a "yield" statement,
# the generator yields its execution back to the for loop,
# returning a new value from the set. The generator function can generate as many values (possibly infinite) as it wants,
# yielding each one in its turn.
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))


def gen1246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
g=gen1246()
next (g)
next (g)


#Output
#And the next number is... 33!
#And the next number is... 16!
#And the next number is... 32!
#And the next number is... 39!
#And the next number is... 15!
#And the next number is... 31!
#And the next number is... 13!
#About to yield 2
#About to yield 4

########################################################################################################
########################################################################################################
#Generators resume execution
#Can maintain state in local variables
#Complex control flow
#LAzy evaluation
def take (count,iterable):
    counter=0
    for item in iterable:
        if counter==count:
            return
        counter +=1
        yield item

def run_take():
    items =[2,4,6,8,10]
    for item in take(3,items):

        print (item)

#if __name__=='__main__':
run_take()

