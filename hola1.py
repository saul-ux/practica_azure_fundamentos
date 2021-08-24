#imprimir nombre
#nombre = input("introduce nombre: ")
#print(f"hola {nombre}")
#print("hola, {}!".format(nombre))

edad = 21

altura = 1.90

booleanos = False

edadString = str(edad)

print(edad + edad)
print(edadString + edadString)

print(type(edad))

tuedad = input("introduce tu edad: ")
tuedad = int(tuedad)

if  tuedad >= 18 and tuedad < 100:
    print("eres mayor de edad")
elif tuedad >= 100:
    print("¿eres inmortal?")
elif tuedad <= 0:
    print("no existes")
else:
    print("eres menor de edad")

for i in range(0, 10):
    print(i)