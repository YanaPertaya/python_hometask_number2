# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

# Например:
# Input:
# 10
# Output:
# 1 2 4 8

n = int(input("Введите натуральное число N: "))
double = 2
index = 1
while (2 ** index) <= n:
        print(2 ** index)
        index += 1