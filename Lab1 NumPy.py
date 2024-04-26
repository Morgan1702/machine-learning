import numpy as np
#Задание 1
print('Выполнение задания:')

array1 = np.array([1, 2, 3, 4, 5, 6])
array2 = np.array([7, 8, 9, 10, 11, 12])

# Арифметические операции
addition = array1 + array2
print(f'Сложение: {addition}')

subtraction = array1 - array2
print(f'Вычитание: {subtraction}')

multiplication = array1 * array2
print(f'Умножение: {multiplication}')

division = array1 / array2
print(f'Деление: {division}')

# Метод конкатенации
concatenated_array = np.concatenate([array1, array2])
print(f'Результат конкатенации: {concatenated_array}')

# Максимальный и минимальный элементы, сумма и произведение
max_element = np.max(concatenated_array)
print(f'Максимальный элемент: {max_element}')

min_element = np.min(concatenated_array)
print(f'Минимальный элемент: {min_element}')

sum_elements = np.sum(concatenated_array)
print(f'Сумма элементов: {sum_elements}')

product_elements = np.prod(concatenated_array)
print(f'Произведение элементов: {product_elements}')
#Задание 2
print('Выполнение задания 2:')

array1 = np.array([5, 4, 1, 67, 32, 6, 16, 11, 9, 10, 9, 3, 13, 2, 15])

# Вычисление среднего значения и изменение каждого элемента массива на среднее значение
mean_value = np.mean(array1)
adjusted_array = array1 - mean_value
print(f'Массив с коррекцией: {adjusted_array}')

# Сортировка скорректированного массива по возрастанию
sorted_array = np.sort(adjusted_array)
print(f'Отсортированный массив по возрастанию: {sorted_array}')
#Задание 3
print('Выполнение задания 3:')

# Инициализация одномерного массива с 20 элементами с использованием функции random()
rand_array = np.random.rand(20)
print(f'Одномерный массив: {rand_array}')

# Преобразование одномерного массива в двумерный массив размером 4x5
two_dimensional_array = rand_array.reshape(4, 5)

# Увеличение каждого элемента двумерного массива на 10
two_dimensional_array += 10
print(f'Двумерный массив с увеличенными элементами: \n{two_dimensional_array}')
#Задание 4
print('Выполнение задания 4:')

# Создание двумерного массива целых чисел в диапазоне от -15 до 15
array1 = np.random.randint(-15, 16, (3, 5))
print(f'Исходный массив: \n{array1}')

# Замена отрицательных чисел на -1 и положительных на 1
array1[array1 < 0] = -1
array1[array1 > 0] = 1

print(f'Массив после замены: \n{array1}')
#Задание 5
print('Выполнение задания 5:')

# Инициализация матриц A и B
A = np.array([[2, 3, -1], [4, 5, 2], [-1, 0, 7]])
B = np.array([[-1, 0, 5], [0, 1, 3], [2, -2, 4]])

# Выполнение операций над матрицами
result = 2 * (A + B) * (2 * B - A)

print(f'Результат операций:\n {result}')
#Задание 6
print('Выполнение задания 6:')

# Матрица с левой частью уравнений
A = np.array([[1, 1, 2, 3],
              [3, -1, -2, -2],
              [2, -3, -1, -1],
              [1, 2, 3, -1]])

B = np.array([1, -4, -6, -4])  # Правая часть уравнений

# Решение системы линейных уравнений
solution = np.linalg.solve(A, B)

print(f'Решение системы уравнений: {solution}')
