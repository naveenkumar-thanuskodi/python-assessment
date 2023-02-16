from flask import Flask
from mysql.connector import connection

app = Flask(__name__)

DB_CONFIG = {
    'user': 'upfhmbkfgp8uhy4n',
    'password': 'iBSfuqddY4C9di9xQeG0',
    'host': 'bkmvndwo29uc9gnsaz9z-mysql.services.clever-cloud.com',
    'port': 3306,
    'database': 'bkmvndwo29uc9gnsaz9z'
}

@app.route("/book/home")
def home():
    print("Naveen home")
    return "<p>Python Assessment - Book Store24dsdsdfd563</p>"

@app.route("/book/getBooks")
def get_book():
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
    return "<p>Python Assessment - Get Books</p>"
