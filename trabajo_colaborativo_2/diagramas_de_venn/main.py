# --- Funciones Auxiliares ---

def obtener_digitos_unicos(dni):
    return set(str(dni))

def contar_frecuencias(dni):
    frecuencia = {}
    for digito in str(dni):
        if digito in frecuencia:
            frecuencia[digito] += 1
        else:
            frecuencia[digito] = 1
    return frecuencia

def suma_digitos(dni):
    return sum(int(d) for d in str(dni))

# --- Ingreso de DNIs ---
cantidad = int(input("¿Cuántos DNIs desea ingresar?: "))
dnis = []

for i in range(cantidad):
    dni = input(f"Ingrese el DNI #{i+1}: ")
    while not dni.isdigit():
        dni = input(f"DNI inválido. Ingrese el DNI #{i+1} nuevamente (solo números): ")
    dnis.append(dni)

# --- Generación de conjuntos ---
conjuntos = [obtener_digitos_unicos(dni) for dni in dnis]

# Mostrar conjuntos
for i, c in enumerate(conjuntos):
    print(f"\nConjunto {chr(65 + i)} (DNI {dnis[i]}): {sorted(c)}")

# --- Operaciones entre pares de conjuntos ---
for i in range(cantidad):
    for j in range(i + 1, cantidad):
        a, b = conjuntos[i], conjuntos[j]
        print(f"\nOperaciones entre Conjunto {chr(65+i)} y {chr(65+j)}:")
        print("Unión:", sorted(a | b))
        print("Intersección:", sorted(a & b))
        print("Diferencia (A - B):", sorted(a - b))
        print("Diferencia Simétrica:", sorted(a ^ b))

# --- Frecuencia y suma de dígitos ---
for i, dni in enumerate(dnis):
    print(f"\nFrecuencia de dígitos en DNI {dni} (Conjunto {chr(65 + i)}):")
    frecuencias = contar_frecuencias(dni)
    for digito, cantidad in sorted(frecuencias.items()):
        print(f"  Dígito {digito}: {cantidad} vez/veces")
    print("Suma total de los dígitos:", suma_digitos(dni))

# --- Evaluación de condiciones lógicas ---

# 1. Dígitos comunes en todos los conjuntos
digitos_comunes = set.intersection(*conjuntos)
if digitos_comunes:
    print(f"\nDígito(s) compartido(s) entre todos los conjuntos: {sorted(digitos_comunes)}")
else:
    print("\nNo hay dígitos comunes en todos los conjuntos.")

# 2. Conjuntos con más de 6 elementos
for i, c in enumerate(conjuntos):
    if len(c) > 6:
        print(f"Conjunto {chr(65 + i)} tiene más de 6 elementos → Diversidad numérica alta.")

# 3. Verificar si la intersección entre todos los conjuntos tiene exactamente un elemento
if len(digitos_comunes) == 1:
    print(f"\nDígito representativo del grupo: {list(digitos_comunes)[0]}")

