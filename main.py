# Actividad de galletas


class Cookie:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def info(self):
        print("Informacion de la galleta")
        print("Datos de la galleta\n"
              f"Nombre: {self.name}\n"
              f"Precio: {self.price}\n"
              f"Peso: {self.weight}\n")

class AddCookies:
    def __init__(self):
        self.cookies = {}
    def new(self):
        while True:
            cookie_name = input("Ingresa el nombre de la galleta 🍪: ")
            if cookie_name == "":
                print("Debes ingresar un nombre a la galleta")
            elif cookie_name in self.cookies:
                print("Debes ingresar un nombre a la galleta")
            else:
                break
        while True:
            try:
                cookies_price = float(input("Ingrese el precio de la galleta 💵: Q. "))
                if cookies_price <= 0:
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
                    self.cookies[cookie_name] = Cookie(cookie_name, cookies_price, cookie_weight)
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

class CookieStuff:
    def __init__(self, stuff):
        self.stuff = stuff

    def stuff_flavor(self):
        self.stuff = input("Ingrese el sabor de la galleta: ")

class CrambleCookies(Cookie, CookieStuff):
    def info(self):
        print("Datos de la galleta\n"
              f"Nombre: {self.name}\n"
              f"Precio: {self.price}\n"
              f"Peso: {self.weight}\n"
              f"Cantidad de chispas: {self.stuff}")