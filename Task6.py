'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
'''

NumOfTicket = input()
FirstPartOfTicket = sum(map(int, NumOfTicket[:3])) # определяю сумму 1 половины через map и sum
SecondPartOfTicket = sum(map(int, NumOfTicket[3:])) # определяю сумму второй половины номера через map и sum
print(f"{NumOfTicket} ->", "yes" if FirstPartOfTicket == SecondPartOfTicket else "no") # вывожу результат через f-строку
