#VECTORES
#Son objetos que se pueden añadir juntos para formar nuevos vectores
#y se pueden multiplicar por "escalares" (números), también para formar nuevos vectores
#Son puntos en algún espacio dimensional finito
#+Utiles para representar datos numéricos

#La forma más sencilla de representar un vector en python es una LISTA

from typing import List

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
