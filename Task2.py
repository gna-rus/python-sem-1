'''
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 
'''
str1 = input("Введите целое положительное число: ")
list1 = list(str1)
sum1 = sum(map(int, list1)) # нахожу сумму цифр
print(f"{str1} -> {sum1} ({list1[0]} + {list1[1]} + {list1[2]})") # Вывод результата на экран
