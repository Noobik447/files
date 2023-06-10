from PyQt5 import QtWidgets
import os


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("Управление файлом")
        
        vbox = QtWidgets.QVBoxLayout()
        self.btn = QtWidgets.QPushButton("Выбрать файл")
        self.btn.clicked.connect(self.select_file)
        self.btn2 = QtWidgets.QPushButton("Удалить")
        self.btn2.clicked.connect(self.delete_file)
        self.btn3 = QtWidgets.QPushButton("Изменить имя файла")
        self.btn3.clicked.connect(self.rename_file)
        self.le = QtWidgets.QLineEdit()
        
        vbox.addWidget(self.btn)
        vbox.addWidget(self.le)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)
        
        self.setLayout(vbox)
        
    def select_file(self):
        self.file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "")
        if self.file_name:
            self.file = os.path.basename(self.file_name)
            self.le.setText(self.file)
    
    def delete_file(self):
        try:
            if self.file_name:
                os.remove(self.file_name)
        except AttributeError:
            print("Выберите файл")
            self.setWindowTitle("Выберите файл")
    
    def rename_file(self):
        try:
            if self.file_name:
                file_directory = os.path.dirname(self.file_name)
                new_file_name = str(self.le.text())
                new_file_path = os.path.join(file_directory, new_file_name)
                os.rename(self.file_name, new_file_path)
                self.file_name = new_file_path
        except AttributeError:
            print("Выберите файл")
            self.setWindowTitle("Выберите файл")
            

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
