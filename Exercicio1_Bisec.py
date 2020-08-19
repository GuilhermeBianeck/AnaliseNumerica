# uma função qualquer
def f(x):
    return x ** 5 - 8 * x - 2

# método da bisseção
a, b = [0, 2]
n = 10 # número de iterações
print ("Questao 1 - Número 2 - Método da Bisseção\n")
for i in range(n):
	print ("	Interacao ", i+1)
	print ("	",a ,"+", b,"			= 		", ((a + b)/2))
	print ("	-----------------------")
	print ("	    	2   \n")
	m = (a + b)/2
	if f(m) == 0:
		print('	A raiz é:', m)
	elif f(a) * f(m) < 0: # teorema de Bolzano
		b = m
	else:
		a = m
	print("		Aproximação -", m, f(m),"\n\n\n")


	"""
	Questao 1 - Número 1 - Método da Bisseção

        Interacao  1
         0 + 2                  =                1.0
        -----------------------
                2

                Aproximação - 1.0 -9.0



        Interacao  2
         1.0 + 2                        =                1.5
        -----------------------
                2

                Aproximação - 1.5 -6.40625



        Interacao  3
         1.5 + 2                        =                1.75
        -----------------------
                2

                Aproximação - 1.75 0.4130859375



        Interacao  4
         1.5 + 1.75                     =                1.625
        -----------------------
                2

                Aproximação - 1.625 -3.669036865234375



        Interacao  5
         1.625 + 1.75                   =                1.6875
        -----------------------
                2

                Aproximação - 1.6875 -1.8158159255981445



        Interacao  6
         1.6875 + 1.75                  =                1.71875
        -----------------------
                2

                Aproximação - 1.71875 -0.750956803560257



        Interacao  7
         1.71875 + 1.75                         =                1.734375
        -----------------------
                2

                Aproximação - 1.734375 -0.1816730061545968



        Interacao  8
         1.734375 + 1.75                        =                1.7421875
        -----------------------
                2

                Aproximação - 1.7421875 0.11247894444386475



        Interacao  9
         1.734375 + 1.7421875                   =                1.73828125
        -----------------------
                2

                Aproximação - 1.73828125 -0.03539848984200944



        Interacao  10
         1.73828125 + 1.7421875                         =                1.740234375
        -----------------------
                2

                Aproximação - 1.740234375 0.03833918678932946













	"""