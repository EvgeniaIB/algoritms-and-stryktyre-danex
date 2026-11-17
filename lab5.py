def task1(n):
    """1. Массив N первых положительных нечетных чисел."""
    arr = []
    for i in range(n):
        arr.append(2 * i + 1)
    return arr

def task2(n, a, d):
    """2. N первых членов геометрической прогрессии."""
    arr = [a]
    for i in range(1, n):
        arr.append(arr[-1] * d)
    return arr

def task3(n, a, b):
    """3. Первый A, второй B, каждый следующий — сумма всех предыдущих."""
    if n == 0:
        return []
    if n == 1:
        return [a]
    arr = [a, b]
    total = a + b
    for i in range(2, n):
        arr.append(total)
        total += arr[-1] 
    return arr

def task4(arr):
    """4. Вывести A1, AN, A2, AN-1, A3, AN-2, ..."""
    result = []
    left, right = 0, len(arr) - 1
    while left <= right:
        if left == right:
            result.append(arr[left])
        else:
            result.append(arr[left])
            result.append(arr[right])
        left += 1
        right -= 1
    return result

def task5(arr):
    """5. Сначала элементы с нечетными номерами (1,3,5...), затем с четными (N, N-2...)."""
    odd = [arr[i] for i in range(0, len(arr), 2)]
    even = [arr[i] for i in range(1, len(arr), 2)]
    even.reverse()
    return odd + even

def task6(arr, k, l):
    """6. Среднее арифметическое элементов с номерами от K до L (1-based)."""
    sub = arr[k-1:l]
    return sum(sub) / len(sub)

def task7(arr):
    """7. Проверить, образуют ли элементы арифметическую прогрессию."""
    if len(arr) < 2:
        return 0
    diff = arr[1] - arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i+1] - arr[i] != diff:
            return 0
    return diff

def task8(arr):
    """8. Минимальный элемент среди элементов с четными номерами (2,4,6...)."""
    even_indices = arr[1::2]
    if not even_indices:
        return None
    return min(even_indices)

def task9(arr):
    """9. Номер последнего локального максимума."""
    last_max_idx = -1
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            last_max_idx = i + 1 
    return last_max_idx

def task10(arr):
    """10. Номера двух одинаковых элементов (в порядке возрастания)."""
    seen = {}
    for i, val in enumerate(arr):
        if val in seen:
            return (seen[val] + 1, i + 1)
        seen[val] = i
    return None


if __name__=="__main__":
    print("ЗАДАЧА 1")
    print(f"N=6 -> {task1(6)}")

    
    print("ЗАДАЧА 2")
    print(f"N=5, A=2, D=3 -> {task2(5, 2, 3)}")

    
    print("ЗАДАЧА 3")
    print(f"N=6, A=1, B=2 -> {task3(6, 1, 2)}")

    
    print("ЗАДАЧА 4")
    print(f"[1,2,3,4,5,6] -> {task4([1,2,3,4,5,6])}")

  
    print("ЗАДАЧА 5")
    print(f"[10,20,30,40,50,60,70] -> {task5([10,20,30,40,50,60,70])}")

    
    print("ЗАДАЧА 6")
    arr6 = [10, 20, 30, 40, 50, 60]
    print(f"Массив {arr6}, K=2, L=4 -> {task6(arr6, 2, 4)}")

    
    print("ЗАДАЧА 7")
    print(f"[2,5,8,11,14] -> разность {task7([2,5,8,11,14])}")
    print(f"[2,5,9,11,14] -> {task7([2,5,9,11,14])}")

   
    print("ЗАДАЧА 8")
    arr8 = [10, 5, 20, 3, 30, 8]
    print(f"Массив {arr8} -> min с четными номерами = {task8(arr8)}")

    
    print("ЗАДАЧА 9")
    arr9 = [1, 3, 2, 5, 1, 4, 2]
    print(f"Массив {arr9} -> номер последнего локального максимума = {task9(arr9)}")

   
    print("ЗАДАЧА 10")
    arr10 = [4, 7, 2, 9, 7, 1]
    print(f"Массив {arr10} -> номера одинаковых элементов = {task10(arr10)}")
   