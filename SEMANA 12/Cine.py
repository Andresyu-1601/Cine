asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
print("=== SISTEMA DE RESERVA DE CINE ===")

fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

if 0 <= fila <= 2 and 0 <= columna <= 3:
    if asientos[fila][columna] == 1:
        print("\n¡El asiento ya se encuentra reservado!")
    else:
        asientos[fila][columna] = 1
        print("\n¡Reserva realizada con éxito!")
else:
    print("\nError: Posición fuera de rango. Ingrese valores válidos.")
print("\nEstado de la sala:")
for i in range(len(asientos)):
    for j in range(len(asientos[i])):
        print(asientos[i][j], end=" ")
    print()