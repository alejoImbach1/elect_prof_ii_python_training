# Un diccionario asocia llaves con valores

empty_dict = {}

empty_dict_2 = dict()

ages = {
    "Felipe" : 18,
    "Manuel" : 22,
    "Lola" : 35
}

other_ages = dict(
    socio = 3,
    perro = 5,
    maria = 89
)

# print(ages["Felipe"])
# print(other_ages["maria"])

# VERIFICAR la existencia de una llave

# print("socio" in other_ages)
# print("kira" in other_ages)

#Función GET para obtener un valor por defecto

# print(ages.get("Hello"))
# print(ages.get("Hello",'default'))
# print(ages.get("Hello",0))
# print(ages.get("Felipe",0))

#  MODIFICAR O AGREGAR
ages["Felipe"] = 99
ages["Andres"] = 22

# print(ages)

# OTRAS FUNCIONES de los diccionarios

# print(ages.keys())
# print(ages.values())
# print(ages.items())

# print(list(ages.keys()))

#ciclo FOR
# for key in ages:
#     print(key)

# CONJUNTOS
# Colección de elementos distintos

primes_below_ten  = {2,3,5,7,7,}
conjunto_2 = set()

primes_below_ten.add(7)
primes_below_ten.add(8)
# print(primes_below_ten)
print(len(primes_below_ten))

