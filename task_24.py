# Задача 22   черника растёт на круглой грядке, причём кусты высажены только по окружности. 
# Всего на грядке растёт N кустов.
# На кустах выросло различное число ягод — на i-ом кусте выросло ai ягод.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

n = int(input('Введите количество кустов на грядке: '))
from random import randint
a = [randint(0, 21)for i in range(n)]
print(a)
arr_count = list()
arr_count = [a[i-1] + a[i] + a[i+1] for i in range(n-1)]
arr_count.append(a[-2] + a[-1] + a[0])
print(arr_count)
print(max(arr_count))

# Способ 2
# n = int(input('Введите количество кустов на грядке: '))
# from random import randint
# a = [randint(0, 21)for i in range(n)]
# print(a)
# arr_count = list()
# for i in range(len(a) - 1):
#      arr_count.append(a[i-1] + a[i] + a[i+1])
# arr_count.append(a[-2] + a[-1] + a[0])
# print(arr_count)
# print(max(arr_count))            
