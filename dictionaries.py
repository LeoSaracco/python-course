# Grupo de datos que se agrupan por clave - valor
# Similar a lo que vendría a ser un archivo JSON.
# product = {
#     "description": "Iphone 13",
#     "brand": "Apple",
#     "price": "1000 USD",
#     "weight": 450.3
# }
person = {
    "name": "Max Power",
    "nickname": "Cacho",
    "age": 26,
    "weight": 89.4
}
# Keys
print(person.keys())
# Items
print(person.items())
# Limpiar
# person.clear()

# Se puede anidar listas dentro de un diccionario
product = [
    {
    "description": "Iphone 13",
    "brand": "Apple",
    "price": "1000 USD",
    "weight": 450.3
    },
    {
        "tienda": "Hendel",
        "sede": "San Vicente",
        "stock": True
    }
]
print(product)