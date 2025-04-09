import random
from queue import Queue # Для обхода в ширину

class Node:
    '''
    Класс для хранения единичного узла бинарного дерева
    '''
    def __init__(self, val):
        self.l = None  # Связь с левым потомком
        self.r = None  # Связь с правым потомком
        self.v = val   # Ключ (значение, которое хранится в узле)

class Tree:
    '''
    Класс для хранения бинарного дерева поиска
    '''
    def __init__(self):
        '''
        Создаем пустое дерево
        '''
        self.root = None

    def getRoot(self):
        '''
        Получение значения корня
        '''
        return self.root

    def add(self, val):
        '''
        Добавление узла.
        Если дерево не содержит элементов, создаем дерево из одного элемента.
        Если дерево не пустое, вызываем вспомогательную функцию добавления.
        '''
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        '''
        Вспомогательная рекурсивная функция добавления.
        Если элемент меньше значения текущего узла,
        добавляем его в левое поддерево.
        В противном случае добавляем его в правое поддерево.
        '''
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        '''
        Поиск узла.
        Если узел не пуст, вызываем вспомогательную функцию поиска,
        иначе возвращаем None.
        '''
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        '''
        Вспомогательная рекурсивная функция поиска.
        Если узел найден, возвращаем его. Если значение узла больше искомого,
        продолжаем поиск в левом поддереве, если оно не пустое. Если значение
        узла меньше искомого, продолжаем поиск в правом поддереве,
        если оно не пустое.
        '''
        if val == node.v:
            return node.v
        elif (val < node.v and node.l != None):
            return self._find(val, node.l)
        elif (val > node.v and node.r != None):
            return self._find(val, node.r)

    def deleteTree(self):
        '''
        Удаление дерева.
        Удаляем корень, все остальное делает сборщик мусора.
        '''
        self.root = None

    def printTree(self):
        '''
        Печать дерева.
        Вызываем вспомогательную функцию печати.
        '''
        if self.root is not None:
            print("Дерево:")
            self._printTree(self.root)
            print()
        else:
            print("Дерево не существует")

    def _printTree(self, node):
        '''
        Вспомогательная рекурсивная функция печати.
        '''
        if node is not None:
            print(str(node.v), end=' ')
            self._printTree(node.l)
            self._printTree(node.r)

    def BFS(self):
        '''
        Обход дерева в ширину.
        '''
        if self.root is not None:
            q = Queue()
            q.put(self.root)
            while not q.empty():
                x = q.get()
                print(str(x.v), end=' ')
                if x.l is not None:
                     q.put(x.l)
                if x.r is not None:
                     q.put(x.r)
            print()
        else:
            print("Дерево не существует")

def generate_random_tree(n, min_val, max_val):
    if n <=0:
        return None

    numbers = random.sample(range(min_val, max_val + 1), n)

    tree = Tree()
    tree.add(numbers[0]) #первое число корень

    for num in numbers[1:]:
        tree.add(num)

    return tree, numbers


n = 10
min_val = 1
max_val = 10

tree, numbers = generate_random_tree(n, min_val, max_val)

print(f"Сгенерированные числа: {numbers}")
tree.printTree()
print("Обход в ширину (BFS):")
tree.BFS()