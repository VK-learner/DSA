# Reverse an Array using Recursion
# TC : O(N/2) = O(N), because we are swapping two elements at a time, so we are traversing only half of the array
# SC : O(N/2) = O(N), Stack Space, because recursion is involved
nums = [5, 7, 3, 2, 6, 1, 5, 9]
def reverse(nums, left, right):
    if left >= right:
        return nums   # return the list when done
    nums[left], nums[right] = nums[right], nums[left]
    return reverse(nums, left+1, right-1)


def reverse_array(nums, left, right):
    return reverse(nums, left, right)

print(reverse_array(nums, 1, 5))



# num = [5, 7, 3, 2, 6, 1, 5, 9]
# num[2:5] = num[2:5][::-1]
# print(num)