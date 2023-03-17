from functools import reduce

def myFunction(lista):
    impares = list(filter((lambda x: not x%2 == 0), lista))
    print(impares)
    sumatoria = reduce((lambda a, b: a + b), impares)
    print(sumatoria)
    
    
    
lista = [1, 14, 11, 16, 32, 64, 91, 102, 99]
myFunction(lista)