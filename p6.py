
def is_prime(n):
    # Check if number is less than 2 (not prime)
    if n < 2:
        return False
    
    # Check if number is 2 (prime)
    if n == 2:
        return True
    
    # Check if number is even (not prime except for 2)
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

# Example usage to print True or False
number = int(input("Enter a number: "))
print(is_prime(number)) 