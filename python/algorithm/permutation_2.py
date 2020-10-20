
import itertools

def permutations(arr, r):
    res = []
    for i in range(len(arr)):
        if r == 1:
            res.append([arr[i]])
        else:
            for perm in permutations(arr[:i] + arr[i+1:], r-1):
                res.append([arr[i]] + perm)
    return res

def product(arr, r):
    res = []
    for i in range(len(arr)):
        if r == 1:
            res.append([arr[i]])
        else:
            for perm in product(arr, r-1):
                res.append([arr[i]] + perm)
    return res

arr = [i for i in range(5)]
r = 2
print(list(itertools.permutations(arr, r)))
print(permutations(arr, r))

print(list(itertools.product(arr, repeat=r)))
print(product(arr, r))











