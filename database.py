import sqlite3

class database:
    def __init__(self, database_file):
        self.database = sqlite3.connect(database_file)