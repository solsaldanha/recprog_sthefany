import psycopg2

class Database:
    def __init__(self, config: dict) -> None:
        self.connect(config)

    def connect(self, config: dict):
        self.conn = None

        try:
            print('Conectando com PostgreSQL...')
            self.conn = psycopg2.connect(**config)

            cur = self.conn.cursor()

            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            db_version = cur.fetchone()
            print(db_version)

            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)