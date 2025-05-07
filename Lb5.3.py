import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QInputDialog, QFileDialog)
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt
import random

class FlagGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Генератор полосатого флага')
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel('Здесь будет отображён ваш флаг')
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.generate_btn = QPushButton('Сгенерировать флаг')
        self.generate_btn.clicked.connect(self.generate_flag)
        self.layout.addWidget(self.generate_btn)

        self.flag_pixmap = None

    def generate_flag(self):
        num_colors, ok = QInputDialog.getInt(
            self, 'Выбор количества цветов',
            'Введите количество цветов для флага (2-10):',
            3, 2, 10, 1
        )

        if not ok:
            return

        # Создаём изображение флага
        width = 400
        height = 250
        flag = QPixmap(width, height)
        painter = QPainter(flag)

        # Вычисляем высоту каждой полосы как целое число
        stripe_height = height // num_colors
        remaining_height = height - (stripe_height * num_colors)

        # Генерируем случайные цвета для полос
        colors = []
        for _ in range(num_colors):
            colors.append(QColor(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            ))

        # Рисуем полосы
        y = 0
        for i in range(num_colors):
            # Последняя полоса может быть немного выше, чтобы компенсировать округление
            h = stripe_height + (1 if i < remaining_height else 0)
            painter.fillRect(0, y, width, h, colors[i])
            y += h

        painter.end()

        self.flag_pixmap = flag
        self.label.setPixmap(flag.scaled(
            width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation
        ))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FlagGenerator()
    window.show()
    sys.exit(app.exec_())