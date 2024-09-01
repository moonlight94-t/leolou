import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class LottoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Lotto Number Generator')
        self.setGeometry(300, 300, 300, 200) 
        #가로위치 , 세로위치, 가로크기, 세로크기

        # 버튼 생성
        self.btn = QPushButton('Generate Lotto Numbers', self)
        self.btn.clicked.connect(self.generateNumbers) 
        self.btn.setStyleSheet("color: red; font-size: 20px;")
        #connect 함수연결 인스턴스의 메소드임을 명시화

        # 로또 번호를 표시할 레이블 생성
        self.lottoLabel = QLabel('push button above', self)
        self.lottoLabel.setAlignment(Qt.AlignCenter)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.lottoLabel)

        self.setLayout(layout)

    def generateNumbers(self):
        numbers = random.sample(range(1, 46), 6)  # 1부터 45까지의 숫자 중 6개를 무작위로 선택
        numbers.sort()  # 선택된 숫자 정렬
        self.lottoLabel.setText('Lotto Numbers: ' + ', '.join(map(str, numbers)))  # 레이블에 표시

def main():
    app = QApplication(sys.argv)
    print(sys.argv)
    ex = LottoApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()