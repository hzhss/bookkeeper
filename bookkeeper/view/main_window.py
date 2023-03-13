""" Main window"""
from PySide6 import QtWidgets, QtCore
import sys

class MainWindow(QtWidgets.QMainWindow):
    """ Main window класс """

    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent=parent)

        self.setWindowTitle("Bookkeeper Application")
        self.resize(QtCore.QSize(int(0.8 * self.screen().geometry().width()),
                                            int(0.8 * self.screen().geometry().height())))

        self.my_layout = QtWidgets.QVBoxLayout()

        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.my_layout)
        self.setCentralWidget(self.widget)

    def set_widgets(self,
                    exp_wgt: QtWidgets.QWidget,
                    cat_wgt: QtWidgets.QWidget,
                    bgt_wgt: QtWidgets.QWidget) -> None:
        self.my_layout.addWidget(bgt_wgt, stretch=2)
        self.my_layout.addWidget(exp_wgt, stretch=5)
        self.my_layout.addWidget(cat_wgt, stretch=1)
