"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = '0'
while int(n) <= 0:
    n = input('Введите число n: ')
# sum = int(n) + int(n + n) + int(n + n + n)
print(f'{n} + {n+n} + {n+n+n} = {int(n) + int(n + n) + int(n + n + n)}')