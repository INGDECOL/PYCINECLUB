from PySide2 import QtWidgets
from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMainWindow

import sys

# import App.views.cineclub_view
from App.views.cineclub_view import CineClubWindow

if __name__ == '__main__':
    # appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    app = QtWidgets.QApplication()
    window = CineClubWindow()
    # window.resize(250, 150)
    window.show()
    app.exec_()
    # exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    # sys.exit(exit_code)
