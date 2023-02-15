# arr = [1, 1, 0, -1, -1]
# output: 0.400000
#         0.400000
#         0.200000

def plusMinus(arr):
    # Write your code here
    # Write your code here
    dicts = {"plus": 0, "minus": 0, "zero": 0}
    for i in arr:
        if i > 0:
            dicts["plus"] += 1
        elif i == 0:
            dicts["zero"] += 1
        else:
            dicts["minus"] += 1
    for i in dicts.values():
        print("{:.6f}".format(i/len(arr)))
