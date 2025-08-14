# Actividad de galletas

class RegistroDuplicadoError(Exception):
    def __init__(self, name):
        self.name = name
        super().__init__(f"Ya existe una galleta con el nombre {name}")

class Cookie:
    def __init__(self, name, price, weight):
        if not name:
            print("Debes ingresar un nombre, no puede ser vacio")
        if price <= 0:
            print("El precio debe ser mayor a 0")
        if weight <= 0:
            print("El peso debe ser mayor a 0")
        #Estableci los parametros importantes en el constructor
        self.name = name
        self.price = price
        self.weight = weight

    def see_info(self):
        return f"Galleta: {self.name}, Precio: ${self.price:.2f}, Peso: {self.weight}g"

class SparkCookies(Cookie):
    def __init__(self, name, price, weight, amount):
        super().__init__(name, price, weight)
        if amount <= 0:
            print("Debes poner mas de 0 chispas")
        self.amount = amount

    def see_info(self):
        info_base = super().see_info()
        return f"{info_base}, Cantidad de chispas: {self.amount}"

class Stuff:
    def __init__(self, flavour):
        if not flavour:
            print("Debes ingresar un sabor, no puede ser vacio")

        self.flavour = flavour

    def describe_stuff(self):
        return f"Sabor del relleno: {self.flavour}"

class StuffCookie(Cookie, Stuff):
    def __init__(self, name, price, weight, flavour):
        Cookie.__init__(self, name, price, weight)
        Stuff.__init__(self, flavour)

    def see_info(self):
        info_base = Cookie.see_info(self)
        info_stuff = self.describe_stuff()
        return f"{info_base}, {info_stuff}"

def add_cookie():
    while True:
        name = input("Ingresa el nombre de la galleta 🍪: ").lower()
        if not name:
            print("Debes ingresar un nombre")
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
                break
        except ValueError:
            print("Debes ingresar un numero")
        except Exception as e:
            print("Ocurrio un error inesperado", e)
    return name, price, weight

def normal_cookie(cookies):
    name, price, weight = add_cookie()
    for coo in cookies:
        if coo.name == name:
            raise RegistroDuplicadoError(coo.name) # raise se usa para las excepciones
    cookie = Cookie(name, price, weight)
    cookies.append(cookie)
    print("Se ha registrado la galleta")

def add_spark_cookies(cookies):
    while True:
        name, price, weight = add_cookie()
        for c in cookies:
            raise RegistroDuplicadoError(c.name)

    while True:
        try:
            amount = int(input("Ingrese la cantidad de chispas: "))
            if amount <= 0:
                print("Debes ingresar un precio mayor a cero")
            else:
                break
        except ValueError:
            print("Debes ingresar un numero")
        except Exception as e:
            print("Ocurrio un error inesperado", e)

    cookie = SpikeCookie(name, price, weight, amount)
    cookies.append(cookie)
    print("Se ha registrado la galleta con chispas")

def add_stuff_cookies(cookies):
    name, price, weight = add_cookie()
    for c in cookies:
        if c.name == name:
            raise RegistroDuplicadoError(c.name)

    while True:
        flavour = input("Ingrese el sabor del relleno: ")
        if not flavour:
            print("No se puede dejar vacio")
        else:
            break

    cookie = StuffCookie(name, price, weight, flavour)
    cookies.append(cookie)
    print("Se ha registrado la galleta con relleno")

def count_cookies(cookies):
    if not cookies:
        print("No hay galletas")
    else:
        print("Listado de galletas")
        for cookie in cookies:
            print(cookie.see_info())

def search_cookies(cookies):
    if not cookies:
        print("No hay galletas")
    else:
        name = input("Ingrese el nombre de la galleta:").lower()
        found = False
        for cookie in cookies:
            if cookie.name == name:
                print(cookie.see_info())
                found = True
                break
        if not found:
            print("No hay galletas")

def delete_cookies(cookies):
    if not cookies:
        print("No hay galletas")
    else:
        name = input("Ingrese el nombre de la galleta:").lower()
        delete = None
        for cookie in cookies:
            if cookie.name == name:
                delete = cookie
                break

        if delete:
            cookies.remove(delete)
            print("Se ha eliminado la galleta")
        else:
            print("No hay galletas con ese nombre")

def menu():
    cookies = []
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
                normal_cookie(cookies)
            case "2":
                add_spark_cookies(cookies)
            case "3":
                add_stuff_cookies(cookies)
            case "4":
                count_cookies(cookies)
            case "5":
                search_cookies(cookies)
            case "6":
                delete_cookies(cookies)
            case "7":
                print("Saliendo")
                break
            case _:
                print("escoge la opcion que este dentro del rango")
menu()