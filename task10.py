# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

from random import randint

print("Вариант 1:")
money = [randint(0,1) for _ in range(int(input("Введите количество монет ")))]
avers_revers = [0,0]
for i in money:
    if i == 0: avers_revers[0] += 1
    else: avers_revers[-1] += 1
print(*money)
print(f'Минимальное количество монет, которые нужно перевернуть: {min(avers_revers)}') 


#####################################################
# 2 ВАРИАНТ
# from random import randint
print("Вариант 2:")
avers_revers = [0,0]
for _ in range(int(input("Введите количество монет "))):
    x = randint(0,1)
    if x == 0: avers_revers[0] += 1
    else: avers_revers[-1] += 1
    print(x, end=' ')
print(f'\nМинимальное количество монет, которые нужно перевернуть: {min(avers_revers)}')     

