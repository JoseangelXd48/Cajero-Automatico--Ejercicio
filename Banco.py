"""Creamos un programa de un cajero automático que permita al usuario realizar operaciones básicas como consultar saldo, retirar dinero y depositar dinero. El programa debe manejar un historial de transacciones y permitir al usuario salir del programa de manera segura."""
Cuenta = 0  # Saldo inicial
#usamos el bucle while para que el programa se ejecute hasta que el usuario decida salir
while True:
    print("____Bienvenido:  ¿Que Desea Realizar?: ____")
    print("Depositar:")
    print("Retirar:")
    print("Ver Saldo:")
    print("Salir:")

    Opcion = int(input("¿Que Desea Realizar?: "))
    if Opcion == 1:
        Deposito = int(input("Cuanto Quiere Ingresar a Su Cuenta: "))
        Cuenta += Deposito
        print(f"haz Depositado {Deposito}")
    elif Opcion == 2:
        Retiro = int(input("Cuanto Quiere Retirar de Su Cuenta: "))
        Cuenta -= Retiro
        print(f"Haz Retiraro {Retiro}")
    elif Opcion == 3:
        print(f"Su saldo es: {Cuenta}")
    elif Opcion == 4:
        print("Gracias por utilizar nuestro cajero automático.")
        #Breack rompe el bucle while y sale del programa
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
