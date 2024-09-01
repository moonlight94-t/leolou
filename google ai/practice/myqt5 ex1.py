## Ex 3-1. 창 띄우기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

#Qwidget 클래스의 특성을 MyApp이 상속받음 거기에 멤버함수 몇개 추가
class MyApp(QWidget):

#super Qwidget을 가르킴 상속받은 부모클래스의 __init__호출
    def __init__(self):
        super().__init__()
        self.initUI()
#순서는 상관없나보네 ㅇㅇ 뒤에 정의되더라도 클래스하나에서는 크게 상관없는듯

    def initUI(self):
        self.setWindowTitle('ICON')
        self.setWindowIcon(QIcon('web.png'))
        self.move(300, 300)
        self.resize(400, 200)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_()) # GUI 창이종료될때 sys.exit 작동되서 꺼짐
   
   #gui 는 event기반으로 동작 / event가 들어올 때 가지 대기 / terminal의 text driven 과 다름