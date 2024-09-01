import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import random as rd
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn=QPushButton(self)
        self.btn.setText('Generate Lotto Number')
        self.btn.clicked.connect(self.genNumbers)
        
        self.label=QLabel('Good Luck',self)
        self.label.setAlignment(Qt.AlignCenter)
        
        layout = QVBoxLayout() #왜 layout에서는 self를 안넣지?
        layout.addWidget(self.btn)
        layout.addWidget(self.label)
        
        self.setLayout(layout)
        
        self.setWindowTitle('My Second Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()
        
    def genNumbers(self):
        numbers=rd.sample(range(1,46),6)
        numbers.sort()
        self.label.setText(f"로또 번호 : {numbers}")
        

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())