# def fibonnaci(n):
#     arr  = [0,1]
#     for i in range(0,n-2):
#         arr.append(arr[i]+arr[i+1])
#     return arr
# print(fibonnaci(5))

# # cleaner version
# def fibonacci(n):
#     arr = [0, 1]
#     for i in range(2, n):
#         arr.append(arr[i-1] + arr[i-2])
#     return arr

# print(fibonacci(5))  # [0, 1, 1, 2, 3]


# Recursion approach for Fibonacci
# Time Complexity (TC) = O(2^n) because each call branches into two recursive calls
# Space Complexity (SC) = O(n) because recursion depth can go up to n
# Example sequence:
# f =  [0, 1, 1, 2, 3, 5, 8, 13]
# n =   0, 1, 2, 3, 4, 5, 6, 7
# f(6) = f(5) + f(4) = 5 + 3 = 8
# General formula: f(n) = f(n-1) + f(n-2)

class Soln:
    # Static method: does not need 'self' because it doesn't depend on object state
    @staticmethod
    def fib(n: int) -> int:
        """
        Recursive Fibonacci function.
        Takes an integer n and returns the nth Fibonacci number.
        """
        # Base case: if n is 0 or 1, return n directly
        if n == 0 or n == 1:
            return n
        # Recursive case: f(n) = f(n-1) + f(n-2)
        return Soln.fib(n-1) + Soln.fib(n-2)

    # Instance method: wrapper around fib, allows calling via an object
    def f(self, n: int) -> int:
        """
        Wrapper method that calls the static fib function.
        Useful if you want to use object-oriented style.
        """
        return self.fib(n)


# ✅ Usage examples:

# Call static method directly using the class
print(Soln.fib(5))   # Output: 5

# Or create an object and call the instance method
fs = Soln()
print(fs.f(6))       # Output: 8
