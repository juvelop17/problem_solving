

def binary_search(li, target):
    start = 0
    end = len(li) - 1
    while start <= end:
        mid = int((start + end)/2)
        if li[mid] == target:
            return mid
        elif li[mid] > target:
            end = mid - 1
        elif li[mid] < target:
            start = mid + 1

    return None



li = [1,2,3,4,5,6,7,8,9]
print(li[0:1])
print(li[-0])
print(li[-1])

# for i in range(5,0,-1):
#     print(i)


# print(binary_search(li, 10))
# li.insert(0,-1)
# print(li)
# li.insert(1,-2)
# print(li)


print(type(int('10')))
print(type([map(int, ['1','2'])]))
_l = ['1','2']

def te(_d):
    return int(_d)

test=list(map(int,_l))
print(test)

print(abs(-1))


li = [[] for _ in range(5)]
print(li)