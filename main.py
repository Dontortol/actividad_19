# Actividad de galletas

cookies = []
class Cookie:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def new(self):
        while True:
            cookie_name = input("Ingresa el nombre de la galleta 🍪: ")
            if cookie_name == "":
                print("Debes ingresar un nombre a la galleta")
            else:
                break
        while True:
            try:
                cookie_price = float(input("Ingrese el precio de la galleta 💵: Q. "))
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
                cookie_weight = float(input("Ingrese el peso de la galleta 🏋️: Kg. "))
                if cookie_weight <= 0:
                    print("Debes ingresar un peso mayor a cero")
                else:
                    print("Galleta creada")
                    new_cookie = Cookie(cookie_name, cookie_price, cookie_weight)
                    cookies.append(new_cookie)
                    break
            except ValueError:
                print("Debes ingresar un numero")
            except Exception as e:
                print("Ocurrio un error inesperado", e)

class ChocOokie(Cookie):
    def __init__(self, name, price, weight, amount):
        super().__init__(name, price, weight)
        self.amount = amount

    def info(self):
        print("Datos de la galleta\n"
              f"Nombre: {self.name}\n"
              f"Precio: {self.price}\n"
              f"Peso: {self.weight}\n"
              f"Cantidad de chispas: {self.amount}")