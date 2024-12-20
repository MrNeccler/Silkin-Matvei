'''Составить программу, в которой функция генерирует четырехзначное число и
определяет, есть ли в числе одинаковые цифры.'''
import random

def generate_four_digit_number():
    # Генерируем четырехзначное число
    number = random.randint(1000, 9999)
    return number

def has_duplicate_digits(number):
    # Преобразуем число в строку и создаем множество для проверки уникальности
    digits = str(number)
    return len(set(digits)) < len(digits)

def main():
    number = generate_four_digit_number()
    print(f"Сгенерированное число: {number}")
    
    if has_duplicate_digits(number):
        print("В числе есть одинаковые цифры.")
    else:
        print("В числе нет одинаковых цифр.")
        
main ()
