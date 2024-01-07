import os
import json
import logging


CUR_DIR=os.path.dirname(__file__)
DATA_FILE=os.path.join(CUR_DIR,"data","movies.json")

def get_movies():
    with open(DATA_FILE,"r") as f:
        movies_title=json.load(f)
    
    movies=[Movie(movie_title) for movie_title in movies_title ]
    return movies



class Movie:
    def __init__(self,nom):
        self.nom=nom.title()

    def title(self):
        print(self.nom)

    def __str__(self):
        return f"{self.nom}"
    
    def _get_movies(self):
        with open(DATA_FILE,"r") as f:
            return json.load(f)

    def _write_movies(self,movies):
        with open(DATA_FILE,"w") as f:
            json.dump(movies,f,indent=4)
        
    def add_to_movies(self):
        self.l_movie= self._get_movies()
        if self.nom in self.l_movie:
           logging.warning(f"Le film {self.nom} existe deja dans notre liste !!!") 
           return False
        else:
            self.l_movie.append(self.nom)
            self._write_movies(self.l_movie)
            return True

    def remove_from_movies(self):
        self.movie=self._get_movies()
        if self.nom in self.movie:
            self.movie.remove(self.nom)
            self._write_movies(self.movie)
            return True
        else:
            logging.warning(f"Pas de film de nom {self.nom}")
            return False
        
if __name__=="__main__": 
    m=Movie("germann")
    m.remove_from_movies()
    
    