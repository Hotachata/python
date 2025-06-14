from sympy import symbols, integrate, exp, sqrt, pi, pprint # type: ignore

x = symbols('x')

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
            f = (1/((o)*(sqrt(2*pi))))*(exp(-(1/2)*(((x-m)/o)**2))) # type: ignore
            resultado, error = integrate(f, (x, a, b))
            print("Resultado simbólico:")
            pprint(resultado)
            print("\nResultado numérico:")
            print(resultado.evalf())
        if(m < 0 or m == 0):
            print("\nEl valor de m debe ser mayor a 0")
    finally:
        print("\n¿Desea realizar otro cálculo? (s/n)\n")
        respuesta = input()
        if respuesta.lower() != "s":
            break
        