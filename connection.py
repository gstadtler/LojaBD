import psycopg2

#con.commit()

con = psycopg2.connect(host='localhost', database='LojaBD', user='postgres', password='postgres123')
cur = con.cursor()
cur.execute('select * from cliente')
recset = cur.fetchall()
for rec in recset:
    print(rec)
con.close()