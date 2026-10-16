#LISTAS
frutas = ["manzana", "pera", "mango"]

# print(frutas)
# print(frutas[0])  # manzana
#print(frutas[-2]) #Números negativos significan posiciones de derecha a izquierda (a partir de -1)

#reemplazar valores con índice
frutas[2] = "mandarina"

frutas.append("uva")       # Agregar al final

frutas.insert(1, "banana") # Agregar en una posición

frutas.remove("pera")      # Eliminar por valor

frutas.pop()               # Eliminar el último elemento

# print(len(frutas))         # Cantidad de elementos

# for fruta in frutas:
#     print(fruta)

x = [3,4,5,6,7,8,9,10,11,12]

#Sumar valores de una lista (deben ser datos numéricos)
# print(sum(x))

#Obtener partes de listas (slicing)
y = []
y.append(x[:4]) #dede posición 0 hasta antes de posición 7 [3,7)
y.append(x[4:]) #desde posicón 4 hasta final [7,12]
y.append(x[2:6]) #desde posición 2 hasta antes de posición 6 [5,9)
y.append(x[-3:]) #desde posición -3 (u 8) hasta último [10,12]

#Obtener valores con 'paso' (Striding)
y.append(x[:4:2]) #dede posición 0 hasta antes de posición 7 [3,7), pero cada 2
y.append(x[2:8:3]) #desde posición 2 hasta antes de posición 8 [5,11), cada 3
y.append(x[3:-1:2]) #desde posición 3 hasta antes de última [6,12), cada 2
y.append(x[6:2:-1]) #Paso negativo cambia sentido y cambia orden. Desde posición 6 hasta antes de posición 2

for i in range(len(y)):
    print(y[i])