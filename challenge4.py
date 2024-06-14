def ordenar_lista(lista):
    return sorted(lista)

entrada = []
cantidad = int(input ("Cuantos numeros ingresas"))

for i in range (cantidad):

    variable = input("Ingrese un numero")

    entrada.append(variable)

print(ordenar_lista(entrada))


