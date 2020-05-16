from app import Pasteleria
from atributos_conexion import atributos_conexion

def main():
    aplicacion = Pasteleria(
        atributos_conexion['server'],
        atributos_conexion['password'],
        atributos_conexion['user'],
        atributos_conexion['database']
    )
    continues = True
    while continues:
        print('Enter 1 if you check a product\n' +
            'Enter 2 if you want to add a product\n' +
            'Enter 3 if you want to update a product\n' +
            'Enter 4 if you want to delete a product\n' +
            'Enter 5 if you want close the app')
        option = input('Enter an option: ')        
        if option == '1':
            continues = aplicacion.check_product()
        elif option == '2':
            continues = aplicacion.add_product()
        elif option == '3':
            continues = aplicacion.change_product()  
        
main()
'''
select
insert
update
delete
'''