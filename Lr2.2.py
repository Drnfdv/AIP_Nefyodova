def rearrange_negatives(arr):
    # Указатель на позицию, куда нужно поместить следующий отрицательный элемент
    neg_index = 0

    # Проходим по списку
    for i in range(len(arr)):
        if arr[i] < 0:
            # Если текущий элемент отрицательный, меняем его местами с элементом на позиции neg_index
            arr[i], arr[neg_index] = arr[neg_index], arr[i]
            # Сдвигаем указатель neg_index вправо
            neg_index += 1

    return arr


import random

# Генерация случайного списка
random_list = [random.randint(-10, 10) for _ in range(10)]
print("Исходный список:", random_list)

# Применение функции
result = rearrange_negatives(random_list)
print("Преобразованный список:", result)