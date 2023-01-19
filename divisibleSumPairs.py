
#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    cnt = 0

    for i in range(len(ar)):
        for j in range(len(ar[i+1:])):
            n = (ar[i] + ar[j+i+1]) / k
            it = int(n)
            if n == it:   
                cnt += 1
            
    return cnt;
