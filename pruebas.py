'''
while True:
    n = input("Nombre : ")
    if n == "":
        print("No nombre")
    else:
        print("Nombre agregado")
        break
peso = float(input("Peso empleado: "))
'''
'''
while True:
    cookie_name = input("Ingresa el nombre de la galleta 🍪: ")
    if cookie_name == "":
        print("Debes ingresar un nombre a la galleta")
    else:
        break
while True:
    try:
        cookie_price = float(input("Ingrese el precio de la galleta 💵: "))
        if cookie_price <= 0:
            print("Debes ingresar un precio mayor a cero")
        else:
            break
    except ValueError:
        print("Debes ingresar un numero")
    except Exception as e:
        print("Ocurrio un error inesperado", e)
while True:
    try:
        cookie_weight = float(input("Ingrese el peso de la galleta 🏋️: "))
        if cookie_weight <= 0:
            print("Debes ingresar un peso mayor a cero")
        else:
            print("Galleta creada")
            break
    except ValueError:
        print("Debes ingresar un numero")
    except Exception as e:
        print("Ocurrio un error inesperado", e)
'''

cookies = []
class Cookie:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def info(self):
        print("Nombre de la galleta: ",self.name)
        print("Precio: Q. ",self.price)
        print("Peso: Kg. ",self.weight)

def new():
    while True:
        name = input("Ingresa el nombre de la galleta 🍪: ").lower()
        for c in cookies:
            if c.name in cookies:
                print("Debes ingresar un nombre nuevo")
        if name == "":
            print("Debes ingresar un nombre a la galleta o crear uno nuevo")
        else:
            break
    while True:
        try:
            price = float(input("Ingrese el precio de la galleta 💵: Q. "))
            if price <= 0:
                print("Debes ingresar un precio mayor a cero")
            else:
                break
        except ValueError:
            print("Debes ingresar un numero")
        except Exception as e:
            print("Ocurrio un error inesperado", e)
    while True:
        try:
            weight = float(input("Ingrese el peso de la galleta 🏋️: Kg. "))
            if weight <= 0:
                print("Debes ingresar un peso mayor a cero")
            else:
                print("Galleta creada")
                new_cookie = Cookie(name, price, weight)
                cookies.append(new_cookie)
                break
        except ValueError:
            print("Debes ingresar un numero")
        except Exception as e:
            print("Ocurrio un error inesperado", e)
for a in range(2):
    new()
    for infor in cookies:
        infor.info()