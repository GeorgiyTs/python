print("Здание №1")
my_list = [23, "text", 24.00]
print(type(my_list[0]))

print("Здание №2")
spisok = [input("Введите список: ")]

print(spisok.insert(1, 2)) #Я опять не понял, как выполнить вторую задачу...

print("Здание №3.1")
mec_num = int(input("Введите № месяца: "))
if 0 < mec_num < 13: #добавляю if для выдачи 2-х результатов
    my_list_m = ["Янаврь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Окрябрь", "Ноябрь", "Декабрь"]
    print(my_list_m[mec_num - 1]) #вопрос: Почему я написал mec_num - 1, а он считает как +?
else:
    print("ERROR")
print("Здание №3.2")
num_mec = int(input("Введите № месяца: "))
if 0 < num_mec <13:
    my_dict_m = {1:"Янаврь", 2:"Февраль", 3:"Март", 4:"Апрель", 5:"Май", 6:"Июнь", 7:"Июль", 8:"Август", 9:"Сентябрь", 10:"Окрябрь", 11:"Ноябрь", 12:"Декабрь"}
    print(my_dict_m.get(num_mec))
else:
    print("ERROR")

print("Здание №4")
stroka = "строка из какого-то большого текста"
for num, el in enumerate(stroka.split(), 1):  #подглядел в 3-м уроке и исправил свой код
    print(num, el)

print("Задание №5")
my_list = [7, 5, 3, 3, 2]
new_num = 5
indx = 0
for item in my_list:
     if new_num <= item:
         indx = my_list.index(item) + 1  #+1, чтобы добавлялось после!
my_list.insert(indx, new_num)
print(my_list)