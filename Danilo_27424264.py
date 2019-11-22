#!/usr/bin/env python3
"""
Proyecto Polinomio de Lagrange.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

def polinomio_lagrange(X, Y):
    """
    Implementa y retorna el Polinomio de Lagrange para las listas X e Y.

    Parámetros:
    X: lista de valores de la variable independiente.
    Y: lista de valores de la variable dependiente.
    """

    if len(X) != len(Y): raise ValueError("Dimensiones diferentes en X e Y.")

    # Ordena el par (x, y) en forma ascendente por x.
    pares = list(zip(X, Y))
    pares.sort(key = lambda x: x[0])
    X, Y  = zip(*pares)
    final=len(X)
    def polinomio(x):
        o=[]
        result=0
        for i in range (final): 
            acum=1  
            for j in range(final):  
                if i != j:
                    acum = (acum * ((x -  X[j])   /  (X [i] - X[j])))  
            o.insert(len(o),acum)
        for k in range(final):
            result = (result + (Y[k]*o[k]))
        return result
    return polinomio

if __name__ == '__main__':
    # Pruebe aquí su Polinomio de Lagrange ...
    X =[2,1,-1]
    Y =[3,-2,1]
    polinomio = polinomio_lagrange (X,Y)
    result = polinomio(2)
    print(result)