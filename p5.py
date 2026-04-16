# Time limit exceeded error [TLE]
def selection_sort(arr):
    """
    Perform selection sort on a list.

    Selection sort works by repeatedly finding the minimum element
    from the unsorted portion of the list and placing it at the
    beginning. Time complexity is O(n^2) in both best and worst cases.

    Parameters:
        arr (list): List of comparable elements to be sorted.

    Returns:
        list: Sorted list in ascending order.
        """
    n = len(arr)
    for i in range(n - 1):
        # Assume the current index holds the minimum
        min_index = i
        # Find the smallest element in the remaining unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
print(selection_sort([64, 25, 12, 22, 11]))
# # Example usage
# numbers = [64, 25, 12, 22, 11]
# print("Original:", numbers)
# print("Sorted:  ", selection_sort(numbers))
# Inefficient O(n) approach
# def is_prime(n):
#     """Check if a number is prime."""
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# # Inline input directly inside print
# print(f"{(x := int(input('Enter a number: ')))} -> {is_prime(x)}")
# print(help(is_prime))