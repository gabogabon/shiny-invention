print("¡Hola, mundo!")

nombre = input("¿Cómo te llamas? ")
print(f"Mucho gusto, {nombre}!")

# Un pequeño cálculo
numero = int(input("Dame un número: "))
print(f"El doble de {numero} es {numero * 2}")
print(f"El cuadrado de {numero} es {numero ** 2}")

# Un bucle simple
print("\nContando del 1 al 5:")
for i in range(1, 6):
    print(i)