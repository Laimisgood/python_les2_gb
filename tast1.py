# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть. С клавиатуры вводятся число монет и сами монеты построчно.
# Пример:
# Ввод: 1 1 1 1 0 0 -> 2 

coins = input().split()
n = len(coins)
heads = coins.count('1')
tails = n - heads

if heads == tails:
    print(0)
else:
    min_flips = min(heads, tails)
    print(min_flips)