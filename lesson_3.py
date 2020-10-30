
print("Задание №1")

var_one = int(input("Введите первое число: "))
var_two = int(input("Введите второе число: "))

def div(var_one, var_two) :
    if var_two == 0:
        return print("ERROR")
    else:
        return (var_one / var_two)

print(div(var_one, var_two))

print("Задание №2")

name = "Alex"
secname = "Ivanov"
city = "Moscow"
age = 1967
email = "ivanov67@gmail.ru"
phone = 89957365130

def data(name, secname, city, age, email, phone):
    return name, secname, city, age, email, phone

print(data(name, secname, city, age, email, phone))

print("Задание №3")

def my_func(arg_one , arg_two, arg_three):
    if arg_one >= arg_three and arg_two >= arg_three:
        return arg_one + arg_two
    elif arg_one > arg_two and arg_one < arg_three:
        return arg_one + arg_three
    else:
        return arg_two + arg_three

print(f'Результат - {my_func(int(input("Введите первый аргумент: ")), int(input("Введите второй аргумент: ")), int(input("Введите третий аргумент: ")))}')

print("Задание №4")

def my_func(x, y):
    if y == 0:
        return 1
    return x * my_func(x, y + 1)

print(my_func(2, -2))

print("Задача №5")

def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input("Введите число или R для выхода: ").split()

        res = 0
        for el in range(len(number)):
            if number[el] == "r" or number[el] == "R":
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f"Текущая сумма {sum_res}")
    print(f"Ваша итоговая сумма {sum_res}")


my_sum()

print("Задача №6")

def int_func(text):
    result = ""
    for word in text.split():
        result += word[0].upper() + word[1:]

    return result

print(int_func("text"))



