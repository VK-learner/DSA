import os

# Step 1: Delete p6.py if it exists
if os.path.exists("p6.py"):
    os.remove("p6.py")
    print("Deleted p6.py")

# Step 2: Rename files from p7...p10 down to p6...p9
for i in range(7, 11):  # 7 to 10 inclusive
    old_name = f"p{i}.py"
    new_name = f"p{i-1}.py"
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed {old_name} -> {new_name}")
