from flask_mysqldb import MySQL
from main import app

# Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '070771'
app.config['MYSQL_DB'] = 'ecommerce'


mysql = MySQL(app)