#4 даны названия блюд (продуктов), перебрать массив найдя указанное слово ("я не ем"):
# 1) удалить его из списка;2)остановить список на (я ем)

x = ["картофель", "лук", "горох", "свекла", "капуста", "яблоко", "масло"]
print(x)
c = "лук" # input("Я не ем ")
for z in x:
     if z == c:
         continue
     print(z)
a = "горох" # input("Я ем ")
for z in x:
     print(z)
     if z == a:
         break