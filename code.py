import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import networkx
import matplotlib.pyplot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

class BSTNode:
    def __init__(self, key):  # узлы
        self.key = key
        self.left = None
        self.right = None

class AnimatedButton(QPushButton): #кнопки
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self._anim = QPropertyAnimation(self, b"geometry", duration=200)
        self.setFixedSize(170, 50)
        self._base_geom = None
        (self.setStyleSheet
         ("""
            QPushButton 
                {background-color: #94b5c2; 
                border: 1px solid #7a839e; 
                border-radius: 8px;
                padding: 8px;
                color: #423c6d; 
                font-size: 14px;}
            QPushButton:hover 
                {background-color: #7a839e; 
                border: 1px solid #7a839e; }
            QPushButton:pressed 
                {background-color: #423c6d; }
         """
         )
        )

class BSTVisualizer(QMainWindow):   #графическое изображение
    def __init__(self):
        super().__init__()
        self.bst = None
        self.setWindowTitle("Визуализация BST")
        self.setGeometry(100, 100, 1000, 800)
        self.set_custom_theme()
        self.init_ui()   # Инициализация графического интерфейса

    def set_custom_theme(self):
        self.setStyleSheet("""
            QMainWindow { background-color: #fef5d8; } 
            QPushButton 
                {background-color: #94b5c2; 
                border: 1px solid #7a839e; 
                border-radius: 8px;
                padding: 8px;
                min-width: 170px;
                color: #423c6d; 
                font-size: 14px}
            QPushButton:hover 
                {background-color: #7a839e; 
                border: 1px solid #7a839e; }
            QPushButton:pressed { background-color: #423c6d; } 
            QLineEdit 
                {background-color: #eadcc1; 
                border: 1px solid #7a839e; 
                border-radius: 8px;
                padding: 5px;
                color: #423c6d; }
            QLabel { color: #423c6d; } 
            QMessageBox 
                {background-color: #eadcc1;
                color: #423c6d;}
            QMessageBox QLabel 
                {color: #423c6d;}
        """
        )

    def init_ui(self):   #расположение графических элементов
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        title = QLabel("Визуализатор Бинарного Дерева Поиска")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #423c6d; margin-bottom: 20px;")
        main_layout.addWidget(title)

        control_layout = QHBoxLayout()
        self.input_label = QLabel("Введите число:")
        self.input_label.setFont(QFont("Arial", 15))
        self.input_entry = QLineEdit()
        self.input_entry.setFont(QFont("Arial", 13))
        self.input_entry.setFixedWidth(150)
        self.input_entry.setFixedHeight(50)
        self.input_entry.setPlaceholderText("Целое число...")

        self.add_button = AnimatedButton("➕ Добавить")
        self.add_button.setToolTip("Добавить узел в дерево")
        self.add_button.clicked.connect(self.add_node)

        self.delete_button = AnimatedButton("🗑️ Удалить")
        self.delete_button.setToolTip("Удалить узел из дерева")
        self.delete_button.clicked.connect(self.delete_node)

        self.search_button = AnimatedButton("🔍 Найти")
        self.search_button.setToolTip("Найти узел в дереве")
        self.search_button.clicked.connect(self.search_node)

        self.info_button = AnimatedButton("ℹ️ Информация")
        self.info_button.setToolTip("Показать информацию о дереве")
        self.info_button.clicked.connect(self.show_info)
        
        self.balance_button = AnimatedButton("⚖️ Сбалансировать")
        self.balance_button.setToolTip("Сбалансировать дерево")
        self.balance_button.clicked.connect(self.balance_tree)

        control_layout.addWidget(self.input_label)
        control_layout.addWidget(self.input_entry)
        control_layout.addSpacing(10)
        control_layout.addWidget(self.add_button)
        control_layout.addWidget(self.delete_button)
        control_layout.addWidget(self.search_button)
        control_layout.addWidget(self.info_button)
        control_layout.addWidget(self.balance_button)
        control_layout.addStretch()
        main_layout.addLayout(control_layout)

        self.figure, self.ax = matplotlib.pyplot.subplots(figsize=(10, 8))   # Создание фигуры и осей matplotlib
        self.figure.patch.set_facecolor("#94b5c2")
        self.ax.set_facecolor("#94b5c2")
        matplotlib.pyplot.rcParams["text.color"] = "#423c6d"
        matplotlib.pyplot.rcParams["axes.labelcolor"] = "#423c6d"
        matplotlib.pyplot.rcParams["xtick.color"] = "#423c6d"
        matplotlib.pyplot.rcParams["ytick.color"] = "#423c6d"
        self.canvas = FigureCanvasQTAgg(self.figure)    # Создание холста PyQt5 для отображения графика matplotlib
        self.canvas.setStyleSheet("background-color: #94b5c2; border-radius: 10px;")
        main_layout.addWidget(self.canvas)

    def add_node(self):   #добавляет узел в дерево
        try:
            key = int(self.input_entry.text())
            if self.bst is None:
                self.bst = BSTNode(key)
            else:
                self._insert(self.bst, key)
            self.draw_tree()
        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Введите целое число!")

    def _insert(self, node, key):  #рекурсивно добавляет узел в дерево
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert(node.right, key)

    def delete_node(self):    #удаляет узел из дерева
        try:
            key = int(self.input_entry.text())
            self.bst = self._delete(self.bst, key)
            self.draw_tree()
        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Введите целое число!")

    def _delete(self, node, key):   #Рекурсивно удаляет узел из дерева
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return node

    def _min_value_node(self, node):   #Находит узел с минимальным значением в поддереве.
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search_node(self):    #Ищет узел в дереве.
        try:
            key = int(self.input_entry.text())
            found = self._search(self.bst, key)
            if found:
                QMessageBox.information(self, "Поиск", f"Число {key} найдено!")
                self.draw_tree(highlight=key)
            else:
                QMessageBox.information(self, "Поиск", f"Число {key} не найдено!")
        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Введите целое число!")

    def _search(self, node, key):    #Рекурсивно ищет узел в дереве.
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def show_info(self):     #Отображает информацию о дереве
        if self.bst is None:
            QMessageBox.information(self, "Информация", "Дерево пусто!")
            return

        depth = self._max_depth(self.bst)
        count = self._count_nodes(self.bst)
        QMessageBox.information(
            self,
            "Информация",
            f"Глубина дерева: {depth}\n"
            f"Количество узлов: {count}\n"
            f"Баланс: {'Сбалансировано' if self._is_balanced(self.bst) else 'Не сбалансировано'}",
        )

    #Рекурсивные методы для вычисления глубины дерева, количества узлов и проверки сбалансированности.
    def _max_depth(self, node):
        if node is None:
            return 0
        return 1 + max(self._max_depth(node.left), self._max_depth(node.right))

    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def _is_balanced(self, node):
        if node is None:
            return True
        left_depth = self._max_depth(node.left)
        right_depth = self._max_depth(node.right)
        return abs(left_depth - right_depth) <= 1 and self._is_balanced(node.left) and self._is_balanced(node.right)

    def draw_tree(self, highlight=None):    #Отрисовывает дерево на графике matplotlib.
        self.ax.clear()
        if self.bst is None:
            self.ax.text(0.5, 0.5, "Дерево пустое", ha="center", va="center", fontsize=15, color="#423c6d")
            self.canvas.draw()
            return

        G = networkx.DiGraph()
        self._build_graph(G, self.bst)
        pos = self._hierarchy_pos(G, self.bst.key)
        node_colors = ["#eadcc1" if node == highlight else "#7a839e" for node in G.nodes()]
        edge_colors = ["#7a839e" for _ in G.edges()]

        networkx.draw_networkx_nodes(
            G,
            pos,
            ax=self.ax,
            node_size=1500,
            node_color=node_colors,
            alpha=0.9,
            edgecolors="#423c6d",
            linewidths=1,
        )
        (networkx.draw_networkx_edges
            (G, pos, ax=self.ax, edge_color=edge_colors, width=2, arrows=True, arrowstyle="->", arrowsize=15)
        )
        networkx.draw_networkx_labels(
            G, pos, ax=self.ax, font_size=12, font_color="#fef5d8", font_weight="bold"
        )

        for node, (x, y) in pos.items():
            self.ax.text(
                x,
                y + 0.02,
                str(node),
                ha="center",
                va="center",
                fontsize=12,
                color="#94b5c2",
                zorder=-1,
                alpha=0.3,
            )
        self.ax.axis("off")
        self.canvas.draw()

    def _build_graph(self, G, node):   #Рекурсивно преобразует BST в граф networkx
        if node is None:
            return
        G.add_node(node.key)
        if node.left:
            G.add_edge(node.key, node.left.key)
            self._build_graph(G, node.left)
        if node.right:
            G.add_edge(node.key, node.right.key)
            self._build_graph(G, node.right)

    def _hierarchy_pos(self, G, root, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5):  #Рекурсивно вычисляет позиции узлов для иерархической компоновки графа.
        pos = {root: (xcenter, vert_loc)}
        children = list(G.successors(root))
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos.update(
                    self._hierarchy_pos(
                        G, child, width=dx, vert_gap=vert_gap, vert_loc=vert_loc - vert_gap, xcenter=nextx
                    )
                )
        return pos

    def balance_tree(self):   #Сбалансирует дерево.
        if self.bst is None:
            QMessageBox.information(self, "Информация", "Дерево пустое!")
            return

        # Получить массив из дерева (inorder traversal)
        array = self._tree_to_array(self.bst)

        # Сбалансировать дерево
        self.bst = self.build_balanced_bst_from_array(array)

        # Перерисовать дерево
        self.draw_tree()

    def _tree_to_array(self, node):
        """Преобразование дерева в отсортированный массив."""
        if node is None:
            return []
        return self._tree_to_array(node.left) + [node.key] + self._tree_to_array(node.right)
    def build_balanced_bst(self, sorted_array, start, end):
        """Создание сбалансированного BST из отсортированного массива."""
        if start > end:
            return None
        mid = (start + end) // 2
        root = BSTNode(sorted_array[mid])
        root.left = self.build_balanced_bst(sorted_array, start, mid - 1)
        root.right = self.build_balanced_bst(sorted_array, mid + 1, end)
        return root
    def build_balanced_bst_from_array(self, array):
        """Основная функция для создания сбалансированного BST из массива."""
        sorted_array = sorted(list(set(array)))  # Удаление дубликатов и сортировка
        return self.build_balanced_bst(sorted_array, 0, len(sorted_array) - 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = BSTVisualizer()
    window.show()
    sys.exit(app.exec_())
