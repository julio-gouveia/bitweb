import sys, os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QInputDialog, QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("BitWeb") 

        # Label "Link" and Input Box
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Link:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        # Button to Download Link
        pybutton = QPushButton("Download", self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 60)

    def clickMethod(self):
        self.folder, ok = QInputDialog.getText(self, 'Enter Folder', 'Enter Your Folder')
        if ok:
                os.chdir(self.folder)
                os.system("wget " + self.line.text())
                
                msg = QMessageBox()
                msg.setWindowTitle("All Good")
                msg.setText("Your Files are downloaded")
                
                x = msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
