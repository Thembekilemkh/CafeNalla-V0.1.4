import pymysql
import pymysql.cursors
import mysql.connector
from mysql.connector import Error

try:
    # Cloud host
    print('Connecting to database')
    db = pymysql.connect(host="mysql-31822-0.cloudclusters.net" ,user="ThembekileNalla", password="Th3mb3k!l3#5",database="CafeNalla", port=31822)
	
    # localhost
    #db = mysql.connector.connect(host="localhost", user="thembekile", password="LlenoCEO#5", database="cafenalla", port="33162")
    print('Getting cursor')
    cursor = db.cursor()

    # Creating tables for our data base
    user_table = """CREATE TABLE user(	
                id INT AUTO_INCREMENT,
                First_Name VARCHAR(100),
                Last_Name VARCHAR(100),
                Email VARCHAR(100),
                Password VARCHAR(100),
                Loyalty_Points FLOAT,
                Regular VARCHAR(150),
                admin INT,
                register_date DATETIME,
                PRIMARY KEY(id));"""

    breakfast_table = """CREATE TABLE breakfast(	
                id INT AUTO_INCREMENT,
                Meal_Name VARCHAR(100),
                Ingredients VARCHAR(100),
                Price VARCHAR(100),
                PRIMARY KEY(id));"""

    meals_table = """CREATE TABLE meals(	
                id INT AUTO_INCREMENT,
                Meal_Name VARCHAR(100),
                Ingredients VARCHAR(100),
                Price VARCHAR(100),
                PRIMARY KEY(id));"""

    salads_table = """CREATE TABLE salads(	
                id INT AUTO_INCREMENT,
                Meal_Name VARCHAR(100),
                Ingredients VARCHAR(100),
                Price VARCHAR(100),
                PRIMARY KEY(id));"""

    smoothies_table = """CREATE TABLE smoothies(	
                id INT AUTO_INCREMENT,
                Meal_Name VARCHAR(100),
                Ingredients VARCHAR(100),
                Price VARCHAR(100),
                PRIMARY KEY(id));"""

    shakes_table = """CREATE TABLE shakes(	
                id INT AUTO_INCREMENT,
                Drink_Name VARCHAR(100),
                Ingredients VARCHAR(100),
                Price VARCHAR(100),
                PRIMARY KEY(id));"""

    cold_drink_table = """CREATE TABLE cold_drink(	
                id INT AUTO_INCREMENT,
                Drink_Name VARCHAR(100),
                Ingredients VARCHAR(100),
                Price VARCHAR(100),
                PRIMARY KEY(id));"""

    orders_table = """CREATE TABLE orders(	
                id INT AUTO_INCREMENT,
                user_id INT,
                Meal_Name VARCHAR(100),
                Meal_Group VARCHAR(100),
                Ingredients VARCHAR(200),
                Status VARCHAR(50),
                collection_date DATETIME,
                order_date DATETIME,
                Meal_Price FLOAT,
                Addon_Price FLOAT,
                Meal_Type VARCHAR(100),
                PRIMARY KEY(id),
                FOREIGN KEY(user_id) REFERENCES user(id));"""

    regulars_table = """CREATE TABLE regulars(	
                id INT AUTO_INCREMENT,
                user_id INT,
                Meal_Name VARCHAR(100),
                Meal_Group VARCHAR(100),
                Ingredients VARCHAR(200),
                creation_date DATETIME,
                PRIMARY KEY(id),
                FOREIGN KEY(user_id) REFERENCES user(id));"""

    tables = [user_table, orders_table, breakfast_table, meals_table,
    		 salads_table, smoothies_table, shakes_table,
    		 cold_drink_table]
    labels = ['User', 'Orders', 'Breakfast', 'Meals', 'Salads', 
              'Smoothies', 'Shakes', 'Cold drink']

    for i in range(len(tables)):
        #cursor.execute(tables[i])
        #db.commit()

        print(f'Commited {labels[i]} table')


    db.close()
except Error as e:
	print(f'Something went wrong: {e}')

'''

import pyodbc


class MssqlConnection(object):
    def __init__(self):
        self.SERVER = "mssql-29978-0.cloudclusters.net"
        self.PORT = 29978
        self.UID = 'Thembekile'
        self.PASSWORD = 'P@$$w0rd'
        self.DATABASE = 'CafeNallaDB'

    def connect_mssql(self):
        conn = False
        try:
            conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=%s,%s;'
                'DATABASE=%s;'
                'UID=%s;'
                'PWD=%s' % (self.SERVER, self.PORT, self.DATABASE, self.UID, self.PASSWORD),
                autocommit=True)
        except Exception as e:
            print(f'There is an exception {e}')
        return conn

    def operate_database(self):
        # example select login user
        connect = self.connect_mssql()
        print('We are connected')
        cursor = connect.cursor()
        #cursor.execute("exec sp_helplogins;")
        #user_list = [i[0] for i in cursor.fetchall()]
        #print(user_list)
        connect.close()


if __name__ == '__main__':
    MssqlConnection().operate_database()'''