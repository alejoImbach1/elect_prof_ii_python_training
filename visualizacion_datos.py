from matplotlib import pyplot as plt

#GRÁFICO BÁSICO, f(x)

# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

#Creamos un gráfico lineal, los años en el eje x, gdp en el eje y
# plt.plot(years, gdp, color = 'green', marker = 'o', linestyle='solid')

# #Añadir títulos
# plt.title("Nominal GDP")

# plt.ylabel("Billions of $")
# plt.savefig("figura.jpg")
# plt.show()

#GRÁFICA DE BARRAS

# movies = ["Angie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
# num_oscars = [5, 11, 3, 8, 10]

# "Gráfico de barras con las coordenadas de x a la izquierda [0,1,2,3,4]"
# "Alturas [num_oscars]"

# plt.bar(range(len(movies)), num_oscars)

# plt.title("My Favorite Movies")
# plt.ylabel("# de Distinciones")
# plt.xticks(range(len(movies)),movies)
# plt.show()

#GRÁFICO DE DISPERSIÓN

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
users = ["Juan", "Isabel", "Brayan", "Manuel", "Alejandro",
        "Natalia", "Eynar", "Felipe", "Gabriel"]

plt.scatter(friends, minutes, s=80)

# Agregar etiquetas
for i, user in enumerate(users):
    plt.annotate(
        user,
        (friends[i], minutes[i]),
        xytext=(5, 5),
        textcoords='offset points'
    )

plt.show()