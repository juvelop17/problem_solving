

# import math
#
# def divisorGenerator(n):
#     large_divisors = []
#     for i in range(1, int(math.sqrt(n) + 1)):
#         if n % i == 0:
#             yield i
#             if i*i != n:
#                 large_divisors.append(int(n / i))
#     for divisor in reversed(large_divisors):
#         yield divisor
#
# print (list(divisorGenerator(10**9)))
#



n=10**9
a = [False,False] + [True]*(n-1)
primes=[]
print('good')

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(i, n+1, i):
        a[j] = False
