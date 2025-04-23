from collections import defaultdict  #создание словаря автоматически инициализирует значения


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)  #список смежности

    def add_edge(self, u, v):  #добавление ребра между вершинами
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_connected(self):  #проверяет связность графа
        visited = [False] * (self.V + 1)  #список посещенных
        stack = []

        # Находим первую вершину с рёбрами(поиск в глубину)
        start_vertex = 1
        for v in range(1, self.V + 1):
            if len(self.graph[v]) > 0: #степень
                start_vertex = v
                break

        # вершина с 0 степенью имеющая ребра
        stack.append(start_vertex)
        visited[start_vertex] = True

        while stack:
            u = stack.pop()
            for v in self.graph[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)

        # Проверяем связность
        for v in range(1, self.V + 1):
            if not visited[v] and len(self.graph[v]) > 0:
                return False
        return True

    def has_eulerian_cycle(self):  #проверяет цикл
        if not self.is_connected():
            return False

        for v in range(1, self.V + 1):  #проверяем четность степени
            if len(self.graph[v]) % 2 != 0:
                return False
        return True


if __name__ == "__main__":
    # Граф с Эйлеровым циклом (все степени чётные)
    g1 = Graph(4)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    g1.add_edge(3, 4)
    g1.add_edge(4, 1)

    print("Граф g1 имеет Эйлеров цикл?", g1.has_eulerian_cycle())  # True

    # Граф без цикла (две нечётные степени)
    g2 = Graph(3)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)

    print("Граф g2 имеет Эйлеров цикл?", g2.has_eulerian_cycle())  # False