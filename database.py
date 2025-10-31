import sqlite3
from datetime import datetime

class Database():

    def __init__(self):
        self.conn, self.cur = self.initialize_database()

    def initialize_database(self):
        conn = sqlite3.connect('productivity.db')
        cur = conn.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS productivity(time, activity, context)")
        conn.commit()
        print("Database initialized")
        return conn, cur

    def insert_data(self, data):
        time = datetime.time(datetime.now())
        time_str = time.strftime("%I:%M:%S %p")
        self.cur.execute("INSERT INTO productivity VALUES (?, ?, ?)", (time_str, data[0], data[1]))
        self.conn.commit()

    def query_data_all(self):
        res = self.cur.execute("SELECT * FROM productivity")
        return res.fetchall()

    def clear_database(self):
        self.cur.execute("DROP TABLE IF EXISTS productivity")
        self.conn.commit()

