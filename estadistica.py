import statistics
num_contacts = [
    28,
    595,
    153,
    123,
    270,
    89,
    63,
    50,
    77,
    0
]

# existen las funciones max(), min(), sorted()
# reverse = False by default, means ascending
print(sorted(num_contacts, reverse=True))

# statistics.mean, .median, .mode