from PyQt5 import QtWidgets
import os


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        
        vbox = QtWidgets.QVBoxLayout()
        self.btn = QtWidgets.QPushButton("Выбрать файл")
        self.btn2 = QtWidgets.QPushButton("Удалить")
        self.btn3 = QtWidgets.QPushButton("Изменить имя файла")
        self.le = QtWidgets.QLineEdit()
        
        vbox.addWidget(self.btn)
        vbox.addWidget(self.le)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)
        
        self.setLayout(vbox)
        

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

#os.path.basename(path_of_the_file)
