from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

from logic import Generate_QR

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("UI\\Generator.ui",self)
        self.show()

        self.currentfile = ""
        
        self.GenerateButton.clicked.connect(self.Generate)
        self.ExitButton.triggered.connect(self.Exit)
        self.ClearButton.triggered.connect(self.Clear)

        self.Display.setPixmap(QPixmap("UI\\StartUp.png").scaled(441, 441, Qt.KeepAspectRatio))

    def Generate(self):
        data = self.Databox.text()
        version = self.Versionbox.text()
        border = self.Borderbox.text()
        colour = self.Colourbox.currentText()
        filename = str(self.Namebox.text()) + self.Filetype.currentText()
        filelocate = str(self.Locationbox.text())

        if filelocate not in [""," "]:
            filelocate = filelocate + "\\"

        if version in ["", " "] or not version.isdigit():
            version = 7
        else:
            version = int(version)

        if not (0 < version < 41):
            version = 7

        if not border:
            border = 3
        else:
            border = int(border)

        Generate_QR(data, version, border, colour,filename,filelocate)

        self.Display.setPixmap(QPixmap(r"{}{}".format(filelocate, filename)).scaled(441, 441, Qt.KeepAspectRatio))


    def Clear(self):
        self.Databox.clear()
        self.Versionbox.clear()
        self.Borderbox.clear()
        self.Namebox.clear()
        self.Locationbox.clear()

        self.Colourbox.setCurrentIndex(0)
        self.Filetype.setCurrentIndex(0)

        self.Display.setPixmap(QPixmap("UI\\StartUp.png").scaled(441, 441, Qt.KeepAspectRatio))

        

    def Exit(self):
        exit()

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()


if __name__ == "__main__":
    main()
