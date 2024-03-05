# Inicio

# Leer un número desde el usuario y almacenarlo en la variable "number".
número = int(input("Ingresa un número para calcular su factorial: "))
# Inicializar la variable "factorial" en 1.
factorial = 1
# Para cada valor "i" en el rango desde 1 hasta el número ingresado por el usuario:
for i in range(1, número + 1):
    # Multiplicar "factorial" por "i" y almacenar el resultado en "factorial".
    factorial *= i
# Escribir "El factorial de" seguido del número ingresado por el usuario y luego "es" seguido del valor de "factorial".
print("El factorial de", número, "es", factorial)

# Fin