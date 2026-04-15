# 1. Always calculate TC in terms of worst case
# 2. O(1) is better than O(n), which is better than O(n^2), etc.
# O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)

age = int(input("Enter your age: "))

if age >= 80:
    print("You are a super senior citizen.")
elif age >= 60:
    print("You are a senior citizen.")
elif age >= 24:
    print("You are a working professional.")
elif age >= 16:
    print("You are a teen.")
else:
    print("You are a child.")

# best/worst case: O(1) (worst case performs 5 constant comparisons)