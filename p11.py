#  Print All Factors of a Given Number 

#1. extreme Brute Force
# Time Complexity = 𝑂(𝑛)
# Space Complexity = O(k) ---> k would be the total number of factors
# result = []
# def divisors(n):
#     num = n
#     for i in range(1,num+1):
#         if num%i==0:
#             result.append(i)
#     return result
# print(divisors(10))

#2. better approach
# TC ---> O(N/2) or simply O(N)
# SC ---> O(k) where k is the total number of factors
# result = []
# def divisors(n):
#     """
#     Find all divisors of a given number `n`.

#     Idea:
#     - A divisor is any integer that divides `n` without leaving a remainder.
#     - Instead of checking all numbers from 1 to n, we only need to check up to n//2,
#       because no number greater than n//2 (except n itself) can divide n.
#     - For each i in [1, n//2], if n % i == 0, then i is a divisor.
#     - Finally, we add n itself as a divisor.

#     Time Complexity (TC):
#     - O(n/2) → simplified as O(n), since we iterate through half the numbers.

#     Space Complexity (SC):
#     - O(k), where k is the number of divisors found and stored in the result list.
#     """
#     num = n
#     for i in range(1,num//2+1):# O(N/2)
#         if num%i == 0:
#             result.append(i)
#     result.append(num) # O(1)
#     return result
# print(divisors(10))

#3.1 optimal solution
# TC ---> O(√𝑛)
# SC ---> O(k) where k is the total number of factors
# total TC = O(√N) + O(NlogN)
from math import sqrt
def divisors(n):
    '''
    Return all divisors of a given integer `num` using the √n optimization.

    Concept:
    - Divisors always come in pairs: if `i` divides `num`, then `num // i` also divides `num`.
      Example: 2 divides 10 (2 * 5 = 10), so 5 must also divide 10 (5 * 2 = 10).
    - Because of this pairing, we only need to check numbers up to √n.
      For each divisor `i` found, we add both `i` and its partner `num // i`.
    - When `i` equals √n (perfect square case), we add it only once to avoid duplication.
    - Finally, we sort the list of divisors for readability.

    Time Complexity:
    - O(√n) for finding divisors.
    - O(k log k) for sorting, where k is the number of divisors.
    - Total: O(√n + k log k).

    Space Complexity:
    - O(k), where k is the number of divisors stored.
    '''
    num = n
    result = []
    for i in range(1,int(sqrt(num))+1):#O(√𝑛)
        if num % i == 0:#O(1)
            result.append(i)#O(1)
            if num//i != i:#O(1)
                result.append(num//i)#O(1)
    return result
factors = divisors(25)
print(factors)
print(sorted(factors))# remember that the TC of sorting is O(NlogN)

#3.2 Better Approach
# if interviewer asks write code without using math then
# Time Complexity = 𝑂(√𝑛)
# Space Complexity = O(k) ---> k would be the total number of factors
# result = []
# def divisors(n):
#     num = n
#     for i in range(1,int(num**0.5)+1):
#         if num%i==0:
#             result.append(i)
#             if i != num//i:
#                 result.append(num//i)
#     return result

# Pythonic Approach
# arr = [x for x in range(1,1+int(input("Enter the number range:")))]
# n = int(input("enter the digit of which you want to find factors:"))
# result = [x for x in arr if n%x==0]
# print(result)
# SC = O(k) were k is the amount of factors.

# print factors/divisors
# arr = [1,2,3,4,5,6,7,8,9,10]
# n=10
# div = []
# for i in range(len(arr)):
#     if n%arr[i]==0:
#         div.append(arr[i])
# print(div)
