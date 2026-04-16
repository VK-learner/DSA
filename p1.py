# ==========================================
# ARRAY FUNDAMENTALS
# ==========================================

# Creating arrays
arr = [3, 1, 4, 1, 5, 9, 2, 6]

# Key operations and their TIME COMPLEXITY
arr.append(7)        # O(1) — add to end
arr.pop()            # O(1) — remove from end
arr.pop(0)           # O(n) ⚠️ — remove from front (all elements shift!)
arr.insert(2, 99)    # O(n) ⚠️ — insert at index
arr[3]               # O(1) ✅ — index access (this is arrays' superpower)
len(arr)             # O(1)

# Traversal
for i in range(len(arr)):        # index-based
    print(arr[i])

for val in arr:                  # value-based (cleaner)
    print(val)

for i, val in enumerate(arr):   # both index AND value (best of both)
    print(i, val)
# a = [1,2,3,4,5,6,7,8,9,10]
# print(a[0]) # 1
# print(a.pop()) # 2
# print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a.append(11)
# print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
# # for i in a:
# #     print(i) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 11
# for i,j in enumerate(a, start=1):
#     print(f"{i}|{j}")
