# Extraction of Digits from a Number
n = 22345
num = n
while num > 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10
