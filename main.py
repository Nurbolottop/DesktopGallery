import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QVBoxLayout, QHBoxLayout, QListWidget, QFileDialog
)
from PyQt5.QtCore import Qt
import os

app = QApplication(sys.argv)
main_win = QWidget()
main_win.setWindowTitle('Easy Editor')
main_win.resize(700, 400)
statement = QLabel('Картинка')
btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_mirror = QPushButton('Зеркало')
btn_sharpness = QPushButton('Резкость')
btn_ok = QPushButton('Ч/Б')
list_widget = QListWidget(main_win)
list_widget.setGeometry(12,39,50,30)
list_widget.resize(80,300)
btn_folder = QPushButton('Папка')

lister = QListWidget()



line0 = QHBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line1.addWidget(statement, alignment = Qt.AlignCenter)
line0.addWidget(btn_folder, alignment = Qt.AlignLeft)
line2.addWidget(btn_left)
line2.addWidget(btn_right)
line2.addWidget(btn_mirror)
line2.addWidget(btn_sharpness)
line2.addWidget(btn_ok)
def choose_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter_graphics_files():
    files = os.listdir(workdir)
    graphic_files = []
    extensions = (".jpeg", ".png", ".jpg")
    for filename in files:
        if filename.endswith(extensions):
            graphic_files.append(filename)
    return graphic_files

def show_filenames_list():
    choose_workdir()
    graphic_files = filter_graphics_files()
    list_widget.clear()
    for filename in graphic_files:
        list_widget.addItem(filename)
btn_folder.clicked.connect(show_filenames_list)

line3 = QVBoxLayout()
line3.addLayout(line0)
line3.addLayout(line1)
line3.addLayout(line2)

main_win.setLayout(line0)
main_win.setLayout(line1)
main_win.setLayout(line2)
main_win.setLayout(line3)
main_win.show()
app.exec_()