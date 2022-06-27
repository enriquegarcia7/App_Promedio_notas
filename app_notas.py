import os
import funciones_notas as fn 
#---------- VARIABLES ----------
opcion_menu=""
nota_1=0
nota_2=0
nota_3=0
promedio=0
estado=0 #---> Aprobado o Reprobado
#---------- CÓDIGO PRINCIPAL ----------
while True:
    os.system("cls")
    opcion_menu=str(input('''
    =======================APP Notas==========================
    1.- Cargar notas y ver estado
    2.- Ver estadísticas
    3.- Salir                          
                          
    Elija opción:  '''))
    
    if opcion_menu=="1":
        os.system("cls")
        print("\n============CARGAR DATOS==================")
        nota_1=float(input("Nota N° 1: "))
        while not 1<=nota_1<=7:
            print("Error..rango[1 a 7]")
            nota_1=float(input("Nota N° 1: "))
        
        nota_2=float(input("Nota N° 2: "))
        while not 1<=nota_2<=7:
            print("Error..rango[1 a 7]")
            nota_2=float(input("Nota N° 2: "))
        
        nota_3=float(input("Nota N° 3: "))
        while not 1<=nota_3<=7:
            print("Error..rango[1 a 7]")
            nota_3=float(input("Nota N° 3: "))
        # Ahora vamos a llamar a nuestras funciones
        promedio= fn.sacar_promedio(nota_1, nota_2, nota_3)
        estado= fn.determinar_estado(promedio)
        fn.imprimir_reporte(nota_1, nota_2, nota_3)                 
        os.system("pause")

    if opcion_menu=="2":
        os.system("cls")
        print("\n===========ESTADÍSTICAS==========")
        min, max, promedio = fn.sacar_estadisticas(nota_1, nota_2, nota_3)
        print(f'''
        Min {min}   \t   Max {max}   \t   Prom {promedio}              
              ''')        
        os.system("pause")
        
    if opcion_menu=="3":
        break


