def mostrar_menu():
    print("Seleccione una operación lógica:")
    print("1. AND")
    print("2. OR")
    print("3. NOT")
    print("4. XOR")
    opcion = input("Ingrese el número de la operación: ")
    return opcion

def generar_tabla_and():
    print("\nTabla de verdad - AND")
    print("A | B | A AND B")
    for A in [0, 1]:
        for B in [0, 1]:
            resultado = A and B
            print(f"{A} | {B} |   {resultado}")

def generar_tabla_or():
    print("\nTabla de verdad - OR")
    print("A | B | A OR B")
    for A in [0, 1]:
        for B in [0, 1]:
            resultado = A or B
            print(f"{A} | {B} |  {resultado}")

def generar_tabla_not():
    print("\nTabla de verdad - NOT")
    print("A | NOT A")
    for A in [0, 1]:
        resultado = int(not A)
        print(f"{A} |   {resultado}")

def generar_tabla_xor():
    print("\nTabla de verdad - XOR")
    print("A | B | A XOR B")
    for A in [0, 1]:
        for B in [0, 1]:
            resultado = int(A != B)
            print(f"{A} | {B} |   {resultado}")

def main():
    opcion = mostrar_menu() 

    if opcion == "1":
        generar_tabla_and()
    elif opcion == "2":
        generar_tabla_or()
    elif opcion == "3":
        generar_tabla_not()
    elif opcion == "4":
        generar_tabla_xor()
    else:
        print("Opción no válida. Intente nuevamente.")

main()
