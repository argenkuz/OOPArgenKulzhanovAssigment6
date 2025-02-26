from PyQt6.QtWidgets import  QMainWindow
from ui_7 import Ui_MainWindow

class BMIApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate_bmi)

    def calculate_bmi(self):
        try:
            height = float(self.line2.text())
            weight = float(self.line1.text())
            selected_box = self.comboBox.currentIndex()

            if selected_box == 1:
                height = height * 0.3048
            else:
                height = height / 100

            bmi = round((weight / (height ** 2)), 1)
            self.output.setText(str(bmi))

        except ValueError:
            self.output.setText("Invalid Input")

