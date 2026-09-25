# greeting = 'Hello world!\n'
#print(greeting*10)

#this a single line comment

'''
This is a multiple line comment
'''

# number_1 = 5
# number_2 = 7
# sum = number_1 + number_2

# print(f"{number_1} + {number_2} = {sum}")

# for_range = int(input('How many times do you wanna print?\n'))
# print()

# for i in range(1,4,1):
#     print(i)

#NESTED FOR

# for_range = int(input("How many?\n"))
# print()

# for i in range(1,for_range):
#     for n in range(2,10):
#         print(f"{i+1} x {n} = {(i+1)*n}")
#     print()


#LOOP WHILE

# number = 1

# while number != 0:
#     number = int(input("Number?\n"))

# print("\nThe end!")


#WHILE AND CONDITIONAL

# keep_going = True

# while keep_going:
#     nota = float(input("nota?\n"))
#     if nota < 0 or nota > 5:
#         continue
#     elif nota >= 4.5:
#         print("Excellent!")
#     elif nota >= 3:
#         print("Approved!")
#     else:
#         print("Failed!")
    
#     keep_going = False


#FUNCTIONS


# def getSum(a,b):
#     return a+b

# a = int(input("a?\n"))
# b = int(input("b?\n"))

# print(f"la suma es {getSum(a,b)}")

#CREAR UNA FUNCIÓN PARA OBTENER EL VALOR MAYOR DE UN ARRAY

# def getMaxInArray(array):
#     aux = array[0]
#     for i in array:
#         if aux < i:
#             aux = i
#     return aux

# data = list(map(int, input("Ingresa los datos del array separados por ' ': ").split()))

# print(getMaxInArray(data))

#IMPORTACION DE LIBRERÍAS

#librería math

# import math

# radious = int(input('Ingrese el radio: '))

# print(f"El perímetro es: {2*math.pi*radious:.2f}")

# number = int(input('Ingrese un entero: '))

# print(f"Su raíz es {math.sqrt(number):.2f}")

# print(f"Su factorial es {math.factorial(number)}")

# number_2 = float(input('Ingrese un float: '))

# print(f"Su entero más cercano hacia arriba es {math.ceil(number_2)}")

# print(f"Su entero más cercano hacia abajo es {math.floor(number_2)}")