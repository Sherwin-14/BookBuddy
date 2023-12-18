from flask import Flask,request,jsonify
import json
import pymysql

app=Flask(__name__)

def db_connection():
    conn=None
    try:
        conn=pymysql.connect(host='sql12.freesqldatabase.com',
                             database='sql12664909',
                             user='sql12664909',
                             password='RXztZnG4LR',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    except pymysql.Error as e:
        print(e)
    return conn    

@app.route('/books',methods=['GET','POST'])
def books():
    conn=db_connection()
    with conn.cursor() as cursor:
        if request.method=='GET':
                cursor.execute("SELECT * FROM book")
                books=[dict(id=row['id'],author=row['author'],bookname=row['bookname'],genre=row['genre'])
                for row in cursor.fetchall()                
            ]
                
                if books is not None:
                        return jsonify(books)

        if request.method=='POST':
            new_author=request.form['author']
            new_bookname=request.form['bookname']
            new_genre=request.form['genre']
            sql="""INSERT INTO book(author,bookname,genre)
                VALUES (%s,%s,%s)"""
            cursor.execute(sql,(new_author,new_bookname,new_genre))
            conn.commit()
            return f"Book with the id :{cursor.lastrowid} created succesfully"



@app.route('/books/<int:id>',methods=['GET','PUT','DELETE'])
def single_book(id):
    conn=db_connection()
    cursor=conn.cursor()
    if request.method=='GET':
           cursor.execute("SELECT * FROM book WHERE id=%s",(id,))
           rows=cursor.fetchall()
           for r in rows:
                book=r
                if book is not None:
                      return jsonify(book),200
           else:
                return "Something wrong",404     

    if request.method =='DELETE':
        sqle="""DELETE FROM book WHERE id=%s"""
        cursor.execute(sqle, (id,))
        conn.commit()
        return "jello"

    
if __name__=='__main__':
    app.run(debug=True)    


    """if request.method=='PUT':
        for book in books_list:
            if book['author']==author:
                book['author']=request.form['author']
                book['bookname']=request.form['bookname']
                book['genre']=request.form['genre']
                updated_book={
                    'author':book['author'],
                    'bookname':book['bookname'],
                    'genre':book['genre']
                }      
                return jsonify(updated_book)  
         """



