def task1_factorial(n):
    """1. Рекурсивное вычисление факториала."""
    if n <= 1:
        return 1
    return n * task1_factorial(n - 1)

def task2_fibonacci(n):
    """2. Рекурсивное вычисление n-го числа Фибоначчи."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return task2_fibonacci(n - 1) + task2_fibonacci(n - 2)

def task3_power(x, n):
    """3. Рекурсивное возведение числа x в степень n."""
    if n == 0:
        return 1
    if n < 0:
        return 1 / task3_power(x, -n)
    if n % 2 == 0:
        half = task3_power(x, n // 2)
        return half * half
    else:
        return x * task3_power(x, n - 1)

def task4_palindrome(s):
    """4. Рекурсивная проверка строки на палиндром."""
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return task4_palindrome(s[1:-1])

def task5_binary_search(arr, target, left=0, right=None):
    """5. Рекурсивный бинарный поиск в отсортированном массиве."""
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1 
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return task5_binary_search(arr, target, mid + 1, right)
    else:
        return task5_binary_search(arr, target, left, mid - 1)

def task6_reverse_words(s):
    """6. Рекурсивный обратный порядок слов в строке."""
    words = s.split()
    if len(words) <= 1:
        return s
    return task6_reverse_words(" ".join(words[1:])) + " " + words[0]

def task7_prime_sum(n):
    """7. Рекурсивное разложение числа на сумму простых чисел."""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def helper(remaining, current_primes):
        if remaining == 0:
            return current_primes
        for p in range(remaining, 1, -1):
            if is_prime(p):
                result = helper(remaining - p, current_primes + [p])
                if result is not None:
                    return result
        return None

    return helper(n, [])

def task8_count_digits(n):
    """8. Рекурсивный подсчет количества цифр в числе."""
    n = abs(n) 
    if n < 10:
        return 1
    return 1 + task8_count_digits(n // 10)

def task9_hanoi(n, source, target, auxiliary):
    """9. Рекурсивное решение головоломки «Ханойская башня»."""
    if n == 0:
        return
    task9_hanoi(n - 1, source, auxiliary, target)
    print(f"Переместить диск {n} с {source} на {target}")
    task9_hanoi(n - 1, auxiliary, target, source)


if __name__ == "__main__":
    print("ЗАДАЧА 1: Факториал")
    print(f"5! = {task1_factorial(5)}")

   
    print("ЗАДАЧА 2: Числа Фибоначчи")
    print(f"F(10) = {task2_fibonacci(10)}")

   
    print("ЗАДАЧА 3: Возведение в степень")
    print(f"2^10 = {task3_power(2, 10)}")
    print(f"2^-3 = {task3_power(2, -3)}")

   
    print("ЗАДАЧА 4: Палиндром")
    print(f"'А роза упала на лапу Азора' -> {task4_palindrome('А роза упала на лапу Азора')}")
    print(f"'Привет' -> {task4_palindrome('Привет')}")

   
    print("ЗАДАЧА 5: Бинарный поиск")
    arr = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    print(f"Массив: {arr}, ищем {target} -> индекс {task5_binary_search(arr, target)}")

 
    print("ЗАДАЧА 6: Обратный порядок слов")
    print(f"'Привет мир как дела' -> '{task6_reverse_words('Привет мир как дела')}'")

    
    print("ЗАДАЧА 7: Разложение на сумму простых чисел")
    n = 10
    print(f"{n} = {' + '.join(map(str, task7_prime_sum(n)))}")

  
    print("ЗАДАЧА 8: Подсчет цифр в числе")
    print(f"Количество цифр в 12345 -> {task8_count_digits(12345)}")

  
    print("ЗАДАЧА 9: Ханойская башня")
    print("Перемещение 3 дисков:")
    task9_hanoi(3, 'A', 'C', 'B')
    
