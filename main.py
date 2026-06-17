Book Price Finder
-----------------------------------------
A PyQt5 GUI application that connects to a SQLite database (books.db)
to look up a book's price by title, validate quantity input, and
calculate the total amount.

Files:
    book_form.ui   - Qt Designer form
    book_form.py   - Python code generated from book_form.ui (pyuic5)
    books.db       - SQLite database with books table (id, title, author, price)
    main.py        - This file: application logic / event handlers
"""

import sys
import sqlite3

from PyQt5 import QtWidgets, QtGui, QtCore
from book_form import Ui_MainWindow


DB_FILE = "books.db"


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Restrict the Quantity field to integers only
        int_validator = QtGui.QIntValidator(0, 1000000, self)
        self.lineEdit_qty.setValidator(int_validator)

        # Keep track of the currently fetched price (None until found)
        self.current_price = None

        # Connect button signals to slots
        self.btn_find_price.clicked.connect(self.find_price)
        self.btn_find_total.clicked.connect(self.find_total)

    # ------------------------------------------------------------------
    # Event handler: Find Price button
    # ------------------------------------------------------------------
    def find_price(self):
        title = self.lineEdit_title.text().strip()

        if not title:
            QtWidgets.QMessageBox.warning(
                self, "Input required", "Please enter a book title."
            )
            return

        try:
            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            # Case-insensitive exact match on title
            cur.execute(
                "SELECT price FROM books WHERE title = ? COLLATE NOCASE",
                (title,),
            )
            row = cur.fetchone()
            conn.close()
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(
                self, "Database error", f"Could not access database:\n{e}"
            )
            return

        if row is None:
            self.current_price = None
            self.label_price.setText("Rs. 0")
            self.label_total.setText("Rs. 0")
            QtWidgets.QMessageBox.information(
                self, "Not found", "The book is not found."
            )
        else:
            self.current_price = row[0]
            self.label_price.setText(f"Rs. {self.current_price:.2f}")

    # ------------------------------------------------------------------
    # Event handler: Find Total button
    # ------------------------------------------------------------------
    def find_total(self):
        # Require a price to be fetched first
        if self.current_price is None:
            QtWidgets.QMessageBox.information(
                self,
                "Price required",
                "Please find the book's price before calculating the total.",
            )
            return

        qty_text = self.lineEdit_qty.text().strip()

        if not qty_text:
            QtWidgets.QMessageBox.warning(
                self, "Input required", "Please enter a quantity."
            )
            return

        try:
            quantity = int(qty_text)
        except ValueError:
            QtWidgets.QMessageBox.warning(
                self, "Invalid quantity", "Quantity must be a whole number."
            )
            return

        total = self.current_price * quantity
        self.label_total.setText(f"Rs. {total:.2f}")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
