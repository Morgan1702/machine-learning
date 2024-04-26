import numpy as np
import matplotlib.pyplot as plt
import re
# Задание 1
#Вариант Y(x)=x * sin(5x), x=[-2...5]
x = np.linspace(-2, 5, 1000)  # вычисление значений x в интервале

y = x * np.sin(5 * x)

plt.plot(x, y)
plt.title('График функции Y(x) = x * sin(5x)')
plt.grid(True)
plt.show()
# Задание 2
with open('text.txt', 'r') as file:
    text = file.read()

frequency = {}
for letter in text:
    if letter.isalpha():
        letter = letter.lower()  # перевод в нижний регистр
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1

# Гистограмма частоты появления букв в тексте
plt.bar(np.array(list(frequency.keys())), np.array(list(frequency.values())), color='skyblue')
plt.xlabel('Буквы')
plt.ylabel('Частота появления')
plt.title('Гистограмма частоты появления букв в тексте')
plt.xticks(rotation=45)  # поворот подписей по оси x на 45 градусов для удобства чтения
plt.grid(axis='y', linestyle='--', alpha=0.7)  # добавление пунктирной сетки по оси y
plt.show()
# Задание 3
with open('text.txt', 'r') as file:
    text = file.read()

ordinary = text.count('.') - text.count('...')
question = text.count('?')
exclamatory = text.count('!')
three_dots = len(re.findall(r'\.\.\.(?!\w)', text))

types = ['Обычные', 'Вопросительные', 'Окличные', 'Триточка']
frequency = [ordinary, question, exclamatory, three_dots]

plt.bar(types, frequency, color='lightgreen')
plt.xlabel('Типи предложения')
plt.ylabel('Частота')
plt.title('Гистограмма частоты появления типов предложений')
plt.grid(axis='y', linestyle='--', alpha=0.7)  # добавление пунктирной сетки по оси y
plt.show()
