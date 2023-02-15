
import math
import os
import random
import re
import sys
from itertools import permutations
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    value = []
    for i in permutations(arr, 4):
        value.append(sum(i))
    print("{} {}".format(min(value),max(value)))
    
