from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

from logic import Qr_Read,Filesave

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("..\\UI\\Reader.ui",self)
        self.show()

        self.currentfile = ""

        self.Exitbutton.triggered.connect(self.Exit)
        self.Clearbutton.triggered.connect(self.Clear)
        self.Savebutton.triggered.connect(self.Save)

        self.Readbutton.clicked.connect(self.Read)

        self.Display.setPixmap(QPixmap("..\\UI\\StartUp.png").scaled(400,400, Qt.KeepAspectRatio))
        self.Output.insertPlainText("Follow Me At: https://github.com/Quack-Duck12")
        
    def Exit(self):
         exit()

    def Clear(self):
        self.Filepath.clear()
        self.Output.clear()

        self.Display.setPixmap(QPixmap("..\\UI\\StartUp.png").scaled(400,400, Qt.KeepAspectRatio))

    def Read(self):

        if self.Checkbox.isChecked(): 
            self.Output.clear()

        Path = self.Filepath.text()
        self.Display.setPixmap(QPixmap(Path).scaled(400,400, Qt.KeepAspectRatio))

        self.Output.insertPlainText((Qr_Read(Path)))

    def Save(self):

        Data = self.Output.toPlainText()
        Path = self.Filepath.text()

        Filesave(Data,Path)


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()


if __name__ == "__main__":
    main()