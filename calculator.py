# почему здесь файл калькулятора?) надо было пул реквест кинуть Олегу)
def calculator(num, num2, operator):
    if operator == '+':
        print('Сложение', num + num2)
    elif operator == '-':
        print('Вычитание', num - num2)
    elif operator == '*':
        print('Умножение', num * num2)
    elif operator == '/':
        print('Деление', num / num2)
    elif operator == '%':
        print('Деление по модулю', num % num2)


while True:  # До : загаловок, а после инструкция

    num = float(input('Введите число: '))
    operator = input('Введите операцию: ')
    num2 = float(input('Введите число: '))
    calculator(num, num2, operator)