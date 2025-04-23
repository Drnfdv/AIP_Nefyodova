def floyd_warshall(graph):  #стек
    # Получаем количество вершин в графе
    n = len(graph)

    # Создаем матрицу расстояний размером n x n, заполненную бесконечностями
    dist = [[float('inf')] * n for _ in range(n)]

    # Заполняем диагональ нулями (расстояние от вершины до самой себя равно 0)
    for i in range(n):
        dist[i][i] = 0

    # Заполняем известные рёбра
    for u in graph:
        for v, weight in graph[u].items():
            dist[u][v] = weight

    # Основная часть алгоритма - тройной вложенный цикл
    for k in range(n):  # Промежуточная вершина
        for i in range(n):  # Начальная вершина
            for j in range(n):  # Конечная вершина
                # Проверяем, дает ли путь через вершину k более короткое расстояние
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Проверка на отрицательные циклы
    for i in range(n):
        if dist[i][i] < 0:
            raise ValueError("Граф содержит отрицательный цикл")

    return dist


# Пример графа (ориентированный)
graph = {
    0: {1: 3, 2: 6},
    1: {0: 3, 2: 2},
    2: {0: 6, 1: 2}
}

# Запуск алгоритма
shortest_paths = floyd_warshall(graph)

# Вывод матрицы
for row in shortest_paths:
    print(row)