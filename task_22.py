# Задача 22:   Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих 
# наборах.  Пользователь вводит 2 числа.
# n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n,m = int(input('Введите количество элементов множества a: ')), int(input('Введиие количество элементов множества b: ')) 
from random import randint
list1, list2 = [randint(0, 21)for i in range(n)], [randint(0, 21)for i in range(m)]
print(list1, list2)
set1, set2 = set(list1), set(list2)
cros = set1.intersection(set2)
print (sorted(cros))