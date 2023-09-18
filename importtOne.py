import sqlite3 as lite

# functionallity start here

class DatabaseManage(object):
    def __init__(self):
        global conn
        try:
            conn = lite.connect('Courses.db')
            with conn:
                curr = conn.cursor()
                curr.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")



            pass
        except Exception:
            print("Unable to create a DB !")

    def insert_data(self, data):
        pass
    def fetch_data(self):
        pass

    def delete_data(self, id):
        pass


# TODO provide interface

