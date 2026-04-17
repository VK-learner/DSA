def palindrome(n: int) -> bool:
    num = n
    result = 0
    while num > 0:
        last_digit = num % 10
        result = result * 10 + last_digit
        num = num // 10
    return n == result


while True:
    n = int(input("Enter a number (or 0 to exit): "))
    if n == 0:
        print("Exiting...")
        break
    print(f"{n} is palindrome? {palindrome(n)}")

# def palindrome(n):
#   b = str(n)
#   if b == b[::-1]:
#      print("Palindrome")
#   else:
#      print("Not a Palindrome")
# while True:
#    palindrome(input("Enter a number: "))
