# range(1,10)
def myrange(stop):
    start = 0
    while start < stop:
        yield start
        start += 1


mr = myrange(10)
print(type(mr))

for i in mr:
    print(i)
