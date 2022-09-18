import sqlite3


#createConnection() --> return connection
def createConnection():
    con = sqlite3.connect("verge.db")
    return con

#CreateTable(con) --> table create return message
def createTable(con):
    cur = con.cursor()
    cur.execute("CREATE TABLE data(id INT PRIMARY KEY,URL TEXT,headline TEXT,author TEXT,date TEXT)")
#InsertData(data, conc) --> message

def insertData(data,con):
    
    cur = con.cursor()
    cur.execute("""INSERT or IGNORE INTO data  (id,URL, headline, author,date) VALUES(?,?,?,?,?)""",data)
    con.commit()
    #con.close()

def getData(id,con):
    cur = con.cursor()
    cur.execute('SELECT * FROM data WHERE  ID = ' + str(id))
    results = cur.fetchall()
    print(results)

