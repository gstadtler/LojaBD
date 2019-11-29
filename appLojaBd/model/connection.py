import psycopg2


class Connection():

    def __init__(self, host='localhost', db='LojaBD', user='postgres', password='postgres123'):
        self.conn = psycopg2.connect(host=host, database=db, user=user, password=password)
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)
        
    def execute(self, query, values):
        self.cur.execute(query, values)
    
    def queryResult(self):
        self.result = self.cur.fetchall()
        for row in self.result:
            print(row)
            
    def callProCedure(self,procNome,procValores):
        self.cur.callproc(procNome, procValores)     
              
    def close(self):
        self.cur.close()
        self.conn.close()

# Test
#db = Connection()
#db.query('Select * from cliente')
#db.queryResult()
#db.close()