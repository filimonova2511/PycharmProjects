# 3.Ведьмаку заплатите чеканной монетой
# Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево, к тому же ведьмак
# не принимает купюры, он принимает только чеканные монеты. В мире ведьмака существуют монеты с номиналами
# 1, 5, 10, 25.
# Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.
# Пример: На вход подается число 49.Ответом будет 7(25 + 10 + 10 + 1 + 1 + 1 + 1) те минимальное количество монет)
a = int(input("введите число - "))
m1, m2, m3, m4 = 1, 5, 10, 25 # монеты
i1, i2, i3, i4 = 0, 0, 0, 0  # счетчик монет
while a >= m4:
    a -= m4
    i4 += 1
print(i4, "монеты по 25")
while m3 <= a < m4:
    a -= m3
    i3 += 1
print(i3, "монеты по 10")
while m2 <= a < m3:
    a -= m2
    i2 += 1
print(i2, "монеты по 5")
while m1 <= a < m2:
    a -= m1
    i1 += 1
print(i1, "монеты по 1")
print("всего монет -", i1+i2+i3+i4)
