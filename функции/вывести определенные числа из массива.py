# ДЗ №3 вывести на экран все четные числа диапазона от 1 до  497  (в строчку)
for x in range(1,498):
    if x % 2 == 0:
        print(x, "", end='')