'''Описать функцию PowerA234(A, B, C, D), вычисляющую вторую, третью и
четвертую степень числа A и возвращающую эти степени соответственно в
переменные B, C и D (A — входной, B, C, D — выходные параметры; все параметры
являются вещественными). С помощью этой функции найти вторую, третью и
четвертую степень пяти данных чисел'''

def PowerA234(A):
    # Вычисляем степени
    B = A ** 2  # Вторая степень
    C = A ** 3  # Третья степень
    D = A ** 4  # Четвертая степень
    return B, C, D


# Задаем пять чисел
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

# Проходим по каждому числу и вычисляем степени
for number in numbers:
    B, C, D = PowerA234(number)
    print(f"Число: {number}, Вторая степень: {B}, Третья степень: {C}, Четвертая степень: {D}")