# Armstrong Number
# Time Complexity = 𝑂(log10(𝑛)) OR simply, O(log n)
# Space Complexity = O(1)
def armstrong(n):
    num = n
    nod = len(str(n))
    sum = 0
    while num > 0:
        ld = num%10
        sum+=ld**nod
        num = num//10
    return sum == n
print(armstrong(153))