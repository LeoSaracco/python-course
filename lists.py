colores = ["Negro", "Blue"]

numbers_list = list((1,2,3,4))
# print(type(numbers_list))
# Mostrar rango
#rango = list(range(1,10+1))
#print(rango)

# Mostrar índice
print(colores[0])
# Si existe
print("Blue" in colores)

# Métodos
colores.append("Dorado")
colores.append("Amarrillo")
# Append con tupla ---> extend
colores.extend(("Naranja","Blanco"))

# Insertar en un índice puntual
colores.insert(1,"Turquesa")

# Eliminar elemento
# Último elemento
colores.pop()
# Elemento
colores.remove("Turquesa")
# Índice
colores.pop(2)
# All
# colores.clear()

# Ordenamiento
colores.sort()
# colores.sort(reverse=True)

# Contar valores
print("Cantidad de color azul: ", colores.count("Blue"))
print(colores)