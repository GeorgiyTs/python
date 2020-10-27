print("Задание №1")
a = input("Введите число:")
s = input("Введите слово:")
print("Ваше число: " + a)
print("Ваше слово: " + s)

print("Задание №2")

print("Задание №3")
n = int(input("Введите число n:"))
print(n * 123)  #n + nn + nnn

print("Задание №4")
aaa = input("Введите число:")
print (max(aaa))

print("Задание №5")
vir = int(input("Введите значение выручки: "))
izd = int(input("Введите значение издержек: "))
if vir > izd:
    print("Ваша компания работает в плюс! Примите мои поздравления!")
    prib = int(vir - izd)
    rent = str(prib / vir)
    print("Рентабельность вашей компании: " + rent)
    sotr = int(input("Введите число сотрудников вашей компании: "))
    prib_sotr = str(prib / sotr)
    print("Каджый сотрудник в среднем приносит вам " + prib_sotr + " рублей!")
elif vir == izd:
    print("Ваша компания работает в ноль!")
else:
    print("Ваша компания несет убытки!")

print("Задание №6")
zha = int(input("Введите значине а: "))
zhb = int(input("Введите значине b: "))
civ = int(0)
while zha < zhb:
    zha = str(zha * 1.1)
    civ = int(civ)
    civ = str(civ + 1)
    print(civ + "-й день: " + zha)
    zha = float(zha)