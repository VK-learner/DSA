# Parameterized and Functional Recursion
# TC : O(N)
# SC : in worst case is O(N) i.e, Stack Space bhara aur finish ho gaya
# Sum of 1 to N [Parameterized]

# def func(Sum,i,N):
#     if i > N:
#         print(Sum)
#         return
#     func(Sum+i,i+1,N)
# func(0,1,4) # 1+2+3+4 = 10 
    
# Sum of 1 to N [Functional Recursion]
def func(i,N):
    if i > N:
        return 0
    return i + func(i+1,N)
print(func(1,4)) # 1+2+3+4 = 10

# OR

def func(N):
    if N == 1:
        return 1
    return N + func(N-1)    
print(func(4)) # 1+2+3+4 = 10

# factorial 0f n [Functional Recursion]
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)    
print(fact(4)) 