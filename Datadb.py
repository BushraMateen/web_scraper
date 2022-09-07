import sqlite3


#createConnection() --> return connection
def createConnection():
    con = sqlite3.connect("verge.db")
    return con

#CreateTable(con) --> table create return message
def createTable(con):
    cur = con.cursor()
    cur.execute("CREATE TABLE data(id INT primary key,URL TEXT,headline TEXT,author TEXT,date TEXT)")
#InsertData(data, conc) --> message

def insertData(data,con):
    
    cur = con.cursor()
    cur.execute("""INSERT or IGNORE INTO data  (id,URL, headline, author,date) VALUES(?,?,?,?,?)""",data)
    con.commit()
    #con.close()
    cur.execute('''SELECT * FROM data''')
    results = cur.fetchall()
    print(results)

