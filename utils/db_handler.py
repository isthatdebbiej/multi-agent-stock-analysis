import psycopg2

class DBHandler:
    def __init__(self, db_url):
        self.db_url = db_url

    def get_connection(self):
        return psycopg2.connect(self.db_url)

    def close(self):
        if self.conn:
            self.conn.close()
