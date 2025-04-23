class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Количество вершин
        self.graph = []  # Список рёбер в формате (u, v, weight)

    #добавление ребра в граф
    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))

    # Поиск корня вершины
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Объединение двух множеств
    def union(self, parent, rank, x, y): #находим корни
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]: #глубина дерева
            parent[x_root] = y_root        #меньшее дерево подвешиваем к большему
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    # Алгоритм Краскала
    def kruskal_mst(self):
        result = []  # Минимальное остовное дерево
        i = 0  # Индекс для сортированных рёбер
        e = 0  # Индекс для result[](счетчик ребер)

        # Сортируем рёбра по весу
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Инициализируем множества (каждая вершина — своё множество)
        for node in range(self.V + 1):  # Вершины нумеруются с 1
            parent.append(node)
            rank.append(0)

        # Выбираем рёбра, пока не получим V-1 рёбер
        while e < self.V - 1 and i < len(self.graph):
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # Если ребро не образует цикл, добавляем его в MST
            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        # Вывод результата
        print("Минимальное остовное дерево (алгоритм Краскала):")
        for u, v, weight in result:
            print(f"{u} -- {v} (вес: {weight})")


# Пример использования
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(1, 2, 5)
    g.add_edge(2, 3, 7)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 1, 2)

    g.kruskal_mst()