import heapq  #для работы с очередью


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)  #извлекает элемент с наименьшим расстоянием

        if current_distance > distances[current_vertex]:  #если найденное больше сохраненного то пропускаем(игнорирует устаревшие записм)
            continue

        for neighbor, weight in graph[current_vertex].items(): #перебираем всех соседей и ребра до них
            distance = current_distance + weight
            if distance < distances[neighbor]: #если найден более короткий путь обновлем расстояние
                distances[neighbor] = distance #новое расстояние
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Пример графа (в формате словаря словарей)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)
print(f"Кратчайшие пути из вершины {start_vertex}: {shortest_paths}")