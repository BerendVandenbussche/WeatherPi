import sqlite3

class database:
    def __init__(self, database_file):
        try:
            self.database = sqlite3.connect(database_file)
            self.cursor = self.database.cursor()
            print('Succesfully connected to database with name {0}!'.format(database_file))
        except:
            print('Could not connect to database with name {0}, does the file exist?'.format(database_file))

    
    def get_data(self, query):
        data = self.cursor.execute(query)
        return data.fetchall()


    def set_data(self, query):
        data = self.cursor.execute(query)
        self.database.commit()
        return data.fetchall()
