def task1(matrix):
    """1. Вывод элементов матрицы по спирали против часовой стрелки, начиная с A[0][0]."""
    if not matrix:
        return []
    m = len(matrix)
    result = []
    top, bottom = 0, m - 1
    left, right = 0, m - 1

    while top <= bottom and left <= right:
        for i in range(top, bottom + 1):
            result.append(matrix[i][left])
        left += 1

        for j in range(left, right + 1):
            result.append(matrix[bottom][j])
        bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][right])
            right -= 1

        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[top][j])
            top += 1

    return result

def task2(matrix, k):
    """2. Сумма и произведение элементов K-й строки (K — 1-based)."""
    row = matrix[k-1]
    total = sum(row)
    product = 1
    for x in row:
        product *= x
    return total, product

def task3(matrix):
    """3. Номер столбца с наименьшим произведением элементов."""
    m = len(matrix)
    n = len(matrix[0])
    min_prod = None
    min_col = 0

    for j in range(n):
        prod = 1
        for i in range(m):
            prod *= matrix[i][j]
        if min_prod is None or prod < min_prod:
            min_prod = prod
            min_col = j

    return min_col + 1, min_prod 

def task4(matrix):
    """4. В каждом столбце количество элементов, больших среднего арифметического этого столбца."""
    m = len(matrix)
    n = len(matrix[0])
    result = []

    for j in range(n):
        col = [matrix[i][j] for i in range(m)]
        avg = sum(col) / m
        count = sum(1 for x in col if x > avg)
        result.append(count)

    return result

def task5(matrix):
    """5. Номер первого столбца, содержащего только нечетные числа (1-based), или 0."""
    m = len(matrix)
    n = len(matrix[0])

    for j in range(n):
        if all(matrix[i][j] % 2 != 0 for i in range(m)):
            return j + 1  
    return 0

def task6(matrix):
    """6. Поменять местами минимальный и максимальный элемент в каждой строке."""
    result = [row[:] for row in matrix] 
    for i, row in enumerate(result):
        min_idx = row.index(min(row))
        max_idx = row.index(max(row))
        row[min_idx], row[max_idx] = row[max_idx], row[min_idx]
    return result

def task7(matrix):
    """7. Поменять местами столбцы, содержащие минимальный и максимальный элементы матрицы."""
    m = len(matrix)
    n = len(matrix[0])
    min_val, max_val = float('inf'), float('-inf')
    min_col = max_col = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                min_col = j
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_col = j

    result = [row[:] for row in matrix]
    for i in range(m):
        result[i][min_col], result[i][max_col] = result[i][max_col], result[i][min_col]
    return result

def task8(matrix):
    """8. Поменять местами левую верхнюю и правую нижнюю четверти (M и N — четные)."""
    m = len(matrix)
    n = len(matrix[0])
    half_m = m // 2
    half_n = n // 2
    result = [row[:] for row in matrix]

    for i in range(half_m):
        for j in range(half_n):
            result[i][j], result[i + half_m][j + half_n] = \
                result[i + half_m][j + half_n], result[i][j]

    return result

def task9(matrix):
    """9. Упорядочить строки по возрастанию их первых элементов."""
    return sorted(matrix, key=lambda row: row[0])

def task10(matrix):
    """10. Сумма элементов каждой диагонали, параллельной главной."""
    m = len(matrix)
    n = len(matrix[0])
    sums = {}
    for i in range(m):
        for j in range(n):
            key = i - j
            sums[key] = sums.get(key, 0) + matrix[i][j]


    return [sums[k] for k in sorted(sums.keys())]


if __name__ == "__main__":
    print("ЗАДАЧА 1: Спираль против часовой стрелки")
    mat1 = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9,  10, 11, 12],
        [13, 14, 15, 16]
    ]
    print("Матрица:")
    for row in mat1: print(row)
    print("Спираль:", task1(mat1))

    print("ЗАДАЧА 2: Сумма и произведение K-й строки")
    mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Матрица {mat2}, K=2 -> сумма, произведение: {task2(mat2, 2)}")

    print("ЗАДАЧА 3: Столбец с наименьшим произведением")
    mat3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Матрица {mat3} -> (номер, произведение): {task3(mat3)}")

    print("ЗАДАЧА 4: Количество элементов больше среднего в каждом столбце")
    mat4 = [[1, 2], [3, 4], [5, 6]]
    print(f"Матрица {mat4} -> {task4(mat4)}")

    print("ЗАДАЧА 5: Первый столбец только с нечетными числами")
    mat5 = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
    print(f"Матрица {mat5} -> номер столбца: {task5(mat5)}")

    print("ЗАДАЧА 6: Поменять min и max в каждой строке")
    mat6 = [[3, 1, 2], [9, 7, 8], [6, 4, 5]]
    print("До:   ", mat6)
    print("После:", task6(mat6))

    print("ЗАДАЧА 7: Поменять столбцы с min и max элементами")
    mat7 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("До:   ", mat7)
    print("После:", task7(mat7))

    print("ЗАДАЧА 8: Поменять четверти")
    mat8 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print("До:   ", mat8)
    print("После:", task8(mat8))

    print("ЗАДАЧА 9: Сортировка строк по первому элементу")
    mat9 = [[3, 9], [1, 8], [2, 7]]
    print("До:   ", mat9)
    print("После:", task9(mat9))

    print("ЗАДАЧА 10: Суммы диагоналей, параллельных главной")
    mat10 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Матрица:")
    for row in mat10: print(row)
    print("Суммы диагоналей:", task10(mat10))