import cmath

# Usando notación literal
z1 = 3 + 4j
# Usando la función complex
z2 = complex(-2, 5)

print("z1:", z1)         # Imprime: (3+4j)
print("z2:", z2)         # Imprime: (-2+5j)
print("Parte real de z1:", z1.real)
print("Parte imaginaria de z1:", z1.imag)

modulo_1 = abs(z1)          # Calcula el módulo de z1 (distancia al origen)
modulo_2 = abs(z2)          # Calcula el módulo de z2 (distancia al origen)

theta_1 = cmath.phase(z1)    # Calcula la fase (ángulo en radianes)
theta_2 = cmath.phase(z2)    # Calcula la fase (ángulo en radianes)

print(f"Módulo 1: {modulo_1:.2f}, Fase: {theta_1:.2f} rad")
print(f"Módulo 2: {modulo_2:.2f}, Fase: {theta_2:.2f} rad")

suma = z1 + z2         # Suma
resta = z1 - z2        # Resta
producto = z1 * z1     # Multiplicación
cociente = z1 / z2     # División
potencia = pow(z1,2)         # Potencia
potenciaz1 = z1**2

print("Suma:", suma)
print("Resta:", resta)
print("Producto:", producto)
print(f"Cociente: {cociente:.2f}") 

print(f"Potencia: {potencia:.3f}") 
print(f"Potencia: {potenciaz1:.3f}") 

forma_polar1 = f"{modulo_1:.2f} (cos {theta_1:.2f} + i sen {theta_1:.2f})"
print("Forma polar:",forma_polar1)


z_cartesiano1 = cmath.rect(modulo_1, theta_1)
z_cartesiano2 = cmath.rect(modulo_2, theta_2)

print("Forma Cartesiana 1:", z_cartesiano1)
print("Forma Cartesiana 2:", z_cartesiano2)