import numpy as np
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