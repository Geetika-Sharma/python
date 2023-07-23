fruits = ["Apple", "Litchi", "Mango"]

for fruit in fruits:
    print(fruit)

# Append fruit
fruits.append("Bananas")
fruits.insert(0,"Pineapple")

print(fruits[3])
print(fruits[0])

# Delete element
fruits.remove("Bananas")
print(fruits)
print(len(fruits))


# Concatenate
list1 = [1,2,3]
list2 = ["John", "Doe"]
combined_list = list1 + list2
print(combined_list)

# Repetition
repeated_list = list1 * 3
print(repeated_list)

# Check Membership
print("Apple" in fruits)