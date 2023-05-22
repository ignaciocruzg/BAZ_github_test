# Datos del usuario
# edad = 33
# nombre = 'Ignacio'
# apellido = 'de la Cruz'
# print(nombre, apellido, edad)

# Operaciones basicas
# x = 10
# y = 20
# print("\nEstas son operaciones aritmeticas")
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y)

# Operador de modulo
# print("\nEsto es la utilizacion del operador de modulo")
# print(15 % 3)


# Estructuras de datos
# nombres_baz = ['Ricardo', 'Bety', 'Roberto', 'Carlos', 'Gonzalo', 'Leti', 'Lore']
# nuevos_nombres = []
# print(nombres_baz)

# Indices
# print(nombres_baz[2])

# Slices
# print(nombres_baz[0:3])
# print(nombres_baz[0:6:2])


# Añadir valores a una lista
# nuevos_nombres.append('Lucia')
# print(nuevos_nombres)


# Tuplas
# nombres_estudiantes = ('Hugo', 'Paco', 'Luis')
# print(nombres_estudiantes)
# print(nombres_estudiantes[1])


# Diccionarios
carros = {
    'carro_01':{
        'marca': 'Toyota',
        'Modelo': 2018,
        'Motor': 'Electrico'
    },
    'carro_02':{
        'marca': 'Nissan',
        'Modelo': 2020,
        'Motor': 'Gasolina'
    },
    'carro_03':{
        'marca': 'BMW',
        'Modelo': 2023,
        'Motor': 'Hibrido'
    }
}

# print(carros)
print(carros['carro_02']['marca'])
print(carros['carro_03']['Motor'])

# Metodos de los diccionarios

# print("Metodos de los diccionarios")
# print(carros.keys())
# print(carros.values())
# print(carros.items())
