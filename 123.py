from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def Calculate_Square_Root(number):
    """Вычисляет квадратный корень"""
    return sqrt(number)

def calc(your_number):
    if your_number<=0:
        return    
     
    root = 0
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
           'Это будет: {Calculate_Square_Root(your_number)}')


print(message)
calc (25.5)