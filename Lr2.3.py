from collections import Counter
def count_pairs(lst):
    # Считаем частоты каждого элемента в списке
    frequency = Counter(lst)
    # Считаем количество пар
    pairs_count = 0
    for count in frequency.values():
        pairs_count += count // 2  # Каждые два одинаковых элемента образуют одну пару
    return pairs_count

# Пример использования
lst = [1, -1, 2, 3, -5, 1, 2, -8, -9, 2]
result = count_pairs(lst)
print(result)