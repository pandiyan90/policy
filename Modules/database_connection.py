import mysql.connector as mysql

class DB():
    def __init__(self):
        self.connection = mysql.connect(host="localhost", user="user", password="mindzen", db="gmc_java")
        self.cursor = self.connection.cursor()

    def executeQuery(self, query):
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        return self.result