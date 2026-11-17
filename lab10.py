def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    steps = 0

    print(f"Ищем число {target} в массиве: {arr}")

    while left <= right:
        steps += 1
        mid = (left + right) // 2
        print(f"Шаг {steps}: проверяем элемент по индексу {mid} (значение: {arr[mid]})")

        if arr[mid] == target:
            print(f" Элемент {target} НАЙДЕН на индексе {mid} (за {steps} шагов).")
            return mid
        elif arr[mid] > target:
            print(f"   {arr[mid]} > {target}, ищем в левой половине.")
            right = mid - 1
        else:
            print(f"   {arr[mid]} < {target}, ищем в правой половине.")
            left = mid + 1

    print(f" Элемент {target} НЕ НАЙДЕН в массиве (потребовалось {steps} шагов).")
    return -1


# --- Проверка ---
if __name__ == "__main__":
    # Отсортированный массив (обязательное условие для бинарного поиска)
    sorted_array = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]

    print("-" * 50)
    # 1. Ищем существующий элемент
    binary_search(sorted_array, 36)
    
    print("-" * 50)
    # 2. Ищем несуществующий элемент
    binary_search(sorted_array, 100)
    
    print("-" * 50)
    # 3. Ищем первый элемент
    binary_search(sorted_array, 2)