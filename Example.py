with open("Families.txt", encoding="utf-8") as file:
    families = [line.strip() for line in file]

# Запрашиваем у пользователя имя и фамилию
name_surname = input("Введите имя и фамилию через пробел: ")

# Разбиваем строку на имя и фамилию
name, surname = name_surname.split()

# Фильтруем фамилии по началу и концу
matching_families = [f for f in families if f.startswith(surname[0]) and f.endswith(surname[-1])]

# Выводим список подходящих фамилий
print("Подходящие фамилии:")
for f in matching_families:
    print(f)
