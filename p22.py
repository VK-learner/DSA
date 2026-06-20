# Bubble Sort Algorithm Implementation in Python
num = [5,8,1,6,9,2,4]
n = len(num)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if num[j] > num[j+1]:
#             num[j], num[j+1] = num[j+1], num[j]
# print(num)
# Optimized Bubble Sort Algorithm Implementation in Python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
num = bubble_sort(num)
# OR
# Optimized Bubble Sort Algorithm Implementation in Python
for i in range(n-2,-1,-1):
    swapped = False
    for j in range(0, i+1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
            swapped = True
    if not swapped:
        break
print(num)

# Time Complexity: O(n(n+1)/2) = O(n^2) in the worst and average case, O(n) in the best case (when the list is already sorted).
# Space Complexity: O(1) since it is an in-place sorting algorithm.