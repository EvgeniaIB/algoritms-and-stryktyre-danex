import math

def task1(a, b):
    """1. Площадь и периметр прямоугольника"""
    s = a * b
    p = 2 * (a + b)
    return s, p

def task2(d):
    """2. Длина окружности (pi = 3.14)"""
    pi = 3.14
    l = pi * d
    return l

def task3(a, b):
    """3. Среднее арифметическое"""
    return (a + b) / 2

def task4(a, b):
    """4. Сумма, разность, произведение и частное квадратов (числа ненулевые)"""
    a2 = a ** 2
    b2 = b ** 2
    return a2 + b2, a2 - b2, a2 * b2, a2 / b2

def task5(a, b):
    """5. Сумма, разность, произведение и частное модулей (числа ненулевые)"""
    abs_a = abs(a)
    abs_b = abs(b)
    return abs_a + abs_b, abs_a - abs_b, abs_a * abs_b, abs_a / abs_b

def task6(x1, y1, x2, y2):
    """6. Расстояние между двумя точками"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def task7(a, b, c):
    """7. Длины отрезков AC, BC и их сумма (точки на числовой оси)"""
    ac = abs(c - a)
    bc = abs(c - b)
    return ac, bc, ac + bc

def task8(a, b, c):
    """8. Произведение длин AC и BC (C между A и B)"""
    ac = abs(c - a)
    bc = abs(c - b)
    return ac * bc

def task9(x1, y1, x2, y2):
    """9. Периметр и площадь прямоугольника по двум противоположным вершинам"""
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    p = 2 * (width + height)
    s = width * height
    return p, s

def task10(x1, y1, x2, y2, x3, y3):
    """10. Периметр и площадь треугольника по координатам вершин"""
    # Длины сторон
    a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    p = a + b + c
    # Площадь по формуле Герона
    p_half = p / 2
    s = math.sqrt(p_half * (p_half - a) * (p_half - b) * (p_half - c))
    return p, s

def task11(x):
    """11. y = 3x^6 - 6x^2 - 7"""
    y = 3 * (x ** 6) - 6 * (x ** 2) - 7
    return y

def task12(x):
    """12. y = 4(x-3)^6 - 7(x-3)^3 + 2"""
    t = x - 3
    y = 4 * (t ** 6) - 7 * (t ** 3) + 2
    return y

import math


if __name__ == "__main__":
    print("ЗАДАЧА 1: Площадь и периметр прямоугольника")
    a, b = 5, 3
    s, p = task1(a, b)
    print(f"Стороны: a={a}, b={b}")
    print(f"Площадь S = {s}")
    print(f"Периметр P = {p}")
    print()

    print("ЗАДАЧА 2: Длина окружности")
    d = 10
    l = task2(d)
    print(f"Диаметр d = {d}")
    print(f"Длина окружности L = {l}")
    print()

    print("ЗАДАЧА 3: Среднее арифметическое")
    a, b = 7, 13
    avg = task3(a, b)
    print(f"Числа: a={a}, b={b}")
    print(f"Среднее арифметическое = {avg}")
    print()

    print("ЗАДАЧА 4: Операции с квадратами")
    a, b = 4, 2
    sum_sq, diff_sq, prod_sq, quot_sq = task4(a, b)
    print(f"Числа: a={a}, b={b}")
    print(f"Сумма квадратов: {sum_sq}")
    print(f"Разность квадратов: {diff_sq}")
    print(f"Произведение квадратов: {prod_sq}")
    print(f"Частное квадратов: {quot_sq}")
    print()

    print("ЗАДАЧА 5: Операции с модулями")
    a, b = -6, 3
    sum_abs, diff_abs, prod_abs, quot_abs = task5(a, b)
    print(f"Числа: a={a}, b={b}")
    print(f"Сумма модулей: {sum_abs}")
    print(f"Разность модулей: {diff_abs}")
    print(f"Произведение модулей: {prod_abs}")
    print(f"Частное модулей: {quot_abs}")
    print()

    print("ЗАДАЧА 6: Расстояние между точками")
    x1, y1 = 1, 2
    x2, y2 = 4, 6
    dist = task6(x1, y1, x2, y2)
    print(f"Точка 1: ({x1}, {y1})")
    print(f"Точка 2: ({x2}, {y2})")
    print(f"Расстояние = {dist}")
    print()

    print("ЗАДАЧА 7: Отрезки на числовой оси")
    a, b, c = 1, 10, 4
    ac, bc, total = task7(a, b, c)
    print(f"Точки: A={a}, B={b}, C={c}")
    print(f"Длина AC = {ac}")
    print(f"Длина BC = {bc}")
    print(f"Сумма AC + BC = {total}")
    print()

    print("ЗАДАЧА 8: Произведение длин AC и BC")
    a, b, c = 2, 8, 5
    prod = task8(a, b, c)
    print(f"Точки: A={a}, B={b}, C={c} (C между A и B)")
    print(f"Произведение AC * BC = {prod}")
    print()

    print("ЗАДАЧА 9: Прямоугольник по двум вершинам")
    x1, y1 = 1, 2
    x2, y2 = 5, 7
    p, s = task9(x1, y1, x2, y2)
    print(f"Вершина 1: ({x1}, {y1})")
    print(f"Вершина 2: ({x2}, {y2})")
    print(f"Периметр = {p}")
    print(f"Площадь = {s}")
    print()

    print("ЗАДАЧА 10: Треугольник по трём вершинам")
    x1, y1 = 0, 0
    x2, y2 = 4, 0
    x3, y3 = 0, 3
    p, s = task10(x1, y1, x2, y2, x3, y3)
    print(f"Вершины: ({x1}, {y1}), ({x2}, {y2}), ({x3}, {y3})")
    print(f"Периметр = {p}")
    print(f"Площадь = {s}")
    print()

    print("ЗАДАЧА 11: y = 3x^6 - 6x^2 - 7")
    x = 2
    y = task11(x)
    print(f"x = {x}")
    print(f"y = {y}")
    print()

    print("ЗАДАЧА 12: y = 4(x-3)^6 - 7(x-3)^3 + 2")
    x = 4
    y = task12(x)
    print(f"x = {x}")
    print(f"y = {y}")

    
