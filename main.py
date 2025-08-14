# Actividad de galletas
from pruebas import cookies


class Cookie:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        self.cookies = {}

    def info(self):
        print("Informacion de la galleta")
        print("Datos de la galleta\n"
              f"Nombre: {self.name}\n"
              f"Precio: {self.price}\n"
              f"Peso: {self.weight}\n")

    def new(self):
        while True:
            cookie_name = input("Ingresa el nombre de la galleta 🍪: ").lower()
            if cookie_name == "":
                print("Debes ingresar un nombre a la galleta")
            elif cookie_name in self.cookies:
                print("Este nombre ya existe, ingresa un nuevo nombre")
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

    def search(self):
        if not self.cookies:
            print("No se ha encontrado la galleta")
        else:
            for i, cookie in enumerate(self.cookies.values(), start=1):
                print(f"{i}: {cookie.info()}")

    def delete(self):
        if not self.cookies:
            print("No se ha encontrado la galleta")
        else:
            search = input("Ingrese el nombre de la galleta que quieres eliminar: ")
            if search in self.cookies:
                del self.cookies[search]
                print("El galleta eliminado exitosamente")
            else:
                print("No se ha encontrado la galleta")

class ChocOokie(Cookie):
    def __init__(self, name, price, weight, amount):
        super().__init__(name, price, weight)
        self.amount = amount

    def spark(self):
        while True:
            self.amount =  int(input("Ingrese la cantidad de chispas que quiere: "))
            if self.amount <= 0:
                print("Debes ingresar un numero mayor a cero")
            else:
                self.cookies[self.name] = Cookie(self.name, self.amount, self.weight)
                break


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



while True:
    print("Tienda de galletas\n"
          "1. Crear galleta\n"
          "2. Crear galleta con chispas\n"
          "3. Crear galleta con relleno\n"
          "4. Listar galletas\n"
          "5. Buscar galleta\n"
          "6. Eliminar galleta\n"
          "7. Salir\n")
    select = input("Ingrese una de estas opciones: ")
    match select:
        case "1":
            pass
        case "2":
            pass