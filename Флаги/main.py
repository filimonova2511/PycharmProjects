#№1 Подводится баланс коммерческого предприятия. Входные данные: получаем от пользователя доходы и расходы.
# Дальнейшие действия могут зависеть от того, будет он положительным (доходы выше расходов) или отрицательным (расходы превышают доходы).
# Если отрицательный, надо просить кредит, положительный — планировать отпуск.

# balans = True
# debit = int(input("Введите доходы -"))
# kredit = int(input("Введите расходы -"))
# res = debit - kredit
# if res < 0:
#     balans = False
# if balans == False:
#     print("просить кредит")
# else:
#     print("планировать отпуск")

# Решаем квадратное уравнение. Если дискриминант не отрицательный — ищем корни.
# Для хода вычислительного процесса важен факт не отрицательности, который также содержит 1 бит информации и может,
# таким образом, быть сохранен с помощью логической переменной.

import math
a,b,c = float(input("число 1 = ")), float(input("число 2 = ")), float(input("число 3 = "))
res = True
d = b**2 - 4*a*c
if d < 0:
    check = False
if res:
    if d > 0:
        if (-b - sqrt(d)) / (2*a) < (-b + sqrt(d)) / (a*2):
            print((-b - sqrt(d)) / (a*2),"\n",(-b + sqrt(d)) / (a*2), sep ="")
        else:
            print((-b + sqrt(d)) / (a*2),"\n",(-b - sqrt(d)) / (a*2), sep ="" )
    elif d == 0:
        print( - b /(2* a))
else:
    print('Дискриминант отрицательный')





