class Graph:
    def __init__(self):
        self.vertices = 0 #вершины
        self.edges = 0 #ребра
        self.edge_list = [] #
        self.adj_matrix = [] #смежности
        self.inc_matrix = [] #инцидентности
        self.adj_list = {} #список смежности

    def read_from_file(self, filename):
        with open(filename, 'r') as file:
            # Чтение количества вершин
            line = file.readline().split('#')[0].strip()
            self.vertices = int(line)

            # Чтение количества ребер
            line = file.readline().split('#')[0].strip()
            self.edges = int(line)

            # Чтение списка ребер
            self.edge_list = []
            for _ in range(self.edges):
                line = file.readline().split('#')[0].strip()
                parts = list(map(int, line.split()))
                if len(parts) == 3:
                    u, v, weight = parts
                else:
                    u, v = parts
                    weight = 1
                self.edge_list.append((u, v, weight))

    def build_adjacency_matrix(self):
        # Инициализация матрицы смежности нулями
        self.adj_matrix = [[0] * (self.vertices + 1) for _ in range(self.vertices + 1)]

        for u, v, weight in self.edge_list:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # Для неориентированного графа

    def build_incidence_matrix(self):
        # Инициализация матрицы инцидентности нулями
        self.inc_matrix = [[0] * self.edges for _ in range(self.vertices + 1)]

        for edge_idx, (u, v, weight) in enumerate(self.edge_list):
            self.inc_matrix[u][edge_idx] = weight
            self.inc_matrix[v][edge_idx] = weight  # Для неориентированного графа

    def build_adjacency_list(self):
        #построение списка смежности
        self.adj_list = {i: [] for i in range(1, self.vertices + 1)}

        for u, v, weight in self.edge_list:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))  # Для неориентированного графа

    def print_adjacency_matrix(self):
        print("Матрица смежности:")
        for row in self.adj_matrix[1:]:
            print(row[1:])

    def print_incidence_matrix(self):
        print("Матрица инцидентности:")
        for row in self.inc_matrix[1:]:
            print(row)

    def print_edge_list(self):
        print("Список ребер:")
        for edge in self.edge_list:
            print(edge)

    def print_adjacency_list(self):
        print("Список смежности:")
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")


# Пример использования
if __name__ == "__main__":
    graph = Graph()
    graph.read_from_file("graph.txt")

    # Построение и вывод всех представлений
    graph.build_adjacency_matrix()
    graph.print_adjacency_matrix()

    graph.build_incidence_matrix()
    graph.print_incidence_matrix()

    graph.print_edge_list()

    graph.build_adjacency_list()
    graph.print_adjacency_list()