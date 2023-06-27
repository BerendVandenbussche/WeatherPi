import sqlite3

class database:
    def __init__(self, database_file):
        self.database = sqlite3.connect(database_file)
        self.cursor = database.cursor()
        print('Succesfully connected to database with name {0}!'.format(database_file))

    
    def get_data(self, query):
        data = self.cursor.execute(query)
        return data.fetchall()


    def set_data(self):
        data = self.cursor.execute(query)
        self.database.commit()
        return data.fetchall()