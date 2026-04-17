# Time Complexity = 𝑂(log10(𝑛)) OR simply, O(log n)
# Space Complexity = O(1)
n = 12345
num = n
count = 0
while num > 0:
    count += 1
    num = num // 10
print(f"Number of digits in {n} is {count}")
# or
# print(f"Number of digits in {n} is {len(str(n))}")
# log10(12345) = 4.091549449716781 + 1 = 5.091549449716781  = 5
# import math
# print(f"Number of digits in {n} is {math.floor(math.log10(n)) + 1}")
