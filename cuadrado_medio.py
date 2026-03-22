import pandas as pd

def generar_numero_pseudo_aleatorios(cantidad_numeros, numero_inicial,cantidad_digitos):
    numero_semilla = numero_inicial
    
    resultados = []
    
    for i in range(cantidad_numeros+1):
        numero_cuadrado = pow(numero_semilla, 2)
        
        numero_cuadrado_str = str(numero_cuadrado)
        longitud = len(numero_cuadrado_str)
        
        inicio = (longitud - cantidad_digitos) // 2
        fin = inicio + cantidad_digitos
        
        numero_nuevo = int(numero_cuadrado_str[inicio:fin])
        
        resultados.append([numero_semilla, numero_cuadrado, numero_nuevo])
        
        numero_semilla = numero_nuevo
    
    df = pd.DataFrame(resultados, columns=["R(n)", "R(n^2)", "Val1"])
    
    print(df)

semilla_inicial =  4567234902 
cantidad_numeros = 50
cantidad_digitos=4

generar_numero_pseudo_aleatorios(cantidad_numeros, semilla_inicial, cantidad_digitos)