# Hashing in python : Prestoring values into some datastructure like List/Dctionary/Sets 
# and then fetching it.

#  Q1. check how many times the elements of m[] gets repeated in n[].
# Constraints: 
# 1. 1<=n[i]<=10 
# 2. n can have 10**8 elements
# 3. m can have 10**8 elements

# Method 1
# TC : O(m*n)
# SC : O(1)
# worst case n=m=10**8 => n*m = 10**16 which shows TLE so we have to make it optimal.
# n = [5,3,2,2,1,5,5,7,5, 10]
# m = [10,111,1,9,5,67,2]
# for num in m:
#     count = 0
#     for x in n:
#         if x == num:
#             count+=1
#     print(count)

# Method 2 optimal
# TC : O(n+m) in worst case if n=m=10**8 => O(10^8+10^8) => O(2*10^8) or O(10^8)
# SC : O(11) 0r O(1)
# n = [5,3,2,2,1,5,5,7,5, 10] # constraint: 1<=n[i]<=10
# m = [10,111,1,9,5,67,2]
# hash_list = [0]*11 # [0,0,0,0,0,0,0,0,0,0,0]
# # 1st store the freq of n in hash_list, then compare the slements of m with hash_list.
# for num in n: #O(n)
#     hash_list[num] += 1 # stores the freq of n in hash_list

# for num in m:#O(m)
#     if num<1 or num>10:
#         print(0)
#     else:
#         print(hash_list[num])

# Method 3, Dictionary
# n = [5,3,2,2,1,5,5,7,5, 10]
# m = [10,111,1,9,5,67,2]
# freq_dict = dict()
# for i in n:
#     cont = 0
#     if i not in freq_dict:
#         freq_dict[i]=1
#     else:
#         freq_dict[i]+=1
# print(freq_dict)
# for i in m:
#     if i in freq_dict:
#         print(freq_dict[i])
#     else:
#         print(0)
    
# Q2. Character hashing
# Constraints : 'a'<=s[i]<='z'
# TC : O(m+n)
# SC : O(L) = O(26) or O(1) because 26 is constant
s = "azyxyyzaaaa"
q = ['d','a','y','x']
L = 26
hash_list = [0]*L
for ch in s: # O(s) or O(n)
    ascii_value = ord(ch)
    index = ascii_value-97
    hash_list[index] += 1
print(hash_list)
for ch in q: # O(q) or O(m)
    ascii_value = ord(ch)
    index = ascii_value-97
    print(hash_list[index])