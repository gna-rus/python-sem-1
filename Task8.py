'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
'''

n, m, k = int(input()), int(input()), int(input()) # ввод размеровв шоколадки и дольки
rez = "no"
for i in range(n*m+1): # цикл, для провдения дробления шоколадки и поиска сопоставления рпзмерам дольки (k)
    if (n*i == k) or (m*i == k):
        rez = " yes"
print(f"{n} {m} {k} -> {rez}")




