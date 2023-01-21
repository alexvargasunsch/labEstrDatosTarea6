ConjuntoA = {'manzana', 'pera','platano','uva','granadilla','lucuma','mandarina','guanabana','gindon','higo'}
ConjuntoB= {'nuez', 'durazno','kiwi','pera','lucuma','granada','sandia','tuna','uva','cereza','papaya','naranja','fresa','ciruela'}

union = ConjuntoA.union(ConjuntoB)
interseccion = ConjuntoA.intersection(ConjuntoB)
diferenciaA= ConjuntoA - ConjuntoB
diferenciaB= ConjuntoB - ConjuntoA

print ('El conjunto A a es: ', ConjuntoA)
print('El conjunto B a es: ', ConjuntoB)
print('Conjunto A union Conjunto B es: ', union)
print('Cojunto A interseccion Conjunto B es: ', interseccion)
print ('Conjunto A diferencia Conjunto B es: ', diferenciaA)
print('Conjunto B diferenica conjunto A es: ', diferenciaB)

