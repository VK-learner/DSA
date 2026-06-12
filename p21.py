# selection sort
nums = [5,7,8,4,1,6,9,2]
def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums
print(selection_sort(nums))
# TC = O(N(N+1)/2) = O(N^2)
# SC = O(4) = O(1), where 4 is for min_idx, i, j and temp variable min_idx used for swapping.