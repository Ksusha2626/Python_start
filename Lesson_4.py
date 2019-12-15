""" Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения необходимо запускать скрипт с параметрами."""
from sys import argv


def my_func_1():
    try:
        num = [int(_) for _ in argv[1:]]
        return (num[0] * num[1]) + num[2]
    except ValueError:
        print('Вы ввели недопустимое значение')
    except IndexError:
        print('Вы ввели недостаточное количество параметров')


print(my_func_1())

""" Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента."""


def my_func_2():
    user_answer = input().split()
    num = [int(_) for _ in user_answer]
    return [a for i, a in enumerate(num) if a > num[i - 1]]


print(my_func_2())

"""Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку."""


def my_func_3():
    return [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]


print(my_func_3())

"""Определить элементы списка, не имеющие повторений. """
my_list = [10, 10, 4, 6, 6, 9, 8]
res = [i for i in my_list if my_list.count(i) == 1]
print(res)

"""Реализовать формирование списка. В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка."""

'''1 вариант'''

from functools import reduce

my_list = [_ for _ in range(1, 7) if _ % 2 == 0]
print(reduce(lambda x, y: x * y, my_list))

'''2 вариант'''

el = 1
for i in my_list:
    el *= i
print(el)

"""
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Усложнение* : Объединить циклы и сделать их НЕ бесконечными. """

from itertools import count, cycle


def my_func():
    l = []
    ex = 0
    for el in count(5):
        if el > 10:
            break
        l.append(el)
    for i in cycle(l):
        if ex > 20:
            break
        ex += 1
        print(i)


my_func()

"""Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. 
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел."""


def fibo_gen():
    x = 1
    for el in range(2, 20):
        x *= el
    yield x


for el in fibo_gen():
    print(str(el)[:15])