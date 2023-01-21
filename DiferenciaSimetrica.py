ConjuntoA = {'manzana', 'pera','platano','uva','granadilla','lucuma','mandarina','guanabana','gindon','higo'}
ConjuntoB= {'nuez', 'durazno','kiwi','pera','lucuma','granada','sandia','tuna','uva','cereza','papaya','naranja','fresa','ciruela'}
ConjuntoC= {'pepe','nuez','jorge','maria' ,'durazno','kiwi','oveja','perro','pera'}

diferencia_sime = ConjuntoA.symmetric_difference(ConjuntoB)
diferencia_simetrica= diferencia_sime.symmetric_difference(ConjuntoC)
print('La diferencia simetrica entre los conjuntos A, B, C es: ', diferencia_simetrica)