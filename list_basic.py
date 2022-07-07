from collections import deque
fruits = ['apple', 'grape', 'orange']
print(fruits)
shop_list = ['cherry', 8, 3, False, fruits]
print(shop_list)
print(shop_list[0])
print(shop_list[-4])
print(shop_list[-1][2])

stack = [1, 2, 3]
stack.append(4)
stack.append(5)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue)
queue.popleft()                 # The first to arrive now leaves
print(queue)
queue.popleft()                 # The second to arrive now leaves
print(queue)
# Remaining queue in order of arrival
