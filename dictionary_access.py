"""
Compares performance of dictionary access: Direct ([]) and Get (.get)

Test in Python 3.6.1

Benjamin Martin
12/04/2017 
"""

import random
import dis
import timeit

MIN_RANGE = 1
MAX_RANGE = 100000
SIZE = 1000
SELECTION_SIZE = 100
SELECTION_TESTS = 100

def dict1(data, key):
    return data[key]

def dict2(data, key):
    return data.get(key)

data = {}

keys = list(random.sample(range(MIN_RANGE, MAX_RANGE), SIZE))

for key in keys:
    data[key] = random.random()

print("Bytecode Analysis")
print("Direct")
dis.dis(dict1)
print("Get")
dis.dis(dict2)

###

def dict1_selection(data, keys):
    for key in keys:
        data[key]

def dict2_selection(data, keys):
    for key in keys:
        data.get(key)

print()
print("Execution Tests {} random keys (of {})".format(SELECTION_SIZE, SIZE))
print("""
#  : Cum. Avg. <- Result   
---------------------------
""".strip())
selection_keys = list(random.sample(keys, SELECTION_SIZE))
total = 0

for i in range(1, 100+1):
    time1 = timeit.timeit(lambda: dict1_selection(data, keys), number=SELECTION_TESTS)
    time2 = timeit.timeit(lambda: dict2_selection(data, keys), number=SELECTION_TESTS)

    ratio = time1/time2
    total += ratio

    print("{:<3}: {:.7f} <- {:.7f}".format(i, total/i, ratio))

print()
print("Direct ran in {:.2f}% of the time of get, on average over {} tests.".format(total, i))
    


