# Создать строку равную введенно строке без последних двух символов.

str = input()
len = len(str)
new_str = str[ :len - 2]
print(new_str)
