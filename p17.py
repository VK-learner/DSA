# Find the Factorial of a Number
# TC : O(N)
# SC : O(N), Stack Space, because recursion is involved
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(1)) # 5*4*3*2*1 = 120
# return 5 * factorial(4) = 5 * 24 = 120
# return 4 * factorial(3) = 4 * 6  = 24
# return 3 * factorial(2) = 3 * 2  = 6
# return 2 * factorial(1) = 2 * 1  = 2
# return 1 * factorial(0) = 1 * 1  = 1

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5)) # 5*4*3*2*1 = 120