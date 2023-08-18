edad=int(input("Ingrese la edad "))
nombreUsuario=input("Ingrese el nombre ")

if edad>0 and edad<=15:
    print(f"Querido{nombreUsuario} se encuenta en el rango de niño")
elif edad>15 and edad<=28:
    print(f"Querido {nombreUsuario}, se encuentra en el rango de joven")
elif edad>28 and edad<=60:
    print(f"Querido {nombreUsuario}, se encuentra en el rango de adulto")
elif edad>60 and edad<110:
    print(f"Querido {nombreUsuario}, se encuentra en el rango Sugar")
else:
    print("edad invalida")
