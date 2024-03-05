número = int(input("Ingresa un número para calcular su factorial: "))
factorial = 1
for i in range(1, número + 1):
    factorial *= i
print("El factorial de", número, "es", factorial)