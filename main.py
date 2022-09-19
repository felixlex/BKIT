import sys
import math


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt, end = '')
        coef_str = input()
    try:
        return float(coef_str)
    except:
        pass
    while(True):
        try:
            print("Введен неверный аргумент")
            print("Введите заново: ", end="")
            coef_str = input()
            float(coef_str)
            break
        except:
            pass
    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''

    if a==0 and b==0:
        return []
    if a == 0:
        return [-c/b]
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        if root1 >= 0:
            if root1 == 0:
                root1 = 0
            else:
                root12=root1
                root1 = math.sqrt(root1)
                root12 = math.sqrt(root12) * (-1)
                result.append(root12)
            result.append(root1)

        root2 = (-b - sqD) / (2.0 * a)
        if root2 >= 0:
            if root2 == 0:
                root2 = 0
            else:
                root22=root2
                root2 = math.sqrt(root2)
                root22 = math.sqrt(root22) * (-1)
                result.append(root22)
            result.append(root2)
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А: ')
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')
    print(a, "x^4 + (", b, ")x^2 + ",c)
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {} и {} , {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4