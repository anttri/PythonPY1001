a = int(input("Введите число: "))

result = (a % 2) == 0 or (a % 3) == 0

if result:
    print("Кратно")
else:
    print("Не кратно")


