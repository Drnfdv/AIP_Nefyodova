import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Настройка главного окна
        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 400, 200)

        # Создание макета
        layout = QVBoxLayout()

        # Поле для ввода выражения
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Введите арифметическое выражение")
        layout.addWidget(self.input_field)

        # Кнопка "Вычислить"
        self.calculate_button = QPushButton("Вычислить", self)
        self.calculate_button.clicked.connect(self.calculate_result)
        layout.addWidget(self.calculate_button)

        # Поле для вывода результата
        self.result_field = QLineEdit(self)
        self.result_field.setReadOnly(True)  # Поле только для чтения
        self.result_field.setPlaceholderText("Результат")
        layout.addWidget(self.result_field)

        # Установка макета
        self.setLayout(layout)

    def calculate_result(self):
        # Получение введённого выражения
        expression = self.input_field.text()

        try:
            # Вычисление результата с помощью eval()
            result = eval(expression)
            # Вывод результата в поле для вывода
            self.result_field.setText(str(result))
        except Exception as e:
            # В случае ошибки выводим сообщение об ошибке
            self.result_field.setText(f"Ошибка: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = CalculatorApp()
    widget.resize(400, 300)
    widget.show()

    sys.exit(app.exec())