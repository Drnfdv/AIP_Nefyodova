def unique_digits(number):
    # Преобразуем число в строку
    num_str = str(number)
    # Создаем множество из символов строки
    digits_set = set(num_str)
    # Выводим уникальные цифры и их количество
    print("Уникальные цифры:", ", ".join(digits_set))
    print("Количество уникальных цифр:", len(digits_set))

# Ввод числа от пользователя
number = int(input("Введите целое число: "))

# Вызов функции
unique_digits(number)