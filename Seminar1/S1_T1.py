# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
#     *Примеры:* 
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет
# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# print (f'{num1}, {num2} -> ', end=' ')

# if num1 ** 2 == num2 or num2 ** 2 == num1:
#     print ('Yes')
# else:
#     print ('No')

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90
num1 = int(input('Enter number1: '))
num2 = int(input('Enter number2: '))
num3 = int(input('Enter number3: '))
num4 = int(input('Enter number4: '))
num5 = int(input('Enter number5: '))

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print ()
