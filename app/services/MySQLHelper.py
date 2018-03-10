import MySQLdb
import os

MYSQL_HOST      = os.environ['MYSQL_HOST']
MYSQL_DB        = os.environ['MYSQL_DB']
MYSQL_USER      = os.environ['MYSQL_USER']
MYSQL_PASSWORD  = os.environ['MYSQL_PASSWORD']

class MySQLHelper:
    def __init__(self):
        self.db = MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASSWORD,db=MYSQL_DB)
    def save(self):
        cursor = self.db.cursor()
        cursor.execute(self.query, self.data)
        self.db.commit()
        cursor.close()
        self.db.close()
    def getCursor(self):
        cursor = self.db.cursor()
        result = cursor.execute(self.data)
        cursor.close()
        self.db.close()
        return result
