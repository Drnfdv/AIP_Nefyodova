input_string = input("Введите последовательность чисел через пробел: ")

# Разделяем строку на числа
numbers = input_string.split()

# Множество для хранения уникальных чисел
seen_numbers = set()

# Проходим по каждому числу
for number in numbers:
    if number in seen_numbers:
        print("YES")
    else:
        print("NO")
        # Добавляем число в множество
        seen_numbers.add(number)