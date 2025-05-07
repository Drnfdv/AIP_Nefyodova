import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QCheckBox, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
class MaslenitsaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Настройка главного окна
        self.setWindowTitle("Масленица")
        self.setGeometry(100, 100, 400, 300)

        # Создание макета
        layout = QVBoxLayout()

        # Группа для выбора добавок
        checkbox_layout = QVBoxLayout()

        # Создаем CheckBox для разных добавок
        self.addon_checkboxes = {
            "Сметана": QCheckBox("Сметана"),
            "Мед": QCheckBox("Мед"),
            "Икра": QCheckBox("Икра"),
        }

        # Добавляем CheckBox в макет
        for checkbox in self.addon_checkboxes.values():
            checkbox_layout.addWidget(checkbox)

        # Кнопка "Показать блины"
        self.show_button = QPushButton("Показать блины")
        self.show_button.clicked.connect(self.show_pancakes)
        checkbox_layout.addWidget(self.show_button)

        # Поле для отображения изображения
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addLayout(checkbox_layout)
        layout.addWidget(self.image_label)

        # Установка макета
        self.setLayout(layout)

    def show_pancakes(self):
        # Список выбранных добавок
        selected_addons = [addon for addon, checkbox in self.addon_checkboxes.items() if checkbox.isChecked()]

        # Формируем имя файла изображения на основе выбранных добавок
        image_name = "pancakes_" + "_".join(selected_addons) + ".png"

        try:
            # Загружаем изображение
            pixmap = QPixmap(image_name)
            if not pixmap.isNull():
                # Отображаем изображение
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))
            else:
                # Если изображение не найдено
                self.image_label.setText("Изображение не найдено")
        except Exception as e:
            # Обработка ошибок
            self.image_label.setText(f"Ошибка: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MaslenitsaApp()
    window.show()
    sys.exit(app.exec())