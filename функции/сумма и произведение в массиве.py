#5 дан массив чисел, найти сумму и произведение
s = 0
p = 1 # не понимаю, откуда 1 - нужно запомнить
for q in range (1, 11):
    s += q
    p *= q
print(s)
print(p)
