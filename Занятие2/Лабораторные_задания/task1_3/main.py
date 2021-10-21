a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

result_1 = (a ** 2 ) + (b ** 2)
result_2 = (a + b) ** 2

if result_1 > result_2:
    print("Сумма квадратов боьше: ", result_1, " > ", result_2)
elif result_1 < result_2:
    print("Квадрат суммы боьше: ", result_2, " > ", result_1)
else:
    print("Суммы равны")

