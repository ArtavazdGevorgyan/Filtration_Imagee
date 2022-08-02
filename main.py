from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog, QMessageBox
import sys
import cv2
import os
import shutil
import filters
import resources

try:
    os.mkdir(".cache")
except FileExistsError:
    pass


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        # Window setup and styling
        self.setWindowTitle("Photo Editor")
        self.setGeometry(100, 100, 0, 0)
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color:#333333")

        # Creating MenuBar
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)
        fileMenu = QMenu("&File", self)
        self.menuBar.addMenu(fileMenu)
        fileMenu.addAction("Open", self.menu_action_clicked)
        fileMenu.addAction("Save", self.menu_action_clicked)

        # Window widgets setup and styling
        self.img_label = QtWidgets.QLabel(self)
        self.img_label.setGeometry(10, 80, 780, 500)
        self.img_label.setText("Import an image")
        self.img_label.setStyleSheet("background-color:#5C5C5C; border-radius: 2; color: #333333; font-size: 30pt")
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_blw = QtWidgets.QPushButton("Monochrome", self)
        self.btn_blw.setGeometry(10, 20, 120, 40)
        self.btn_blw.setStyleSheet("border-radius: 5; background-color: #5C5C5C ")
        self.btn_blw.setContentsMargins(5, 5, 5, 5)
        self.btn_blw.clicked.connect(self.clicked_btn)
        self.btn_retro = QtWidgets.QPushButton("Retro", self)
        self.btn_retro.setGeometry(142, 20, 120, 40)
        self.btn_retro.setStyleSheet("border-radius: 5; background-color: #5C5C5C ")
        self.btn_retro.setContentsMargins(5, 5, 5, 5)
        self.btn_retro.clicked.connect(self.clicked_btn)
        self.btn_contrast = QtWidgets.QPushButton("Contrast", self)
        self.btn_contrast.setGeometry(274, 20, 120, 40)
        self.btn_contrast.setStyleSheet("border-radius: 5; background-color: #5C5C5C ")
        self.btn_contrast.setContentsMargins(5, 5, 5, 5)
        self.btn_contrast.clicked.connect(self.clicked_btn)
        self.btn_saturation = QtWidgets.QPushButton("Saturation", self)
        self.btn_saturation.setGeometry(406, 20, 120, 40)
        self.btn_saturation.setStyleSheet("border-radius: 5; background-color: #5C5C5C ")
        self.btn_saturation.setContentsMargins(5, 5, 5, 5)
        self.btn_saturation.clicked.connect(self.clicked_btn)
        self.btn_blurr = QtWidgets.QPushButton("Blurr", self)
        self.btn_blurr.setGeometry(538, 20, 120, 40)
        self.btn_blurr.setStyleSheet("border-radius: 5; background-color: #5C5C5C ")
        self.btn_blurr.setContentsMargins(5, 5, 5, 5)
        self.btn_blurr.clicked.connect(self.clicked_btn)
        self.btn_undo = QtWidgets.QPushButton("Undo", self)
        self.btn_undo.setGeometry(670, 20, 120, 40)
        self.btn_undo.setStyleSheet("border-radius: 5; background-color: #5C5C5C ")
        self.btn_undo.setContentsMargins(5, 5, 5, 5)
        self.btn_undo.clicked.connect(self.clicked_btn)
        self.final_img = None
        self.img = None
        self.fname = None

        # Error box
        self.error = QMessageBox()
        self.error.setWindowTitle("Error")
        self.error.setIcon(QMessageBox.Warning)

        # Action when you close Program
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)

    def open_img(self, path):
        self.final_img = cv2.imread(path)
        pixmap = QPixmap(path)
        pixmap_resized = pixmap.scaled(780, 500, QtCore.Qt.KeepAspectRatio)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setPixmap(pixmap_resized)

    @QtCore.pyqtSlot()
    def menu_action_clicked(self):
        action = self.sender()
        if action.text() == "Open":
            self.fname = QFileDialog.getOpenFileName(self)[0]
            if self.fname.endswith(('.jpg', '.jpeg', '.png')):
                self.img = cv2.imread(self.fname)
                self.open_img(self.fname)
            elif self.fname == '':
                pass
            else:
                self.error.setText("Not valid file               ")
                self.error.setInformativeText("File must have .png, .jpg or .jpeg extentions")
                self.error.exec_()

        elif action.text() == "Save":
            if self.final_img is None:
                self.error.setText("File is not opened       ")
                self.error.setInformativeText("Open the file: File > Open")
                self.error.exec_()
            else:
                save_fname = QFileDialog.getSaveFileName(self)[0]
                if save_fname.endswith(('.jpg', '.jpeg', '.png')):
                    cv2.imwrite(save_fname, self.final_img)
                elif save_fname == '':
                    pass
                else:
                    self.error.setText(" Not valid file name                ")
                    self.error.setInformativeText("Use .png, .jpg or .jpeg extentions\nFile name example: exampl.png")
                    self.error.exec_()

    def clicked_btn(self):
        click = self.sender()
        try:
            match click.text():
                case "Monochrome":
                    img = filters.blw(self.img)
                    cv2.imwrite('.cache/blw.jpg', img)
                    self.open_img('.cache/blw.jpg')
                case "Retro":
                    img = filters.retro(self.img)
                    cv2.imwrite('.cache/retro.jpg', img)
                    self.open_img('.cache/retro.jpg')
                case "Contrast":
                    img = filters.contrast(self.img)
                    cv2.imwrite('.cache/contrast.jpg', img)
                    self.open_img('.cache/contrast.jpg')
                case "Saturation":
                    img = filters.saturation(self.img)
                    cv2.imwrite('.cache/saturation.jpg', img)
                    self.open_img('.cache/saturation.jpg')
                case "Blurr":
                    img = filters.blurr(self.img)
                    cv2.imwrite('.cache/blurr.jpg', img)
                    self.open_img('.cache/blurr.jpg')
                case "Undo":
                    if not self.final_img is None:
                        self.open_img(self.fname)
        except (ValueError, AttributeError, cv2.error):
            self.error.setText("File is not opened       ")
            self.error.setInformativeText("Open the file: File > Open")
            self.error.exec_()

    # When programme closed remove .cache_file directory
    def closeEvent(self, event):
        shutil.rmtree('.cache')


def application():
    app = QApplication(sys.argv)
    window = Window()

    path = ":/icons/logo.png"
    app.setWindowIcon(QtGui.QIcon(path))
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
