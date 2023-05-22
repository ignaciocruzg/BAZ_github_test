# names = ['Hugo', 'Paco', 'Luis']
# absence = []

# for name in names:
#     # print(name)
#     if name == 'Paco':
#         print(name + " si se encuentra en clase")
#     else:
#         absence.append(name)


# print("\nEsta es la lista de alumnos ausentes")
# print(absence)


# Ciclo while
# i = 1
# while i < 8:
#     print(i)
#     if i == 4:
#         break
#     i += 1


# names = ['Hugo', 'Paco', 'Luis']
# absence = []

# if 'Ignacio' not in names:
#     print("Ignacio no esta en la lista")

# for name in names:
#     if name != 'Paco':
#         absence.append(name)
#     else:
#         print(name + " si se encuentra en clase")

# print(absence)

def evaluacion_edad(edad):
    if edad < 4:
        ticket_price = 0
    elif edad < 18:
        ticket_price = 10
    else:
        ticket_price = 15
    print(ticket_price)


age = int(input("Por favor ingresa la edad: "))
evaluacion_edad(age)
