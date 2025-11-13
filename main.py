num1_str= input()

num2_str= input()


num1 = int(num1_str)
num2 = int(num2_str)

resultado = num1 + num2
print(resultado)





def calculadora_avanzada():
    print("\nSeleccione una operación o escriba 'salir':")
    print("1: Suma (a + b)")
    print("2: Resta(a - b)")
    print("3: Multiplicación (a * b)")
    print("4: División (a / b)")
    print("5: Módulo (a % b)")

    opcion = input("Opcion: ")

    if opcion.lower() == 'salir':
        print("¡Hasta luego!")
        break

    try:
        num_a = float(input("Ingrese el primer número (a):"))
        num_b = float(input("Ingrese el segubdo número (b):"))
    except ValueError:
        print("Error: Ingrese números válidos.")
        continue



    if opcion == '1':
        resultado = num_a + num_b
        print(f"Resultado: {num_a} + {num_b} = {resultado}")

    elif opcion == '2':
        resultado = num_a - num_b
        print(f"Resultado: {num_a} - {num_b} = {resultado}")

    else:
        print("Opción no valida. Intente de nuevo.")



        def suma_tres():
    print("\n--- Suma de Tres Números ---")
    try:
        n1 = float(input("Nro 1: "))
        n2 = float(input("Nro 2: "))
        n3 = float(input("Nro 3: "))
        print(f"Resultado: {n1} + {n2} + {n3} = {n1 + n2 + n3}")
    except ValueError:
        print("Error: Ingrese números válidos.")




        def combinacion_operaciones():
    print("\n--- Combinación de Operaciones ---")
    print("Ejemplo: 2 + 4 * 3 / 2 - 1")
    
    expresion = input("Ingrese la expresión a calcular: ")
    
    try:
        # La función eval() toma la cadena y calcula el resultado.
        resultado = eval(expresion)
        print(f"El resultado de '{expresion}' es: {resultado}")
    except Exception as e:
        print(f"Error al evaluar la expresión: {e}")