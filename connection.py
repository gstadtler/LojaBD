import psycopg2
#sql = "insert into cidade values (default,'São Paulo,'SP')"
#cur.execute(sql)
#con.commit()

con = psycopg2.connect(host='localhost', database='LojaBD', user='postgres', password='postgres123')
cur = con.cursor()
sql = 'create table teste (id serial primary key, nome varchar(100), sobrenome varchar(2))'
cur.execute(sql)
"""
cur.execute('select * from teste')
recset = cur.fetchall()
for rec in recset:
    print(rec)
con.close()
"""