import pandas as pd

def generar_numero_pseudo_aleatorios(numero_inicial,a,c,m,cantidad_numeros):
    numero_actual = numero_inicial
    resultados = []
    for i in range(cantidad_numeros+1):
        numero_operacion = (a*numero_actual+c)
        numero_siguiente = numero_operacion%m
        resultados.append([numero_actual, numero_operacion, numero_siguiente])
  
        numero_actual = numero_siguiente
    df = pd.DataFrame(resultados, columns=["X(n)", "a*X(n)+c", "[a*X(n)+c] mod m"])

    print(df)    
    
    
numero_inicial = 7
a = 1 
c = 7
m = 13
cantidad_numeros = 15

generar_numero_pseudo_aleatorios(numero_inicial,a,c,m,cantidad_numeros)