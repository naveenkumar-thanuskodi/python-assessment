from flask import Flask, render_template, request
from mysql.connector import connection

app = Flask(__name__, template_folder='template')

DB_CONFIG = {
    'user': 'upfhmbkfgp8uhy4n',
    'password': 'iBSfuqddY4C9di9xQeG0',
    'host': 'bkmvndwo29uc9gnsaz9z-mysql.services.clever-cloud.com',
    'port': 3306,
    'database': 'bkmvndwo29uc9gnsaz9z'
}

@app.route("/book/index", methods=['GET'])
def home():
    return render_template('index.html')

#INSERT
@app.route("/book/insertBook", methods=['GET'])
def insertBookGet():
    return render_template('insert-book.html')


@app.route("/book/insertBook", methods=['POST'])
def insertBookPost():
    insert_book_id = request.form['bookId']
    insert_book_name = request.form['bookName']
    insert_book_author = request.form['bookAuthor']
    insert_book_publisher = request.form['bookPublisher']
    insert_book_cost = request.form['bookCost']
    print('insert_book_id = ', insert_book_id)
    insert_res  = ''

    try:
        db_connection = connection.MySQLConnection(**DB_CONFIG)
        db_cursor = db_connection.cursor()
        insert_sql = "INSERT INTO `book_info` (`book_id`, `book_title`, `book_cost`, `book_author`, `book_publisher`) VALUES ('"+insert_book_id+"', '"+insert_book_name+"', '"+insert_book_author+"', '"+insert_book_publisher+"', '"+insert_book_cost+"');"
        print(insert_sql)
        res = db_cursor.execute(insert_sql)
        db_connection.commit()
        print(res)
        insert_res  = 'Book id (' + insert_book_id + ') inserted sussessfully'
       
    except connection.Error as e:
        insert_res  = 'Error in insert books = ' + insert_book_id
        print("Error insert data to MySQL table", e)
    finally:
        if db_connection.is_connected():
            db_cursor.close()
            db_connection.close()
            print("MySQL connection is closed")

    return render_template('insert-book.html', msg = insert_res)

#DELETE
@app.route("/book/deleteBook", methods=['GET'])
def deleteBookGet():
    return render_template('delete-book.html')


@app.route("/book/deleteBook", methods=['POST'])
def deleteBookPost():
    delete_book_id = request.form['bookId']
    print('deleteBookId = ', delete_book_id)
    delete_res  = ''

    try:
        db_connection = connection.MySQLConnection(**DB_CONFIG)
        db_cursor = db_connection.cursor()
        delete_sql = "DELETE FROM `book_info` WHERE book_id = " + delete_book_id
        print(delete_sql)
        res = db_cursor.execute(delete_sql)
        db_connection.commit()
        print(res)
        delete_res  = 'Book id (' + delete_book_id + ') deleted sussessfully'
       
    except connection.Error as e:
        delete_res  = 'Error in delete books = ' + delete_book_id
        print("Error deleting data from MySQL table", e)
    finally:
        if db_connection.is_connected():
            db_cursor.close()
            db_connection.close()
            print("MySQL connection is closed")

    return render_template('delete-book.html', msg = delete_res)

@app.route("/book/getBooks")
def get_book():
    #print('Naveen')
    #print(request.form)
    try:
        db_connection = connection.MySQLConnection(**DB_CONFIG)
        db_cursor = db_connection.cursor()
        sql_statement = "SELECT * FROM `book_info`"
    
        db_cursor.execute(sql_statement)
    
        output = db_cursor.fetchall()
        
        for x in output:
            print(x)
        
    except connection.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if db_connection.is_connected():
            db_cursor.close()
            db_connection.close()
            print("MySQL connection is closed")
    #return "<p>Python Assessment - Get Books</p>"
    return render_template('get-books.html')
