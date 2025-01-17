import socket
from flask import Flask, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')

# Initialize MySQL


# Perform database opedockerrations within app context
with app.app_context():
    mysql = MySQL(app)
    cursor = mysql.connection.cursor()
    cursor.execute("SHOW DATABASES")
    
    for database in cursor:
        print(database)
    
    # Closing the cursor
    cursor.close()

@app.route("/data")
def return_hostname():
    return f"This is an example wsgi app served from the {socket.gethostname()} to {request.remote_addr}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
