import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QInputDialog,
                             QPushButton, QVBoxLayout, QMessageBox)
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random


class FlagDrawer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.flag_colors = 3  # Значение по умолчанию
        self.colors = []
        self.generate_colors()

    def initUI(self):
        self.setWindowTitle('Генератор полосатых флагов')
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()

        # Кнопка для изменения количества цветов
        self.btn_set_colors = QPushButton('Установить количество цветов', self)
        self.btn_set_colors.clicked.connect(self.show_color_dialog)
        layout.addWidget(self.btn_set_colors)

        # Кнопка для перегенерации цветов
        self.btn_regenerate = QPushButton('Сгенерировать новые цвета', self)
        self.btn_regenerate.clicked.connect(self.regenerate_colors)
        layout.addWidget(self.btn_regenerate)

        self.setLayout(layout)

    def show_color_dialog(self):
        # Диалоговое окно для ввода количества цветов
        count, ok = QInputDialog.getInt(
            self,
            "Количество цветов флага",
            "Сколько полос должно быть на флаге?",
            self.flag_colors,  # Значение по умолчанию
            1,  # Минимальное значение
            10,  # Максимальное значение
            1  # Шаг
        )

        if ok:
            self.flag_colors = count
            self.generate_colors()
            self.update()  # Перерисовываем флаг

    def generate_colors(self):
        # Генерация случайных цветов для флага
        self.colors = []
        for _ in range(self.flag_colors):
            # Случайный цвет в RGB
            color = QColor(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            self.colors.append(color)

    def regenerate_colors(self):
        # Перегенерировать цвета без изменения количества
        self.generate_colors()
        self.update()

    def paintEvent(self, event):
        # Отрисовка флага
        painter = QPainter(self)
        painter.begin(self)

        # Размеры области для флага
        flag_width = 300
        flag_height = 200
        start_x = (self.width() - flag_width) // 2
        start_y = 50

        # Рисуем каждую полосу
        stripe_height = flag_height // self.flag_colors
        for i in range(self.flag_colors):
            painter.setBrush(self.colors[i])
            painter.drawRect(
                start_x,
                start_y + i * stripe_height,
                flag_width,
                stripe_height
            )

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FlagDrawer()
    window.show()
    sys.exit(app.exec_())