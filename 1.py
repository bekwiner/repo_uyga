
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


class NoteApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("App")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("Noteni kiriting:", self)
        self.note_input = QLineEdit(self)
        self.saved_notes = QTextEdit(self)
        self.saved_notes.setReadOnly(True) 
        self.save_button = QPushButton("Noteni saqlash", self)

        self.save_button.clicked.connect(self.save_note)

        input_layout = QHBoxLayout()  
        input_layout.addWidget(self.label)
        input_layout.addWidget(self.note_input)

        layout = QVBoxLayout()  
        layout.addLayout(input_layout)
        layout.addWidget(self.save_button)
        layout.addWidget(self.saved_notes)

        self.setLayout(layout)

    def save_note(self):
        note = self.note_input.text()
        if note:
            self.saved_notes.append(f" - {note}")
            self.note_input.clear() 


app = QApplication(sys.argv)
window = NoteApp()
window.show()
sys.exit(app.exec_())
