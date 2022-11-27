"""1) Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию
 type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
 а указать явно, в программе."""

nomenclature = ['1', 2, 2.45, "string", None, True]
for el in nomenclature:
    print(f"{el} - {type(el)}")

"""2) Для списка реализовать обмен значений соседних элементов, т.е. значениями 
обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве 
элементов последний сохранить на своем месте. Для заполнения списка элементов 
необходимо использовать функцию input()."""

user_list = list(input("Введите значения списка: "))
if len(user_list) % 2 == 0:
    i = 0
    while i < len(user_list):
        el = user_list[i]
        user_list[i] = user_list[i + 1]
        user_list[i + 1] = el
        i += 2
else:
    i = 0
    while i < len(user_list) - 1:
        el = user_list[i]
        user_list[i] = user_list[i + 1]
        user_list[i + 1] = el
        i += 2
print(user_list)

"""3)Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому 
времени года относится месяц (зима, весна, лето, осень). Напишите решения через 
list и через dict."""

calendar = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль",
            "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
month = int(input("Введите месяц от 1 до 12: "))
if month > 0 and month < 13:
    for i in calendar:
        i = month - 1
        print(calendar[i])
        break
else:
    print("Ввели некорректное число!")

calendar_dict = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май",
                 6: "Июнь", 7: "Июль", 8: "Август", 9: "Сентябрь",
                 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
month = int(input("Введите значение от 1 до 12: "))
if month > 0 and month < 13:
    print(calendar_dict.get(month))
else:
    print("Нет месяца под таким номером!")

"""4) Пользователь вводит строку из нескольких слов, разделённых пробелами.
 Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
 Если в слово длинное, выводить только первые 10 букв в слове."""

user_string = input("Введите строку из нескольких слов: ")
str_format = user_string.split(" ")
index = 0
for value in str_format:
    if len(value) > 10:
        value = value[0:10]
    print(index, value)
    index += 1

"""5)Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
 натуральных чисел. У пользователя необходимо запрашивать новый элемент 
 рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то 
 новый элемент с тем же значением должен разместиться после них."""

user_list = [8, 7, 5, 5, 4, 3, 2]
numb = int(input("Введите число: "))
count = user_list.count(numb)
for el in user_list:
    if count > 0:
        i = user_list.index(numb)
        user_list.insert(i+count, numb)
        break
    else:
        if numb > el:
            j = user_list.index(el)
            user_list.insert(j, numb)
            break
        elif numb < user_list[len(user_list) - 1]:
            user_list.append(numb)
print(user_list)

"""6) *Реализовать структуру данных «Товары». Она должна представлять собой
 список кортежей. Каждый кортеж хранит информацию об отдельном товаре. 
 В кортеже должно быть два элемента — номер товара и словарь с параметрами 
 (характеристиками товара: название, цена, количество, единица измерения). 
 Структуру нужно сформировать программно, т.е. запрашивать все данные 
 у пользователя."""

goods = []
while input("Добавить товар? Введите y/n: ") == 'y':
    product = {}
    number = int(input("Введите номер товара: "))
    product_name = input("Введите название товара: ")
    product_price = int(input("Введите цену товара: "))
    product_amount = int(input(("Введите количество товара: ")))
    piece = "шт"
    product["Название"] = product_name
    product["Цена"] = product_price
    product["Количество"] = product_amount
    product["Ед"] = piece
    goods.append(tuple([number, product]))
print(goods)
analitics = {}
for good in goods:
    for key, value in good[1].items():
        if key in analitics:
            analitics[key].append(value)
        else:
            analitics[key] = [value]
print(analitics)
