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

# using while loop and function
# TC = O(N/2) => O(N) & SC = O(2) => O(1) since we used only 2 variables
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

# using recursion
# TC = O(N/2) => O(N)
# SC = O(N/2) => O(N)
# since we are using recursion and the maximum depth of the recursion will be N/2
def is_palindrome(string, L, R):
    if L >= R:
        return True
    if string[L] != string[R]:
        return False
    return is_palindrome(string, L + 1, R - 1)

result = is_palindrome('MOM', 0, len('MOM') - 1)
if result:
    print('Palindrome')
else:
    print('Not Palindrome')