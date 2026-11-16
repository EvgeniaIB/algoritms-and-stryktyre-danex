def task1(price):
    """1. Стоимость 0.1, 0.2, ..., 1 кг конфет."""
    print(f"Цена 1 кг: {price}")
    weight = 0.1
    while weight <= 1.0001: 
        cost = price * weight
        print(f"{weight:.1f} кг -> {cost:.2f} руб.")
        weight += 0.1
    print()

def task2(n):
    """2. Произведение 1.1 * 1.2 * ... (N сомножителей)."""
    product = 1.0
    for i in range(1, n + 1):
        term = 1 + i * 0.1
        product *= term
    return product

def task3(n):
    """3. Квадрат числа через сумму нечетных чисел, с выводом промежуточных сумм."""
    total = 0
    print(f"N = {n}")
    for i in range(1, n + 1):
        odd = 2 * i - 1
        total += odd
        print(f"Добавляем {odd}, текущая сумма = {total}")
    return total

def task4(a, n):
    """4. Сумма 1 + A + A^2 + ... + A^N."""
    total = 0
    power = 1
    for i in range(n + 1):
        total += power
        power *= a
    return total

def task5(a, n):
    """5. 1 - A + A^2 - A^3 + ... ± A^N (без условного оператора)."""
    total = 0
    power = 1
    sign = 1
    for i in range(n + 1):
        total += sign * power
        power *= a
        sign = -sign 
    return total

def task6(a, b):
    """6. Вывести все целые числа от A до B, каждое число повторяется столько раз, каково его значение."""
    for num in range(a, b + 1):
        for _ in range(num):
            print(num, end=" ")
    print()

def task7(a, b):
    """7. Длина незанятой части отрезка A (без умножения и деления)."""
    remainder = a
    while remainder >= b:
        remainder -= b
    return remainder

def task8(n):
    """8. Наименьшее K, для которого 1+2+...+K >= N, и сама сумма."""
    total = 0
    k = 0
    while total < n:
        k += 1
        total += k
    return k, total

def task9(p):
    """9. Через сколько месяцев вклад превысит 1100 руб. при P% в месяц."""
    s = 1000.0
    months = 0
    while s <= 1100:
        s += s * p / 100
        months += 1
    return months, s

def task10(a, b):
    """10. НОД по алгоритму Евклида."""
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print("ЗАДАЧА 1")
    task1(250.0)

    
    print("ЗАДАЧА 2")
    n = 5
    print(f"N = {n}, произведение = {task2(n)}")

    
    print("ЗАДАЧА 3")
    n = 4
    result = task3(n)
    print(f"Итоговый квадрат: {result} (должно быть {n*n})")

    
    print("ЗАДАЧА 4")
    a, n = 2.0, 3
    print(f"A = {a}, N = {n}, сумма = {task4(a, n)}")

   
    print("ЗАДАЧА 5")
    a, n = 2.0, 3
    print(f"A = {a}, N = {n}, значение = {task5(a, n)}")

    
    print("ЗАДАЧА 6")
    print("A = 2, B = 5")
    task6(2, 5)

    
    print("ЗАДАЧА 7")
    a, b = 10, 3
    print(f"A = {a}, B = {b}, незанятая часть = {task7(a, b)}")

    
    print("ЗАДАЧА 8")
    n = 10
    k, total = task8(n)
    print(f"N = {n}: K = {k}, сумма = {total}")

    
    print("ЗАДАЧА 9")
    p = 5.0
    months, s = task9(p)
    print(f"P = {p}%: месяцев = {months}, итоговый вклад = {s:.2f}")

    
    print("ЗАДАЧА 10")
    a, b = 48, 18
    print(f"A = {a}, B = {b}, НОД = {task10(a, b)}")
    