#  Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

num = input('Введите число: ')
if '.' in num:
    index_num = num.find('.')+1
    print(num[index_num])
elif ',' in num:
    index_num = num.find(',')+1
    print(num[index_num])
else:
    print('No')

