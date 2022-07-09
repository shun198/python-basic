fruits = {1: "apple", 2: "banana", 3: "orange"}
print(fruits[1])

for fruit in fruits.keys():
    print(fruit)

for fruit in fruits.values():
    print(fruit)

for key, value in fruits.items():
    print(key)
    print(value)

print(fruits.get(4, "fruits not found"))

fruits_2 = {4: "grape", 5: "cherry", 6: "mango"}
fruits.update(fruits_2)
print(fruits)
