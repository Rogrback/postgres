from connection import Connection

class Pasteleria:
    def __init__(self, server, password, user, database):
        self.cx = Connection(server, password, user, database)
  
    def check_product(self):
        op = True
        while op:
            name = input('Enter the product name to find: ')
            result = self.cx.consult_product(
              condition=name
            )
            print(result)
            op = input('¿Do you want to check another product? y/n: ').lower()
            if op == 'y':
                op = True 
        return False
    
    def add_product(self):
        name = input('Enter the product name to add: ')
        price = input('Enter the product price to add: ')
        self.cx.insert_product(
            name=name,
            price=price
        )
        print('Added product')
        op = input('¿Do you want to add another product? y/n: ').lower()
        return op == 'y'
    
    def change_product(self):
        pass
        #name = input('Enter the product to change: ')
        #self.update_product()