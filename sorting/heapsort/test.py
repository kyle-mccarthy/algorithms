import random
import copy
from heapsort import *

# create test data
test = random.sample(range(1000), 500)
test_cpy = test.copy()

heap = Heap(test)
heap.heap_sort()

test_cpy.sort()

assert heap.a == test_cpy
print("sorted test equals sorted test_cpy")
