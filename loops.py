comidas = ["Milanesas","Canelones","Fideos"]
print("===== For =====")
# For
for comida in comidas:
    print(comida)

# For - Condicional
for comida in comidas:
    if comida == "Fideos":
        print("No te olvides del queso rayado")
    print(comida)

# For - Condicional - break
for comida in comidas:
    if comida == "Canelones":
        break

# Range
for number in range(1,5):
    print(number)

# Character - String
for letra in "Hola mundo!":
    print(letra)

print("===== While =====")

# While
count = 5
while count <= 10:
    print(count)
    count = count + 1