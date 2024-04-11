import random
from faker import Faker

# You need to write in cmd "pip install -r requirements.txt"

fake = Faker()

list_name = [fake.name() for _ in range(10)]
list_mark = [random.randint(1, 12) for _ in range(10)]

for ind in range(len(list_mark)): print(f"{list_name[ind]} - {list_mark[ind]}")

for i in range(100): print("-", end="")
print()

paired_list = sorted(list(zip(list_name, list_mark)))

for ind in paired_list: print(f"{ind[0]} - {ind[1]}")