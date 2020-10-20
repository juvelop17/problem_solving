
import itertools


def combinations(arr, r):
    res = []
    for i in range(len(arr)):
        if r == 1:
            res.append([arr[i]])
        else:
            for comb in combinations(arr[i+1:],r-1):
                res.append([arr[i]] + comb)
    return res

def combinations_with_replacement(arr, r):
    res = []
    for i in range(len(arr)):
        if r == 1:
            res.append([arr[i]])
        else:
            for comb in combinations_with_replacement(arr[i:],r-1):
                res.append([arr[i]] + comb)
    return res

arr = [i for i in range(5)]
r = 2
print(list(itertools.combinations(arr, r)))
print(combinations(arr, r))

print(list(itertools.combinations_with_replacement(arr, r)))
print(combinations_with_replacement(arr, r))











