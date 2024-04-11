import random

list1 = [random.randint(1, 50) for _ in range(12)]
list2 = [list1.pop(list1.index(min(list1))) for _ in range(len(list1))]

print(list2)
