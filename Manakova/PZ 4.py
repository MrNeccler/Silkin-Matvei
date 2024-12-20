'''Дано вещественное число X и целое число N (> 0). Найти значение выражения 1 + X
X2/(2!) + ... + XN/(N!) (N! = 12 ...N). Полученное число является приближенным значением функции exp в точке X. '''

def exp(X, N):
    result = 1.0  # Начальное значение для 1
    f = 1.0  # Начальное значение для 0! (факториал)

    for n in range(1, N + 1):
        f *= n  # Вычисляем n! (факториал)
        result += (X ** n) / f  # Добавляем X^n / n! к результату

    return result


# Пример использования
X = float(input("Введите вещественное число X: "))
N = int(input("Введите целое число N (> 0): "))

if N > 0:
    ap = exp(X, N)
    print(f"Приближенное значение exp({X}) с N={N}: {ap}")
else:
    print("N должно быть больше 0.")
