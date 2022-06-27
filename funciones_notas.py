# Esta librería contendra las 
# funciones requeridas por la
# aplicación app_notas.py
import numpy as np

def sacar_promedio(nota1, nota2, nota3):
    prom=(nota1+nota2+nota3)/3
    return round(prom, 1) #-> 1 decimal

def determinar_estado(prom):
    if prom>=4:
        return "APROBADO"
    else:
        return "REPROBADO"
    
def imprimir_reporte(nota1, nota2, nota3):
    print(f'''
    ============ REPORTE ================
    Nota1:{nota1} \t Nota2:{nota2} \t Nota3:{nota3}
    Promedio:{sacar_promedio(nota1, nota2, nota3)}
    Estado:{determinar_estado(sacar_promedio(nota1, nota2, nota3))}                
          ''')
        
def sacar_estadisticas(nota1, nota2, nota3):
    """ Ingresan 3 notas, retornará la min, max y promedio

    Args:
        nota1 (_float_): valor nota 1
        nota2 (_float_): valor nota 2
        nota3 (_float_): valor nota 3
    """
    
def sacar_estadisticas(nota1, nota2, nota3):
    lista = [nota1, nota2, nota3]
    arreglo = np.array(lista)
    min = arreglo.min()
    max = arreglo.max()
    promedio = round(arreglo.mean(), 2)
    
    return min, max, promedio
    