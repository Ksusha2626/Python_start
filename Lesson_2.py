"""Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента."""

type_list = ['cat', 1, (2,), [1, 2], 3.1, False, frozenset('1'), set('1')]
for el in type_list:
    print(type(el))

"""Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте."""

my_list = list(input('Введите значения: ').split())
new_list = []
for i in range(0, len(my_list), 2):
    next_i = i + 2
    a = my_list[i:next_i]
    a.reverse()
    new_list.extend(a)
print(new_list)

"""Вариант 2"""

my_list = list(input('Введите значения: ').split())
for i in range(1, len(my_list), 2):
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
print(my_list)


"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень)."""

season = {
    'Winter': [12, 1, 2],
    'Spring': [3, 4, 5],
    'Summer': [6, 7, 8],
    'Autumn': [9, 10, 11]
}
month = int(input('Введите номер месяца'))
for key, value in season.items():
    if month in value:
        print(key)
        break
else:
    print('Not a month')

"""Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное, выводить только первые 10 букв в слове."""

my_list = input('Введите значения: ').split()

for i, el in enumerate(my_list, 1):
    print(i, el[0:10])

"""Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге есть элементы с одинаковыми значениями, то новый элемент с тем же значением размещется после них."""

my_list = [7, 5, 3, 3, 1]

a = False
while not a:
    try:
        new_score = int(input('New score is: '))
        if new_score < 0:
            print('Должно быть положительное число')
            continue
        if new_score > max(my_list):
            my_list.insert(0, new_score)
            break
        if new_score < min(my_list):
            my_list.append(new_score)
            break
        for i, el in enumerate(my_list):
            if my_list[-1] == new_score:
                my_list.append(new_score)
                a = True
                break
            if el == new_score and el != my_list[i + 1]:
                my_list.insert(i + 1, new_score)
                a = True
                break
    except ValueError:
        print('Должно быть положительное число')

print(f'Измененный список {my_list}')

"""Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
с параметрами (характеристиками товара: название, цена, количество, единица измерения)."""

"""Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров."""

goods = []
analytics = {'name': [],
             'price': [],
             'quantity': [],
             'unit': []}
num = 1
while True:
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    unit = input('Введите единицу измерения товара: ')
    params = {
        'name': name,
        'price': price,
        'quantity': quantity,
        'unit': unit
    }
    good = (num, params)
    goods.append(good)

    for key, value in params.items():
        i = analytics.get(key)
        if value in i:
            continue
        i.append(value)
        continue

    num += 1
    exit_answer = input('Ввести еще позицию? ').lower()
    if exit_answer == 'нет':
        break
print(analytics)
