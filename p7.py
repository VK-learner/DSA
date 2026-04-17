# dict = {'a': 1, 'b': 2, 'c': 3}
# for key in dict:
#    print(key)

# for key, values in dict.items():
#     print(f'{key} --> {values}')
# phoneBook = {'Name':[], 'Phone No':[]}
# phoneBook['Name'].append('John')
# phoneBook['Phone No'].append('123456789')
# phoneBook['Name'].append('Jane')
# phoneBook['Phone No'].append('987654321')
# for name, phone in zip(phoneBook['Name'], phoneBook['Phone No']):
#   print(f"{name} -> {phone}")

phoneBook = {"Name": [], "Phone No": []}

# Ask how many entries to store
n = int(input("How many contacts do you want to add? "))

for i in range(1, n + 1):
    name = input(f"Enter name {i}: ")
    phone = input(f"Enter phone number {i}: ")
    phoneBook["Name"].append(name)
    phoneBook["Phone No"].append(phone)

# Print neatly
print("\nStored Contacts:")
for name, phone in zip(phoneBook["Name"], phoneBook["Phone No"]):
    print(f"{name} -> {phone}")
