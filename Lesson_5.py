"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""
"""С переносом строки"""

with open('new_file.txt', 'a') as file:
    while True:
        user_answ = input('Write smth: ')
        file.write(user_answ + '\n')
        if not user_answ:
            break

"""Без переноса строки"""
with open('new_file.txt', 'a') as file:
    while True:
        user_answ = file.write(input('Write smth: '))
        if not user_answ:
            break

'''Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке. '''


def count_info():
    try:
        with open('new_file.txt', 'r', encoding="utf-8") as file:
            my_list = file.readlines()
            print(f'Количество строк в файле {len(my_list)}')
            for i in range(len(my_list)):
                new_l = my_list[i].split()
                print(f'В {i + 1}-ой строке {len(new_l)} слов(а)')
    except FileNotFoundError:
        return 'Файл не найден.'


count_info()

"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""


def workers_statistics():
    workers = [['Сидоров ', '12000 \n'], ['Кукушкин ', '19000 \n'], ['Иванов ', '145000 \n'], ['Смирнов ', '80000']]
    try:
        with open('new_file.txt', 'r+', encoding="utf-8") as file:
            for i in range(len(workers)):
                file.writelines(workers[i])
            l = file.readlines()
            poor = []
            sum = 0
            for i in range(len(l)):
                salary = int((l[i].split())[1])
                if salary < 20000:
                    poor.append((l[i].split())[0])
                sum += salary
            print(f'Средняя величина дохода сотрудников равна {sum / len(workers) / 12:.2f}')
            print(f'Меньше 20 тыс. рублей получает сотрудник: {", ".join(poor)}')
    except FileNotFoundError:
        return 'Файл не найден.'


workers_statistics()

''' Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''


def rewrite_file():
    num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_text = []
    try:
        with open('file.txt', 'r+', encoding="utf-8") as file:
            l = file.readlines()
            for i in l:
                i = i.split(' ', 1)
                new_text.append(num[i[0]] + ' ' + i[1])
        with open('one_file.txt', 'r+', encoding="utf-8") as new_file:
            new_file.writelines(new_text)
    except FileNotFoundError:
        return 'Файл не найден.'


rewrite_file()

"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def rewrite_file():
    try:
        with open('filsse.txt', 'r+') as file:
            file.write(input('Введите числа через пробел: '))
            l = map(int, file.read().split())
            print(sum(l))
    except FileNotFoundError:
        return 'Файл не найден.'


rewrite_file()

"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
по нему. Вывести словарь на экран."""


def count_subjects():
    try:
        # Информатика: 100(л) 50(пр) 20(лаб).
        mydict = {}
        with open("file.txt", encoding='utf-8') as fobj:
            for line in fobj:
                name, stats = line.split(':')  # name = Информатика, stats = 100(л) 50(пр) 20(лаб).
                name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
                """1. [i for i in stats if i == ' ' or ('0' <= i <= '9')] - Перебирает все элементы и берет только цифры и пробелы(для разделения цифр: [' ', '1', '0', '0', ' ', '5', '0', ' ', '2', 
                 '0']) 

                 2. ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]) с помощью join объединяет 
                 получившееся: _100_50_20  (где _ это пробел) 

                 3. ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split() - делит по пробелам методом .split(): ['100', '50', '20'] 

                 4. map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()) 
                 - с помощью map(int, ['100', '50', '20']) приводит все элементы списка к типу int 

                 5. с помощью sum(['100', '50', '20']) суммирует все элементы списка """
                mydict[name] = name_sum
            print(f"{mydict}")  # вывод:{'Информатика': 170}
    except FileNotFoundError:
        return 'Файл не найден.'


count_subjects()

"""Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
фирме: название, форма собственности, выручка, издержки. Необходимо построчно прочитать файл, вычислить прибыль
каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать. Далее
реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если
фирма получила убытки, также добавить ее в словарь (со значением убытков). """

import json


def get_statistics():
    try:
        with open('file.txt', 'r+', encoding='utf-8') as file:
            statistics = []
            profit = {}
            average_profit = {}
            av = 0
            prof = 0
            i = 3
            for line in file:
                name, firm, earning, damage = line.split()
                total = int(earning) - int(damage)
                if total >= 0:
                    prof = prof + total
                else:
                    i -= 1
                profit[name] = total
            statistics.append(profit)
            if i != 0:
                (av) = prof / i
                average_profit['average_profit'] = round(av)
                statistics.append(average_profit)
            else:
                print('Все компании работают в убыток')
            print(statistics)
        with open('file.json', 'a+', encoding='utf-8') as json_file:
            json.dump(statistics, json_file)
    except FileNotFoundError:
        return 'Файл не найден.'


get_statistics()
