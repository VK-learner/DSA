# Recursion using parameters
def greet(n,m):
    if m==0:
        return
    print(n,m)
    greet(n,m-1)
greet("vaibhav",10)

# Recursion using parameters
# def greet(x,n):
#     if n==0:
#         break # shows error because break is used only in loops.
#     print(x,n)
#     greet(x,n-1)
# greet("vaibhav",5)

# Print 1 to N using Recursion
def print1toN(n):
    if n==0:
        return
    print1toN(n-1)
    print(n)

print1toN(10)

# OR
def printitoN(i,N):
    if i > N:
        return
    print(i) #this is Head Recursion
    printitoN(i+1,N)
    # print(i) # this reverse N to i also called back tracking or Tail Recursion
printitoN(1,5)