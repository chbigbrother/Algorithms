
import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    
    for i in dict(Counter(a)).items():
        
        if i[1] == 1:
            return i[0]
