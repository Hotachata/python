# imports
import cmath

# números complejos
def complejo(n):
    x = float(input(f"Parte real del número complejo ({str(n)}): \t"))
    y = float(input(f"Parte imaginaria del número complejo ({str(n)}): \t"))
    return complex(x,y)

# suma
def suma(z1, z2):
    return z1 + z2
# resta
def resta(z1, z2):
    return z1 - z2
# producto
def producto(z1, z2):
    return z1 * z2
# cociente
def cociente(z1, z2):
    return z1 / z2
# potencia
def potencia(z, n):
    return pow(z,n)
# forma polar
def forma_polar(m, t):
    return f"{m:.2f} (cos {t:.2f} + i sen {t:.2f})"
# forma cartesiana
def forma_cartesiana(m, t):
    return cmath.rect(m, t)

while True:
    try:
        switch = int(input("\nIngrese la operación que desea realizar: \n0. Salir\n1. Suma\n2. Resta\n3. Producto\n4. Cociente\n5. Potencia\n6. Forma polar\n7. Forma cartesiana\n"))
        if switch == 1:
            z1 = complejo(1)
            z2 = complejo(2)
            print(f"\nSuma: {suma(z1, z2):.1f}")
        elif switch == 2:
            z1 = complejo(1)
            z2 = complejo(2)
            print(f"Resta: {resta(z1, z2):.1f}")
        elif switch == 3:
            z1 = complejo(1)
            z2 = complejo(2)
            print(f"Producto: {producto(z1, z2):.1f}")
        elif switch == 4:
            z1 = complejo(1)
            z2 = complejo(2)
            print(f"Cociente: {cociente(z1, z2):.1f}")
        elif switch == 5:
            z = complejo(1)
            n = int(input("Ingrese el exponente: "))
            print(f"Potencia: {potencia(z, n):.1f}")
        elif switch == 6:
            z = complejo(1)
            m = abs(z)
            t = cmath.phase(z)
            print(f"Forma polar: {forma_polar(m, t):.1f}")
        elif switch == 7:
            z = complejo(1)
            m = abs(z)
            t = cmath.phase(z)
            print(f"Forma cartesiana: {forma_cartesiana(m, t):.1f}")
        elif switch == 0:
            print("\nSaliendo del programa\n")
            break
        else:
            print("Opción no válida")
    except ValueError as e:
        print(f"Error: {e}")