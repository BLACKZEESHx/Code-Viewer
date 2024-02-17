# Importing packages
from PyQt6.QtCore import Qt, QSettings, QRect
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QGraphicsBlurEffect
import sys

class Code_Beauty(QMainWindow):
    def __init__(self):
        super(Code_Beauty, self).__init__()
        self.setStyleSheet(
        """
            *{
                background-image: url("D:/Go code/Code Viewer/App/bg.png");
                background-repeat: no-repeat;
                background-position: center;
            }

            QWidget#MainCodeW {
                background-color: rgb(255, 255, 255);
                background-image: url("D:/Go code/Code Viewer/App/highlighted_code.png");
                background-repeat: no-repeat;
                background-position: center;
                border-radius: 20px;
            }
        """)
        # self.setGeometry(QRect(0, 0, 700, 500))

        self.MainCodeW = QWidget(self)
        self.MainCodeW.setObjectName("MainCodeW")

        self.ChildCodepic = QPixmap("highlighted_code.png")
        self.ChildCodeCW = QLabel(self.MainCodeW)
        # self.ChildCodeCW.setPixmap(self.ChildCodepic)
        picsize = QImage("highlighted_code.png")
        picsize.setText("Description", "This is the description")
        self.MainCodeW.setGeometry(self.geometry().width()//2+self.MainCodeW.geometry().width()*2,\
                                    self.geometry().height()//4-self.MainCodeW.geometry().height(),\
                                      picsize.width(), picsize.height())
        self.blur = QGraphicsBlurEffect(self)
        self.blur.setBlurRadius(44)

                                      

def run():
    app = QApplication(sys.argv)
    window = Code_Beauty()
    window.showMaximized()
    sys.exit(app.exec())

if __name__ == '__main__':
    run()