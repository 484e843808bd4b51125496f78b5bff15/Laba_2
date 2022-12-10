from colorama import Fore
from loguru import logger

U = "qwertyuiopasdfghjklzxcvbnm"
a = set(input(Fore.RED + 'Введіть множину A !!!\n'))
count = 0
for j in a:
    for r in U:
        if j == r:
            count += 1
if len(a) != count:
    logger.debug("Error.[Помилка введення 120993]. Записати в множину тільки літери англ. алфавіту!!!\n")
    a = set(input(Fore.BLUE + "Введіть множину A, ще раз!!!\n"))

b = set(input('Введіть множину B !!!\n'))
count = 0
for j in b:
    for r in U:
        if j == r:
            count += 1
if len(b) != count:
    logger.debug('Error.[Помилка введення 120993]. Записати в множину тільки літери англ. алфавіту!!!\n')
    b = set(input(Fore.LIGHTWHITE_EX + 'Введіть множину B, ще раз!!!\n'))

c = set(input('Введіть множину C !!!\n'))
count = 0
for j in c:
    for r in U:
        if j == r:
            count += 1
if len(c) != count:
    logger.debug('Error.[Помилка введення 120993]. Записати в множину тільки літери англ. алфавіту!!!\n')
    c = set(input(Fore.MAGENTA + 'Введіть множину C, ще раз!!!\n'))

print('\n')
print(Fore.BLUE + 'A = ', a, ' Довжина = ', [len(a)])
print(Fore.BLUE + 'B = ', b, ' Довжина = ', [len(b)])
print('C = ', c, ' Довжина = ', [len(c)])
print('\n')

menu = ["Вирішити даний вираз (1)", "Завершити (0)"]
for m in menu:
    print(Fore.LIGHTYELLOW_EX + m)

while True:
    i = int(input('\nОбери операцію над множинами [1/0] !!!\n'))
    if i == 1:
        s = a - b
        x = c - b - a
        print('А/B = ', s)
        print('C/B/А = ', x)
        end = s.intersection(x)
        if len(end) == 0:
            logger.debug('Вираз = порожній множині !')
        else:
            print(end)
    elif i == 0:
        print('Операції виконано успішно !')
        break
    if i > 2:
        logger.debug('Помилка введення !!!')
