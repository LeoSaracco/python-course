#String
name = "Leo Saracco"
print(name)

#Upper
print("Uppercase: " + name.upper())

#Lowercase
print("Lowercase: " + name.lower())

#Swapcase
print("Swapcase: " + name.swapcase())

#Capitalize
print("Capitalize: " + name.capitalize())

#Replace
print("Replace: " + name.replace("Leo", "Ricardo"))

#Replace + Upper
print("Replace: " + name.replace("Leo", "Ricardo").upper())

#Count
print(name.count("o"))

#Si comienza la palabra con:
print(name)
print(name.startswith("Leo"))

#Si finaliza la palabra con:
print(name)
print(name.endswith("Gomez"))

#Split
name = "Leo-Saracco"
print(name)
print(name.split("-"))

#Find
name = "Leo Saracco"
print(name.find("a"))

#String Lenght
print(len(name))

#Indice de la letra 'e'
print(name.index('e'))

#Consultar si es número
print(name.isnumeric())

#Consultar si es letra
print(name.isalpha())