'''Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar':
'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого
ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). Чтобы
получить список ключе - использовать метод .keys()
(подсказка: создается новы ключ с цифро в конце,
стары удаляется)'''


a = {'test': 'test_value', 'europe': 'eur', 'dollar':
'usd', 'ruble': 'rub'}
lenght = len(a.keys())
b = a.keys()
i = 0
while i < lenght:
    lenght = str(len(a.keys()))
    b += lenght
    i += 1
print(a)
