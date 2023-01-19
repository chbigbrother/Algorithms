# Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. 
# If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

from collections import Counter
#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    arr = sorted(arr)
    arr = Counter(arr)

    v = []
    for i in arr:
        if arr[i] == max(arr.values()):
            v.append(i)
            
    val = min(v)
    return val
    
