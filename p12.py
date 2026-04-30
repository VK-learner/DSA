# Store Frequency in Dictionary
# Time Complexity = 𝑂(𝑛)
# Space Complexity = O(n) ---> i worst case if all keys are unique
# def frequency(num):
#     dictionary = dict()
#     for num in num:#O(n)
#         if num not in dictionary:#O(i)
#             dictionary[num] = 1#O(i)
#         else:
#             dictionary[num] += 1#O(i)
#     return dictionary
# print(frequency([5,6,7,7,1,9,111,1,1,5,1,1]))

#  Store Frequency in Dictionary
# Time Complexity = 𝑂(𝑛)
# Space Complexity = O(n) ---> in worst case if all keys are unique
# num = [5,6,7,7,1,9,111,1,1,5,1,1]
# dictionary = {}
# for i in range(len(num)):
#     if num[i] in dictionary:
#         dictionary[num[i]]+=1
#     else:
#         dictionary[num[i]] = 1
# print(dictionary)

# method 2 using hashmap
# hashmap = {'a':1,'b':2,'c':3}
# print(hashmap.get('d','not found this key value'))

# hashmap = {'a':1,'b':2,'c':3}
# try:
#     print(hashmap['d'])
# except KeyError:
#     print("not found this key value")

def frequency(num):
    n = len(num)
    hashmap = {}
    for i in range(0,len(num)):
        hashmap[num[i]] = hashmap.get(num[i],0)+1
    return hashmap
print(frequency([5,6,7,7,1,9,111,1,1,5,1,1]))


