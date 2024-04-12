import random

list_of_random_numbers = []

ordered_list = []


for _ in range(12):
    list_of_random_numbers.append(random.randint(1, 50))

for _ in range(len(list_of_random_numbers)):
    ordered_list = ordered_list + [min(list_of_random_numbers)]
    list_of_random_numbers.remove(min(list_of_random_numbers))

print(ordered_list)
