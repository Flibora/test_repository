'''Ввести строку. Вывести на экран букву, которая
находится в середине это строки.
Также, если эта центральная буква равна перво букве
в строке, то создать и вывести часть строки между
первым и последним символами исходно строки.
(подсказка: для получения центрально буквы,
на дите длину строки и разделите ее пополам; для
создания результирующи строки использу те срез)'''


stroka = input()

a = len(stroka) // 2
b = stroka[a]
print(b)
if b == stroka[0]:
    print(stroka[1: -1])
