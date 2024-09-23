# uyga vazifa: ikki.py

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)


class UserInfoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Foydalanuvchi ma'lumotlari")
        self.setGeometry(100, 100, 400, 400)
        self.name_label = QLabel("Ism:", self)
        self.name_input = QLineEdit(self)

        self.email_label = QLabel("Email:", self)
        self.email_input = QLineEdit(self)

        self.bio_label = QLabel("biografiya:", self)
        self.bio_input = QTextEdit(self)

        self.submit_button = QPushButton("qabulqilish", self)
        self.output_area = QTextEdit(self)
        self.output_area.setReadOnly(True)  
        self.submit_button.clicked.connect(self.info)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.bio_label)
        layout.addWidget(self.bio_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.output_area)

        self.setLayout(layout)

    def info(self):
        name = self.name_input.text()
        email = self.email_input.text()
        bio = self.bio_input.toPlainText()

        self.output_area.setPlainText(
            f"Ism: {name}\nEmail: {email}\nQisqacha biografiya:\n{bio}"
        )


app = QApplication(sys.argv)
window = UserInfoApp()
window.show()
sys.exit(app.exec_())
