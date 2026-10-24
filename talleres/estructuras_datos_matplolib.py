# Taller: Estructuras de datos y uso de Matplotlib en Python
# Nota: el archivo taller.md no incluye una lista adjunta con los nombres de todos
# los compañeros del curso. Por eso se usan los nombres del ejemplo del taller.
# Reemplaza o completa la lista "estudiantes" con los nombres reales de tu curso.
# Las horas y las notas son valores hipotéticos para fines académicos.

import matplotlib.pyplot as plt

# A) Crear las tres listas

estudiantes = ["Ana", "Carlos", "Laura", "Mateo", "Sofía", "Juan"]
horas = [4, 7, 3, 8, 6, 2]
notas = [3.5, 4.2, 3.0, 4.5, 4.0, 2.8]

# B) Calcular estadísticas a partir de las listas

promedio_notas = sum(notas) / len(notas)
promedio_horas = sum(horas) / len(horas)
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)

# El índice de la nota máxima permite encontrar el nombre correspondiente.
indice_mejor_nota = notas.index(nota_mas_alta)
mejor_estudiante = estudiantes[indice_mejor_nota]

# Se considera aprobada una nota mayor o igual a 3.0.
nota_minima_aprobacion = 3.0

cantidad_aprobados = sum(1 for nota in notas if nota >= nota_minima_aprobacion)

print("=== PUNTO B ===")
print(f"Promedio de las notas: {promedio_notas:.2f}")
print(f"Promedio de horas de estudio: {promedio_horas:.2f}")
print(f"Nota más alta: {nota_mas_alta:.2f}")
print(f"Nota más baja: {nota_mas_baja:.2f}")
print(f"Estudiante con la nota más alta: {mejor_estudiante}")
print(f"Estudiantes aprobados (nota >= {nota_minima_aprobacion:.1f}): {cantidad_aprobados}")

# C) Crear y recorrer un diccionario de estudiantes y notas

notas_estudiantes = dict(zip(estudiantes, notas))

# 1. Mostrar la nota de un estudiante determinado.
estudiante_consultado = "Carlos"
if estudiante_consultado in notas_estudiantes:
    print(f"\nNota de {estudiante_consultado}: {notas_estudiantes[estudiante_consultado]:.2f}")
else:
    print(f"\nEl estudiante {estudiante_consultado} no está en el diccionario.")

# 2. Recorrer el diccionario con un ciclo for.
print("\nNotas de todos los estudiantes:")
for estudiante, nota in notas_estudiantes.items():
    print(f"{estudiante}: {nota:.2f}")

# 3. Mostrar solo quienes obtuvieron una nota >= 4.0.
print("\nEstudiantes con nota mayor o igual a 4.0:")
for estudiante, nota in notas_estudiantes.items():
    if nota >= 4.0:
        print(f"{estudiante}: {nota:.2f}")

# D) Gráficos con Matplotlib

# 1. Gráfico de barras: compara la nota obtenida por cada estudiante.
plt.figure(figsize=(9, 5))
plt.bar(estudiantes, notas, color="cornflowerblue")
plt.title("Nota obtenida por estudiante")
plt.xlabel("Estudiantes")
plt.ylabel("Nota")
plt.ylim(0, 5)
plt.grid(axis="y", linestyle="--", alpha=0.4)

# 2. Gráfico de dispersión: relaciona las horas de estudio con las notas.
plt.figure(figsize=(8, 5))
plt.scatter(horas, notas, color="darkorange", s=80)
plt.title("Horas de estudio frente a nota")
plt.xlabel("Horas de estudio semanal")
plt.ylabel("Nota")
plt.ylim(0, 5)
plt.grid(True, linestyle="--", alpha=0.4)

# Agregar etiquetas
for i, estudiante in enumerate(estudiantes):
    plt.annotate(
        estudiante,
        (horas[i], notas[i]),
        xytext=(5, 5),
        textcoords='offset points'
    )

plt.show()

# E) Respuestas

# 1. ¿Los estudiantes que estudian más horas parecen obtener mejores notas?
#    En general, sí: Mateo estudia 8 horas y obtiene 4.5, y Carlos estudia
#    7 horas y obtiene 4.2.
#
# 2. ¿Qué estudiante obtuvo el mejor resultado?
#    Mateo, con una nota de 4.5.
#
# 3. ¿Cuántos estudiantes tienen una nota igual o superior a 4.0?
#    Tres estudiantes: Carlos (4.2), Mateo (4.5) y Sofía (4.0).
#
# 4. ¿Qué información permite identificar más fácilmente el gráfico de barras?
#    Permite comparar directamente las notas de cada estudiante e identificar
#    con facilidad la nota más alta y la más baja.
#
# 5. ¿Qué información permite observar el gráfico de dispersión?
#    Permite observar la relación entre las horas de estudio semanal y las
#    notas, y reconocer si una mayor cantidad de horas parece asociarse con
#    notas más altas.
