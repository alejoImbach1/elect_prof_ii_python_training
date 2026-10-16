# LAS TUPLAS SON LOS 'PRIMOS' INMUTABLES DE LAS LISTAS
# CASI TODO lo que se hace con listas menos modificar,
# se puede hacer con las tuplas

tuple_1 = (1,2,5,2,5,2)
tuple_2 = 3,4

list_1 = [3,4,2]

# print(tuple_1[1:3])
# print(tuple_1[2])

#TUPLAS son una forma convenicente de retornar múltiples
# valores de una función

def sum_and_product(x, y):
    return (x + y), (x*y)

output = sum_and_product(3,5)

# print(output)

# Las tuplas (y las listas) se pueden usar para ASIGNACIONES MÚLTIPLES

x,y = 4,2
(x_1,y_2) = (7,9)
# print(f"{x} , {y}")
# print(f"{x_1} , {y_2}")

# PRÁCTICA
# Probar las funcionalidades de las listas con las tuplas