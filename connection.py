from psycopg2 import connect, Error

class Connection:
    def __init__(self, server, password, user, database):
        self.db = connect(
            host = server,
            password = password,
            user = user,
            database = database
        )
        self.cursor = self.db.cursor()

    def execute_sql(self, script_sql, parameters=None, autocommit=True):
        try:
            self.cursor.execute(script_sql, parameters)
            if autocommit:
                self.db.commit()
        except Exception as e:
            print("An error ocurred while executing the statement\n")
            print(e)
            if autocommit:
                self.db.rollback()
    
    def consult_product(self, condition):
        self.execute_sql(
            "SELECT name FROM product WHERE name = (%s);", 
            (condition,)
        )

    def insert_product(self, name, price):
        self.execute_sql(
            "INSERT INTO product(name, price) VALUES(%s, %s);",
            (name, price)
        )
    
    def update_product(self, condition):
        self.execute_sql(
            "UPDATE product SET name =  WHERE name = ;"
        )
            sql_update_query = """Update mobile set price = %s where id = %s"""
            cursor.execute(sql_update_query, (price, mobileId))
            connection.commit()
            count = cursor.rowcount
            print(count, "Record Updated successfully ")


    def delete_product(self, condition):
        self.execute_sql(
            "DELETE product WHERE name = (%s)", 
            (condition,)
        )