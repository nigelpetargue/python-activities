# print('hello world')

# collections
# list = ordered and mutable, allow duplication
# set = unordered and immutable, can add/remove element, unique elements
# tuple = ordered and imutable, allow duplication

fruits = ["apple", "orange", "banana", "coconut", "apple"]

fruits.append("pineapple")
fruits.insert(5, "grapes")
# fruits.reverse()
# fruits.sort()

print(f"the index of 2 is {fruits[:3]}")

removed = fruits.pop(2)
count = fruits.count("apple")
index = fruits.index("orange")

print(f"removed {removed}")
print(f"count {count}")
print(f"index {index}")

# fruits.clear()

print(fruits)


# for fruit in fruits:
#     print(fruit)

is_admin = False

if is_admin:
    print(f"is_admin {is_admin}")
else:
    print(f"not admin {is_admin}")
