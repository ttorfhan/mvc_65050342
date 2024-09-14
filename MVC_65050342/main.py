from view.app import MainWindow as AppMainWindow
from PyQt5.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    window = AppMainWindow()
    window.show()
    sys.exit(app.exec_())

# start application
if __name__ == '__main__':
    main()
  

