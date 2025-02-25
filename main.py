import sys
import sqlite3
from PyQt6 import QtWidgets, uic

class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.load_data()
    
    def load_data(self):
        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coffee")
        rows = cursor.fetchall()
        
        for row in rows:
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            for column, value in enumerate(row):
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, column, QtWidgets.QTableWidgetItem(str(value)))
        
        connection.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
