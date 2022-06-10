from PySide2 import QtWidgets, QtCore

from App.modules.cineclub import Movie, get_movies


class CineClubWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # self.layout = None
        # self.txt_movie_title = None
        # self.btn_add = None
        # self.dgv_data_grid = None
        # self.btn_clear_all = None

        self.setWindowTitle("PyMovie")
        self.setup_ui()
        self.add_widgets()
        self.connect_widgets()
        self.update_ui()
        self.load_movie()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.le_title = QtWidgets.QLineEdit()
        self.btn_add = QtWidgets.QPushButton("Ajouter le film")
        self.lw_movies = QtWidgets.QListWidget()
        self.btn_clear_all = QtWidgets.QPushButton("Supprimer le(s) film(s)")

    def add_widgets(self):
        self.layout.addWidget(self.le_title)
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.lw_movies)
        self.layout.addWidget(self.btn_clear_all)

    def connect_widgets(self):
        self.btn_add.clicked.connect(self.add_movie)
        self.le_title.returnPressed.connect(self.add_movie)
        self.btn_clear_all.clicked.connect(self.remove_movie)

    def update_ui(self):
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)

    @property
    def title(self):
        return self.le_title.text().title()

    def add_movie(self):
        if self.title:
            m = Movie(self.title)
            res = m.add_movies()
            if res:
                self.load_movie()
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Opération réussit")
                msg.setText("Enregistrement effectué succès !")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.exec_()

            self.le_title.clear()

    def load_movie(self):
        movies = get_movies()
        # print(movies)
        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.movie_title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)

    def remove_movie(self):
        for selection in self.lw_movies.selectedItems():
            movie = selection.data(QtCore.Qt.UserRole)
            movie.remove_movie()
            self.lw_movies.takeItem(self.lw_movies.row(selection))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = CineClubWindow()
    win.show()
    app.exec_()
