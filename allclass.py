import sqlite3
path = "./datamayhoc.db"
conn = sqlite3.connect(path)
c = conn.cursor()
ids = "1"
cau = "tôi là trí"
vingu = 'là trí'
chungu = 'tôi'
danhtu = 'tôi và trí'
tinhtu = 'none'
dongtu = 'none'
query = "INSERT INTO data VALUES ('"+ids+"','"+cau+"','"+chungu+"','"+vingu+"','"+danhtu+"','"+tinhtu+"','"+dongtu+"')"
c.execute(query)
conn.commit()
conn.close()
