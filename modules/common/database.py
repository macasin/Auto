import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(r'C:\\Users\\arsen\\Desktop\\QA\\Automation\\become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")
        return record  # Ensure that the record is returned
    
    def get_allUsers(self):
        query= "SELECT name,address,city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_UserAddressAndCityByName(self,name):
        query= f"SELECT city, address FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def change_productsQuantityByID(self,qnt,product_id):
        query= f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit() #accepted the changes

    def get_showTheChangesInProductByID(self,product_id):
        query=f"SELECT quantity from products WHERE id = {product_id}"
        self.cursor.execute(query)
        record=self.cursor.fetchall()
        return record

    def add_newProduct(self,product_id,name,description,quantity):
        query=f"INSERT INTO products (id,name,description,quantity) VALUES ({product_id},'{name}','{description}','{quantity}')"
        self.cursor.execute(query)
        self.connection.commit
