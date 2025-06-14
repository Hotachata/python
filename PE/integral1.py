from scipy.integrate import simpson, trapezoid # type: ignore
import numpy as np

def variables():
    a = float(input("\nIngrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    o = float(input("Ingrese el valor de o: "))
    m = float(input("Ingrese el valor de m: "))
    return a, b, o, m

while True:
    try:
        a, b, o, m = variables()
        if m > 0:
            x = np.linspace(a, b, 200)     # 100 puntos entre a y b
            y = (1/((o)*(np.sqrt(2*np.pi))))*(np.exp(-(1/2)*(((x-m)/o)**2))) # type: ignore
            # Regla del trapecio
            integral_trap = trapezoid(y, x)
            # Regla de Simpson
            integral_simps = simpson(y, x)
            print(f"\nRegla del trapecio: {integral_trap}")
            print(f"Regla de Simpson: {integral_simps}")
        if(m < 0 or m == 0):
            print("\nEl valor de m debe ser mayor a 0")
    finally:
        print("\n¿Desea realizar otro cálculo? (s/n)\n")
        respuesta = input()
        if respuesta.lower() != "s":
            break
        