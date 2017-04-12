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

def selection(data, keys):
    for key in keys:
        pass

print()
print("Execution Tests {} random keys (of {})".format(SELECTION_SIZE, SIZE))
print("""
#  : Cum. Avg. <- Result   
---------------------------
""".strip())
selection_keys = list(random.sample(keys, SELECTION_SIZE))
total = 0
total_comp = 0

for i in range(1, 100+1):
    time_loop = timeit.timeit(lambda: selection(data, keys), number=SELECTION_TESTS)

    time1 = timeit.timeit(lambda: dict1_selection(data, keys), number=SELECTION_TESTS)
    time2 = timeit.timeit(lambda: dict2_selection(data, keys), number=SELECTION_TESTS)

    time1_comp = time1 - time_loop
    time2_comp = time2 - time_loop

    ratio = time1/time2
    total += ratio

    print("{:<3}: {:.7f} <- {:.7f}".format(i, total/i, ratio), end="; ")

    ratio_comp = time1_comp/time2_comp
    total_comp += ratio_comp

    print("{:<3}: {:.7f} <- {:.7f}".format(i, total_comp/i, ratio_comp))

print()
print("On average, over {} tests: ".format(i))
print("Uncompensated: ")
print("  Direct ran in {:.2f}% of the time of get.".format(total))
print("Compensated for Loop Time: ")
print("  Direct ran in {:.2f}% of the time of get.".format(total_comp, i))
    


