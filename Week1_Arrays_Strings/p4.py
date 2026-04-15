# -----------------------------------------
# SPACE COMPLEXITY = Auxiliary Space + Input Space 
# Auxiliary Space : The extra space used to solve the problem.
# Input Space : The space used to store the input.
# EXAMPLE
# -----------------------------------------

def sum_of_elements(arr):
    """
    This function calculates the sum of elements in a list.
    """

    # -------------------------------
    # INPUT SPACE
    # -------------------------------
    # 'arr' is the input provided to the function.
    # Memory used to store this list is called INPUT SPACE.
    # If size of arr = n → Input Space = O(n)

    total = 0  
    # -------------------------------
    # AUXILIARY SPACE
    # -------------------------------
    # 'total' is an extra variable used to compute the result.
    # This is NOT part of input → so it's AUXILIARY SPACE.
    # It takes constant space → O(1)

    for num in arr:  
        # 'num' is a loop variable → also auxiliary (temporary)
        total += num

    return total


# -------------------------------
# DRIVER CODE
# -------------------------------
arr = [5, 10, 15, 20, 25, 25]

result = sum_of_elements(arr)
print(result)