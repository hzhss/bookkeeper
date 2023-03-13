from typing import Callable

from bookkeeper.bookkeeper.view.expence_table_view import MainTableWidget
from bookkeeper.bookkeeper.view.categories_view import MainCategoryWidget
from bookkeeper.bookkeeper.view.main_window import MainWindow
from bookkeeper.bookkeeper.view.budget_table_view import BudgetWidget


class PyQtView():

    def __init__(self) -> None:
        self.window = MainWindow()

        self.expense_view = MainTableWidget()
        self.category_view = MainCategoryWidget()
        self.budget_view = BudgetWidget()

        self.window.set_widgets(self.expense_view, self.category_view, self.budget_view)

    def set_budget_data(self, user_data: list[list[str]]) -> None:
        self.budget_view.set_data(user_data)

    def register_budget_update_callback(self, callback: Callable[[str, str], None]) -> None:
        self.budget_view.register_update_callback(callback)

    def set_expense_data(self, user_data: list[list[str]]) -> None:
        self.expense_view.set_data(user_data)

    def set_category_data(self, data: list[list[str]]) -> None:
        self.category_view.set_data(data)
        self.expense_view.set_categories([row[1] for row in data])

    def register_category_add_callback(self, callback: Callable[[str], None]) -> None:
        self.category_view.register_add_callback(callback)

    def register_category_del_callback(self, callback: Callable[[str], None]) -> None:
        self.category_view.register_del_callback(callback)

    def register_expense_add_callback(self, callback: Callable[[dict[str, str]], None]) -> None:
        self.expense_view.register_add_callback(callback)

    def register_expense_del_callback(self, callback: Callable[[list[str]], None]) -> None:
        self.expense_view.register_remove_callback(callback)

    def register_expense_update_callback(self, callback: Callable[[str, dict[str, str]], None]) -> None:
        self.expense_view.register_update_callback(callback)

    def show_main_window(self) -> None:
        self.window.show()

