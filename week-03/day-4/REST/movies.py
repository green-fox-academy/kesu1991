import json

class MovieCollection:

    def __init__(self, database):
        self.database = database
        self.list_data = []
        self.list_single = []

    def list_movie(self):
        with open(self.database, 'r') as fp:
            obj = json.load(fp)
            for p in obj['movies']:
                #print('ID: ' + p['id'])

                self.list_data.append({
                    'id': p['id'],
                    'title': p['title'],
                    'year': p['year'],
                    'genre': p['genre'],
                    'description': p['description']})
                
            return self.list_data

    def read_movie(self,movie_id):
        with open(self.database, 'r') as fp:
            obj = json.load(fp)
            for p in obj['movies']:
                #print('ID: ' + p['id'])
                if p['id'] == movie_id:
                        self.list_single = ({
                        'id': p['id'],
                        'title': p['title'],
                        'year': p['year'],
                        'genre': p['genre'],
                        'description': p['description']})
            return self.list_single
            

    def add_movie(self,titles,years,genres,descriptions):

        self.list_data.append({
            'title': titles,
            'year': years,
            'genre': genres,
            'description': descriptions})
        
        return self.list_data

#c = MovieCollection("movie.json")
#print(c.read_movie("2"))
#print(c.add_movie("a","b","c","d"))


