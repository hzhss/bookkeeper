"""Виджет для бюджета"""
import itertools
from typing import Callable

from PySide6 import QtWidgets, QtCore, QtGui


class BudgetWidget(QtWidgets.QWidget):
    """ Виджет для бюджета"""

    def __init__(self, parent: QtWidgets.QWidget | None = None):
        super().__init__(parent=parent)

        self.user_data: list[list[str]]
        self.update_callback: Callable[[str, str], None]
        self.table = QtWidgets.QTableWidget()
        self.set_up_table()

        main_layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel('Мой бюджет')
        label.setFixedHeight(20)
        main_layout.addWidget(label, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(self.table)

        self.table.cellChanged.connect(self._on_cell_changed)

        self.last_clicked_cell: tuple[int, int] = (-1, -1)
        self.table.cellClicked.connect(self._on_cell_clicked)

        self.setLayout(main_layout)

    def _on_cell_clicked(self, row: int, column: int) -> None:
        self.last_clicked_cell = (row, column)

    def _on_cell_changed(self, row: int, column: int) -> None:
        if self.last_clicked_cell == (row, column):
            item = self.table.item(row, column)
            pk = self.user_data[row][0]
            self.last_clicked_cell = (-1, -1)

            if item.text().isdecimal() and float(item.text()) >= 0:
                self.update_callback(pk, item.text())
            else:
                self.update_callback(pk, '0')

    def register_update_callback(self, callback: Callable[[str, str], None]) -> None:
        self.update_callback = callback

    def set_data(self, user_data: list[list[str]]) -> None:
        self.user_data = user_data
        self.table.setRowCount(len(self.user_data))

        n_cols = self.table.columnCount()
        n_rows = self.table.rowCount()

        for row, col in itertools.product(range(n_rows), range(n_cols)):
            item = QtWidgets.QTableWidgetItem(self.user_data[row][col+1])
            if col == 2:  # limit column
                item.setFlags(
                    QtCore.Qt.ItemFlag.ItemIsEditable |
                    QtCore.Qt.ItemFlag.ItemIsSelectable |
                    QtCore.Qt.ItemFlag.ItemIsEnabled)
            else:
                item.setFlags(
                    QtCore.Qt.ItemFlag.ItemIsSelectable |
                    QtCore.Qt.ItemFlag.ItemIsEnabled)
            self.table.setItem(row, col, item)

        # self.table.resizeRowsToContents()

    def set_up_table(self) -> None:
        my_headers = ['Период', 'Расходы за период', 'Лимит', 'Остаток']
        self.table.setColumnCount(len(my_headers))
        self.table.setHorizontalHeaderLabels(my_headers)

        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.setFixedHeight(120)
        self.table.verticalHeader().hide()


