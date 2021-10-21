speed = int(input("Скорость передачи данных по локальной, бит/сек "))
time = int(input("Время скачивания, мин "))
coast = int(input("Стоимость Гигабайта, руб "))

ras = (speed/1073741824) * (time * 60)

money = ((round(ras, 5) - 1) * coast)

print(round(ras, 5), money)