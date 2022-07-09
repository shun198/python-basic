import grp
from locale import currency


fruits = ['apple', 'grape', 'orange']
fruits.insert(2, 'banana')
print(fruits)

group = ["Eric", "John", "Michael"]
group.remove("John")
print(group)

movies = ["Harry Potter", "The Matrix", "The Shawshank Redemption"]
movies.sort(reverse=True)
print(movies)

currency = ["USD", "EUR", "JPY"]
print(len(currency))
