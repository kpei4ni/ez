list_of_names = ["Анна", "Олексій", "Ірина",
                 "Михайло", "Катерина", "Андрій",
                 "Вікторія", "Олена", "Іван",
                 "Марія"]

list_of_grades = [7, 3, 1, 9, 5, 2, 10, 6, 4, 8]

print("Список до сортування:")
for i in range(len(list_of_names)): print(list_of_names[i], "-", list_of_grades[i])

length = len(list_of_names)

combined_list = sorted(list(zip(list_of_names, list_of_grades)))

print()
print("Список після сортування:")
print()

for ind, val in combined_list:
    print(f"{ind} - {val}")