#  Print All Factors of a Given Number 

# print factors/divisors
# arr = [1,2,3,4,5,6,7,8,9,10]
# n=10
# div = []
# for i in range(len(arr)):
#     if n%arr[i]==0:
#         div.append(arr[i])
# print(div)

# Pythonic Approach
# arr = [x for x in range(1,1+int(input("Enter the number range:")))]
# n = int(input("enter the digit of which you want to find factors:"))
# result = [x for x in arr if n%x==0]
# print(result)

# extreme Brute Force
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

# Better Approach
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

# better approach
# TC ---> O(N/2) or simply O(N)
# result = []
# def divisors(n):
#     num = n
#     for i in range(1,num//2+1):# O(N/2)
#         if num%i == 0:
#             result.append(i)
#     result.append(num) # O(1)
#     return result
# print(divisors(10))

# optimal solution
# TC ---> O(√𝑛)
from math import sqrt
num = 36
result = []
for i in range(1,int(sqrt(num))+1):#O(√𝑛)
    if num % i == 0:#O(1)
        result.append(i)#O(1)
        if num//i != i:#O(1)
            result.append(num//i)#O(1)
print(result)
print([result.sort()])# remember that the TC of sorting is O(NlogN)
# total TC = O(√N) + O(NlogN)
# SC = O(k) were k is the amount of factors.