# mutable
fruits = ['apple', 'banana', 'orange']
print(f"fruitsのIDは{id(fruits)}")
fruits.append('grape')
print(f"fruitsのIDは{id(fruits)}")

# immutable
fruit = 'apple'
print(f"fruitのIDは{id(fruit)}")
fruit += 'grape'
print(f"fruitのIDは{id(fruit)}")
