from PySide2 import QtWidgets,QtCore
import movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.styles=""
        self.setup_ui()
        self.setWindowTitle("Ciné club")
        self.populate_movies()
        self.isSombre=False
        self.setup_connection()
        
       
        

    def setup_ui(self):
        self.layouts=QtWidgets.QVBoxLayout(self)
        self.line_title=QtWidgets.QLineEdit()
        self.styles=self.line_title.styleSheet()
        self.btn_add_title=QtWidgets.QPushButton("Ajouter un film")
        self.liste_movies=QtWidgets.QListWidget()
        self.liste_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_delete_title=QtWidgets.QPushButton("Supprimer le(s) film(s)")
        self.btn_sombre=QtWidgets.QPushButton("Dark mode")
        self.layouts.addWidget(self.line_title)
        self.layouts.addWidget(self.btn_add_title)
        self.layouts.addWidget(self.liste_movies)
        self.layouts.addWidget(self.btn_delete_title)
        self.layouts.addWidget(self.btn_sombre)
        

        

    def populate_movies(self):
        movies= movie.get_movies()
        for move in movies:
            l_item=QtWidgets.QListWidgetItem(move.nom)
            l_item.setData(QtCore.Qt.UserRole, move)
            self.liste_movies.addItem(l_item)
    def setup_connection(self):
        self.btn_add_title.clicked.connect(self.add_movie)
        self.btn_delete_title.clicked.connect(self.remove_movie)
        self.line_title.returnPressed.connect(self.add_movie)
        self.btn_sombre.clicked.connect(self.is_dark)

    def is_dark(self):
        if self.isSombre==True:
            self.isSombre=False
            self.setup_css_1()
            print("faux")
        else:
            self.isSombre=True 
            self.setup_css() 
            self.btn_sombre.setText("light mode")
            print("true")

    def add_movie(self):
        title=self.line_title.text()
        if not title:
            return False
        move=movie.Movie(nom=title)
        test=move.add_to_movies()
        if test:
            l_item=QtWidgets.QListWidgetItem(move.nom)
            l_item.setData(QtCore.Qt.UserRole, move)
            self.liste_movies.addItem(l_item)
            
        self.line_title.setText("")

    def remove_movie(self):
        for selected_item in self.liste_movies.selectedItems():
            #move=selected_item.film
            move=selected_item.data(QtCore.Qt.UserRole)
            move.remove_from_movies()
            self.liste_movies.takeItem(self.liste_movies.row(selected_item))
    def setup_css_1(self):
        self.setStyleSheet("""""")
        self.btn_sombre.setText("dark mode")


    def setup_css(self):
        self.setStyleSheet("""
        background-color:rgb(30,30,30);
        color:rgb(240,240,240);
        
        """)
        
        
    
app=QtWidgets.QApplication([])
win=App()
win.show()
app.exec_()