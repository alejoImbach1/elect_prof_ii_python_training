#VECTORES
#Son objetos que se pueden añadir juntos para formar nuevos vectores
#y se pueden multiplicar por "escalares" (números), también para formar nuevos vectores
#Son puntos en algún espacio dimensional finito
#+Utiles para representar datos numéricos

#La forma más sencilla de representar un vector en python es una LISTA

from typing import List, Tuple
import math

Vector = List[float]

grades = [
    4.5,
    3.8,
    2.3
]

other_grades = [
    2.5,
    4.8,
    3.9
]

#Función para sumar vectores

def add (v1: Vector, v2: Vector) -> Vector:
    assert len(v1) == len(v2), "Different sizes!"
    return [v1_i + v2_i for v1_i, v2_i in zip(v1,v2)]

def substract (v1: Vector, v2: Vector) -> Vector:
    assert len(v1) == len(v2), "Different sizes!"
    return [v1_i - v2_i for v1_i, v2_i in zip(v1,v2)]


# Producto punto
def dot(v1: Vector, v2: Vector) -> float:
    assert len(v1) == len(v2), "Different size!"
    return sum(v1 * v2 for v1, v2 in zip(v1,v2))

# Magnitud de un vector
# def sum_of_squares(v: Vector) -> float:
#     return dot(v, v)

def magnitude(v:Vector) -> float:
    return math.sqrt(dot(v,v))

print(magnitude([3,4]))

# Matrices

matrix = List[List[float]]

# Matriz 2x3
A = [
    [1, 2, 3],
    [4, 5, 6]
]

# Matriz 3x2
B = [
    [4,2],
    [2,1],
    [9,3]
]

def shape(A: matrix) -> Tuple[int,int]:
    n_rows = len(A)
    n_columns = len(A[0])
    return n_rows,n_columns