import pymysql

conn=pymysql.connect(
    host='sql12.freesqldatabase.com',
    db='sql12664909',
    user='sql12664909',
    password='RXztZnG4LR',
    port=3306,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor=conn.cursor()
sql_query="""CREATE TABLE book(
          
       id  integer PRIMARY KEY AUTO_INCREMENT,
       author text NOT NULL,
       bookname text NOT NULL,
       genre text NOT NULL
)"""
cursor.execute(sql_query)
conn.close()