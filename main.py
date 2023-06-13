from PyQt5 import QtWidgets
import os


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(285, 100)
        
        self.file()
        
        self._createActions()
        self._createMenuBar()
    
    def file(self):
        self.setWindowTitle("Управление файлом")
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        
        vbox = QtWidgets.QVBoxLayout()
        self.btn = QtWidgets.QPushButton("Выбрать файл")
        self.btn.clicked.connect(self.select_file)
        self.btn2 = QtWidgets.QPushButton("Удалить файл")
        self.btn2.clicked.connect(self.delete_file)
        self.btn3 = QtWidgets.QPushButton("Изменить имя файла")
        self.btn3.clicked.connect(self.rename_file)
        self.le = QtWidgets.QLineEdit()
        self.btn4 = QtWidgets.QPushButton("Создать файл")
        self.btn4.clicked.connect(self.create_File)
        
        
        vbox.addWidget(self.btn)
        vbox.addWidget(self.le)
        vbox.addWidget(self.btn4)
        vbox.addWidget(self.btn3)
        vbox.addWidget(self.btn2)
    
        wid.setLayout(vbox)
    
    def folder(self):
        self.setWindowTitle("Управление папкой")
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        
        vbox = QtWidgets.QVBoxLayout()
        self.btn1 = QtWidgets.QPushButton("Выберите папку")
        self.btn1.clicked.connect(self.select_folder)
        self.btn2 = QtWidgets.QPushButton("Удалить папку")
        self.btn2.clicked.connect(self.delete_folder)
        self.btn3 = QtWidgets.QPushButton("Изменить имя папки")
        self.btn3.clicked.connect(self.rename_folder)
        self.le = QtWidgets.QLineEdit()
        self.btn4 = QtWidgets.QPushButton("Создать папку")
        self.btn4.clicked.connect(self.create_folder)
        
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.le)
        vbox.addWidget(self.btn4)
        vbox.addWidget(self.btn3)
        vbox.addWidget(self.btn2)
        
        wid.setLayout(vbox)
        
    def _createActions(self):
        self.fileAction = QtWidgets.QAction("Файл", self)
        self.fileAction.triggered.connect(self.file)
        
        self.folderAction = QtWidgets.QAction("Папка", self)
        self.folderAction.triggered.connect(self.folder)
        
    def _createMenuBar(self):
        menuBar = self.menuBar()
        modeMenu = QtWidgets.QMenu("Режим", self)
        menuBar.addMenu(modeMenu)
        modeMenu.addAction(self.fileAction)
        modeMenu.addAction(self.folderAction)
        
    def select_file(self):
        self.file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть файл", "")
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
        except OSError:
            print("Невозможно удалить файл")
            self.setWindowTitle("Невозможно удалить файл")
    
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
            
    def create_File(self):
        self.file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить файл", "")
        if self.file_name:
            f = open(self.file_name, "w")
            f.close()
            self.file = os.path.basename(self.file_name)
            self.le.setText(self.file)
            
    def create_folder(self):
        self.folder_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить папку", "")
        if self.folder_name:
            os.mkdir(self.folder_name)
            
    def rename_folder(self):
        try:
            if self.folder_name:
                folder_directory = os.path.dirname(self.folder_name)
                new_folder_name = str(self.le.text())
                new_folder_path = os.path.join(folder_directory, new_folder_name)
                os.rename(self.folder_name, new_folder_path)
                self.folder_name = new_folder_path
        except AttributeError:
            print("Выберите файл")
            self.setWindowTitle("Выберите файл")
    
    def delete_folder(self):
        try:
            if self.folder_name:
                os.rmdir(self.folder_name)
        except AttributeError:
            print("Выберите папку")
            self.setWindowTitle("Выберите папку")
        except OSError:
            print("Невозможно удалить папку")
            self.setWindowTitle("Невозможно удалить папку")
    
    def select_folder(self):
        self.folder_name = QtWidgets.QFileDialog.getExistingDirectory(self, "Открыть папку", "")
        if self.folder_name:
            self.folder = os.path.basename(self.folder_name)
            self.le.setText(self.folder)
        
if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
