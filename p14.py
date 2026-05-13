# Recursion : When a function calls itself

# infinite recursion which gives stack overflow error in other 
# languages but pythob is smart it runs upto 987 timee only and 
# stops.
# def greet(): #RecursionError: maximum recursion depth exceeded
#     print("Vaibhav")
#     greet()
# greet()

# 1. HEAD RECURSION: 1st job and calls function.
# using global
# TC = O(N+1) = O(N)
# SC = O(N+1) = O(N)
# count = 0
# def greet():
#     global count
#     if count == 4:
#         return
#     print("vaibhav")
#     count += 1
#     greet()
# greet()

# not using global
# def greet(count):
#     if count == 4:
#         return
#     print("vaibhav")
#     greet(count + 1)

# greet(0)

# TAIL RECURSION: 1st calls the function and then dos its job.
# also called backtracking
# TC = O(N+1) = O(N)
# SC = O(N+1) = O(N)
# def greet(count):
#     if count == 4:
#         return
#     greet(count+1)
#     print(f"Vaibhav{count}")
# greet(0)

count = 0
def greet():
    global count
    if count == 4:
        return
    count += 1
    greet()
    print("vaibhav")
greet()