# if - else Enteros
x = 1
if x >= 1:
    print("Mayor")
else:
    print("Menor")

# if - else String
color = "Azul"
if color == "Azul":
    print("El color es igual a la variable")
else:
    print("Nada que ver")

# if - else - elif
valor = 22
if valor == 20:
    print("Valor mayor")
elif valor == 22:
    print("Valor es igual")
else:
    print("Valor es menor")

# Anidar if
name = "Leaandro"
lastname = "Saracco"

if name == "Leandro":
    if lastname == "Saracco":
        print("El nombre es correcto")
    else:
        print("El apellido es incorrecto")
else:
    print("El nombre es incorrecto")

# Operadores lógicos
# AND
edad = 12
if edad > 0 and edad < 18:
    print("Es menor de edad")
else:
    print("Es mayor de edad")

# OR
pais = "Argentina"
if pais == "Argentina" or pais == "Uruguay":
    print("Pertenece al Mercosur")
else:
    print("NO pertenece al Mercosur")