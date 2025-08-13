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