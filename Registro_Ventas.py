from collections import namedtuple
import datetime
import pandas as pd


Ventas = namedtuple("Ventas", ("fecha", "descripcion","descripcionEquipo","cantidad", "precio", "total","nombre"))

lista_ventas = []
DiccionarioVentas = {}

SEPARADOR = ("*" * 80) + "\n"

while True:
    print("\nMENÚ")
    print("1) Agregar servicio")#Registrar servicio
    print("2) Busqueda especifica (por folio)")
    print("3) Consultar  los servicio (por fecha)")
    print("4) Salir")

    respuesta = int(input("Elija una opción: "))

    if respuesta == 4:
        print("Gracias por su compra, buen día")
        break

    if respuesta == 1:
        lista_ventas = []
        while True:
            if DiccionarioVentas.keys():
                clave = max(DiccionarioVentas.keys())+1
            else:
                clave = 1
            DiccionarioVentas[clave] = lista_ventas
            break

        while True:
            diccionario_compras = {}
            agregarArticulo = 1
            while agregarArticulo == 1:
                while True:
                    try:
                        FechaCapturada = input('Digite la fecha inicio (DD-MM-AAAA)): ')
                        fecha =datetime.datetime.strptime(FechaCapturada, '%d-%m-%Y').date()
                        break
                    except ValueError:
                        print('ERROR: Debe digitar una fecha valida con el formato DD-MM-AAAA')

                #fecha = datetime.date.today()
                descripcionServicio = input('Introduce un articulo: ')
                descripcionEquipo = input('Digita la descripcion del equipo: ')
                precio = float(input('Introduce el precio del articulo: '))
                cantidad = float(input('Introduce la cantidad: '))
                nombre=str(input('Digita el nombre del cliente: '))
                total = precio * cantidad
                diccionario_compras[descripcionServicio] = total
                #print(diccionario_compras)
                # Lista
                venta = Ventas(fecha, descripcionServicio, descripcionEquipo, cantidad, precio,total,nombre)
                lista_ventas.append(venta)

                # DiccionarioVentas
                DiccionarioVentas[clave] = lista_ventas
                #print(DiccionarioVentas)
                agregarArticulo = int(
                    input('¿Desea añadir más articulos? \n1)Si \n2)No: '))

            break
            Total=(precio*cantidad)
            _Iva = Total * 0.16
            ptotal = _Iva + Total
            print(f"Total : ${Total}")
            print(f"Total + IVA : ${ptotal}")

    elif respuesta == 2:
        busqueda = int(input("Ingresa la folio a buscar: "))
        #df_diccionario_ventas = pd.DataFrame(diccionario_ventas)
        df_DiccionarioVentas = pd.DataFrame(DiccionarioVentas[busqueda])
        print(df_DiccionarioVentas)

        sumtotal = df_DiccionarioVentas["total"].sum()
        iva = sumtotal * .16
        totaliva = sumtotal + iva
        print(SEPARADOR)
        print(f"Total : ${sumtotal}")
        print(f"Total + IVA : ${totaliva}")

    if respuesta == 3:
        while True:
            try:
                FechaCap = input('Digite la fecha inicio (DD-MM-AAAA)): ')
                fechaProcesada = datetime.datetime.strptime(FechaCap, '%d-%m-%Y').date()
                print("Clave\tFecha servicio\tdescripcionServicio\tdescripcionequipo\tcantidad\tprecio\ttotal\tnombrecliente")
                print("-" * 120)
                for clave, elemento in DiccionarioVentas.items():
                    if elemento[0][0] == fechaProcesada:
                        print(f"{clave}\t{elemento[0][0]}\t{elemento[0][1]}\t{elemento[0][2]}\t{elemento[0][3]}\t{elemento[0][4]}\t{elemento[0][5]}\t{elemento[0][6]}")

                break
            except ValueError:
                print('ERROR: Debe digitar una fecha valida con el formato DD-MM-AAAA')
