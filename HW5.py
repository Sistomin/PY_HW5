# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А 
# в целую степень B с помощью рекурсии.

# def power(base, exp):
#     if (exp == 1):
#         return (base)
#     if (exp != 1):
#         return (base * power(base, exp - 1))
# base = int(input("Введите число: "))
# exp = int(input("Введите его степень: "))
# print("Результат возведения в степень равен:", power(base, exp))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
 
 
def sum(a, b):
    if b == 0:
        return a
    return sum(a+1, b-1)
 
 
print('Сумма чисел равна ', sum(a, b))