# # Check if a string  is Palindrome or not
# string = 'MOMD'
# if string == string[::-1]:
#     print('Palindrome')

# # using loop
# S = 'ANBCDDCBNA'
# L = 0
# R = len(S) - 1
# for i in range(len(S)//2):
#     if S[L] != S[R]:
#         print('Not Palindrome')
#         break
#     L += 1
#     R -= 1
# else:
#     print('Palindrome')

# using function

def is_palindrome(string):
    L = 0
    R = len(string) - 1
    while L < R:
        if string[L] != string[R]:
            return False
        L += 1
        R -= 1
    return True
result = is_palindrome('MOM')
if result:
    print('Palindrome')
else:
    print('Not Palindrome')