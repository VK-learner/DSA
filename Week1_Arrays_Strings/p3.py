# 1. Always calculate TC in terms of worst case
# 2. Avoid constant values
# 3. Avoid lower bound checks (e.g. age >= 16) if not needed.
#    TC ---> O(8N^6 + 3N^2 + 15)
#     = O(N^6) (drop constants and lower order terms)
#     = O(1) (if N is constant, e.g. 1000)
# different types of TC's
# 1. Big O (worst case)
# 2. Big Omega (best case)
# 3. Big Theta (average case)

# example 1:
import numpy as n
def print_pairs(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i,j) # O(n^2)
# print_pairs(3)

# example 2:
def print_nums(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,j) # O(n(n+1)/2) = O(n^2)
print_nums(3)
