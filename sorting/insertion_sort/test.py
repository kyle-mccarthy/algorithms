import random
import copy
from insertion_sort import *

# create test data
test = random.sample(range(100), 35)
test_cpy = copy.copy(test)

# run the sorting, our implementation and pythons implementation
insertion_sort(test)
test_cpy.sort()

assert test == test_cpy
print("test equals test_cpy")
