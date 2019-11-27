import psycopg2


class Connection():

    def __init__(self, host='localhost', database='LojaBD', user='postgres', password='postgres123'):
        self.conn = psycopg2.connect(database=db, user=user)
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)

    def close(self):
        self.cur.close()
        self.conn.close()


db = Connection()
db.query("SELECT * FROM table;")
db.close()

# con.commit()

# con = psycopg2.connect(host='localhost', database='LojaBD', user='postgres', password='postgres123')
# cur = con.cursor()
# cur.execute('select * from cliente')
# recset = cur.fetchall()
# for rec in recset:
#    print(rec)
# con.close()
