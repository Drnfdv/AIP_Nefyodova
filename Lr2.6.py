def count_characters(s):
    # Создаем пустой словарь для хранения количества вхождений символов
    char_count = {}

    # Проходим по каждому символу в строке
    for char in s:
        # Если символ уже есть в словаре, увеличиваем его счетчик на 1
        if char in char_count:
            char_count[char] += 1
        # Если символа нет в словаре, добавляем его с начальным значением 1
        else:
            char_count[char] = 1

    return char_count


# Ввод строки с клавиатуры
input_string = input("Введите строку: ")

# Подсчет количества вхождений символов
result = count_characters(input_string)

# Вывод результата
print("Количество вхождений каждого символа:")
for char, count in result.items():
    print(f"'{char}': {count}")