# seja g:[a,b]->R
# 0. g tem que ser contínua
# 1. g(x)\in [a,b] para todo x\in[a,b] é o mesmo que g([a, b])\subset[a,b]
# 2. |g'(x)| < 1 para todo x\in[a,b]
# f(x) = 0 <--> g(x) = x
import math 

def g(x):
    #return math.log1p(2*x+1)
    #return math.exp(x) - 2*x-1
    return math.sin(x) - 2*x+4
    #return ((math.sin(x)+4)/2)
    #return (x*x+5) ** (1. / 4)

n = 10
a, b = [2,3]
x0 = 2.354233955421625

for i in range(n):
    xn = g(x0)
    x0 = xn
    print("	Iteracao - PF - ",i+1, x0)


"""

  Q2 - 1 - 

  		Ponto Fixo de G(X) - Existente
  			1 3.7318181818181815
			2 2.803789724283025
			3 2.6502053077099683
			4 2.645755053809739
			5 2.645751311067238
			6 2.6457513110645907
			7 2.6457513110645907
			8 2.6457513110645907
			9 2.6457513110645907
			10 2.6457513110645907

		Interação com f(x) - Inf

        Iteracao -  1 -6.937499999359886e-06
        Iteracao -  2 -6.999999999951871
        Iteracao -  3 41.9999999993262
        Iteracao -  4 1756.9999999434008
        Iteracao -  5 3087041.9998011105
        Iteracao -  6 9529828308529.04
        Iteracao -  7 9.081762759004145e+25
        Iteracao -  8 8.247841481083459e+51
        Iteracao -  9 6.802688909708098e+103
        Iteracao -  10 4.6276576402265553e+207
        Iteracao -  11 inf



 Q2 - 2 - 
		
		Ponto Fixo de G(X) - Existente
        Iteracao - PF -  1 2.375
        Iteracao - PF -  2 2.1625692520775623
        Iteracao - PF -  3 2.257326111317677
        Iteracao - PF -  4 2.2080423406119905
        Iteracao - PF -  5 2.2321219398330054
        Iteracao - PF -  6 2.2199536588765794
        Iteracao - PF -  7 2.226004267424049
        Iteracao - PF -  8 2.222970762278171
        Iteracao - PF -  9 2.2244854422393043
        Iteracao - PF -  10 2.2237275869276067
		
		Interação com f(x) - Inf


Q2 - 3 - 
		Ponto Fixo de G(X) - Existente
		Iteracao - PF -  1 2.345207879911715
        Iteracao - PF -  2 2.1657367706679937
        Iteracao - PF -  3 2.2536865222086964
        Iteracao - PF -  4 2.2092740370325825
        Iteracao - PF -  5 2.231369785832444
        Iteracao - PF -  6 2.2202944252640395
        Iteracao - PF -  7 2.2258252168996533
        Iteracao - PF -  8 2.223058101061334
        Iteracao - PF -  9 2.2244412287078688
        Iteracao - PF -  10 2.2237495573498953


		Interação com f(x) - Inf

		Iteracao - PF -  1 -0.003746289900828259
        Iteracao - PF -  2 -11.00000005257801
        Iteracao - PF -  3 -1342.0000190858175
        Iteracao - PF -  4 -2416893802.118612
        Iteracao - PF -  5 -1.4117984606070195e+28
        Iteracao - PF -  6 -2.8139612461836442e+84
        Iteracao - PF -  7 -2.228200852923309e+253
        Iteracao - PF -  8 -inf
        Iteracao - PF -  9 -inf
        Iteracao - PF -  10 -inf


Q2 - 4 - 
		Ponto Fixo de G(X) - Existente
		Iteracao - PF -  1 2.25
        Iteracao - PF -  2 2.2242798353909463
        Iteracao - PF -  3 2.2239801309612304
        Iteracao - PF -  4 2.223980090569316
        Iteracao - PF -  5 2.2239800905693157
        Iteracao - PF -  6 2.2239800905693157
        Iteracao - PF -  7 2.2239800905693157
        Iteracao - PF -  8 2.2239800905693157
        Iteracao - PF -  9 2.2239800905693157
        Iteracao - PF -  10 2.2239800905693157


		Interação com f(x) - Inf
        Iteracao - PF -  1 1.7763568394002505e-15
        Iteracao - PF -  2 -11.0
        Iteracao - PF -  3 -1342.0
        Iteracao - PF -  4 -2416893699.0
        Iteracao - PF -  5 -1.4117982799006626e+28
        Iteracao - PF -  6 -2.8139601656456616e+84
        Iteracao - PF -  7 -2.2281982860918717e+253
        Iteracao - PF -  8 -inf
        Iteracao - PF -  9 -inf
        Iteracao - PF -  10 -inf

Q2 - 5 - 
		Ponto Fixo de G(X) - Existente
		Iteracao - PF -  1 1.8637638298035335
        Iteracao - PF -  2 1.7452839645974174
        Iteracao - PF -  3 1.7030316981118414
        Iteracao - PF -  4 1.687521174796905
        Iteracao - PF -  5 1.6817664529768848
        Iteracao - PF -  6 1.6796228822008357
        Iteracao - PF -  7 1.6788232495846391
        Iteracao - PF -  8 1.6785247926803553
        Iteracao - PF -  9 1.678413373036816
        Iteracao - PF -  10 1.678371774780458


		Interação com f(x) - Sem PF
		Iteracao - PF -  1 1.000083196512716
        Iteracao - PF -  2 -0.2816584035899079
        Iteracao - PF -  3 0.3178481929081638
        Iteracao - PF -  4 -0.2615287488163527
        Iteracao - PF -  5 0.2929312397800674
        Iteracao - PF -  6 -0.24551185510081797
        Iteracao - PF -  7 0.27332771964826974
        Iteracao - PF -  8 -0.23232453298144318
        Iteracao - PF -  9 0.257337893852732
        Iteracao - PF -  10 -0.2211936751232193


Q2 - 6 - 
		Ponto Fixo de G(X) - Existente
		Iteracao - PF -  1 1.7099759466766968
        Iteracao - PF -  2 1.7873574968915917
        Iteracao - PF -  3 1.795395380753263
        Iteracao - PF -  4 1.7962261861600644
        Iteracao - PF -  5 1.7963120153988614
        Iteracao - PF -  6 1.796320881819125
        Iteracao - PF -  7 1.7963217977421984
        Iteracao - PF -  8 1.7963218923592568
        Iteracao - PF -  9 1.7963219021334262
        Iteracao - PF -  10 1.7963219031431215


		Interação com f(x) - Inf
		Iteracao - PF -  1 -1.0096949942806077e-09
        Iteracao - PF -  2 -3.999999998990305
        Iteracao - PF -  3 -63.999999952544336
        Iteracao - PF -  4 -262083.99941691227
        Iteracao - PF -  5 -1.8002031714193194e+16
        Iteracao - PF -  6 -5.83397504910875e+48
        Iteracao - PF -  7 -1.9856088606252662e+146
        Iteracao - PF -  8 -inf
        Iteracao - PF -  9 -inf


Q2 - 7 - 
		Ponto Fixo de G(X) - Existente
		Iteracao - PF -  1 1.5650845800732873
        Iteracao - PF -  2 1.6520821224445132
        Iteracao - PF -  3 1.6673858027473085
        Iteracao - PF -  4 1.6701187325210356
        Iteracao - PF -  5 1.6706080125180693
        Iteracao - PF -  6 1.6706956481193795
        Iteracao - PF -  7 1.670711345904543
        Iteracao - PF -  8 1.6707141578209441
        Iteracao - PF -  9 1.6707146615158304
        Iteracao - PF -  10 1.6707147517420742


		Interação com f(x) - Inf
		Iteracao - PF -  1 -3.0148462393242426e-07
        Iteracao - PF -  2 -5.000000000000091
        Iteracao - PF -  3 595.0000000000443
        Iteracao - PF -  4 125333346595.03735
        Iteracao - PF -  5 2.467553313023455e+44
        Iteracao - PF -  6 3.707372110875494e+177
        Iteracao - PF -  7 inf
        Iteracao - PF -  8 inf
        Iteracao - PF -  9 inf
        Iteracao - PF -  10 inf



Q2 - 8 - 
		Ponto Fixo de G(X) - Existente
        Iteracao - PF -  1 2.454648713412841
        Iteracao - PF -  2 2.3170886197314795
        Iteracao - PF -  3 2.3671055753186523
        Iteracao - PF -  4 2.349674770623528
        Iteracao - PF -  5 2.3558509290474348
        Iteracao - PF -  6 2.353674836932837
        Iteracao - PF -  7 2.354443099310472
        Iteracao - PF -  8 2.3541720582218595
        Iteracao - PF -  9 2.354267704728952
        Iteracao - PF -  10 2.354233955421625


		Interação com f(x) - Sem PF
        Iteracao - PF -  1 2.3817934808878505e-05
        Iteracao - PF -  2 3.999976182065189
        Iteracao - PF -  3 -4.756739290782491
        Iteracao - PF -  4 14.512495267742073
        Iteracao - PF -  5 -24.094603220733017
        Iteracao - PF -  6 53.05066659619395
        Iteracao - PF -  7 -101.75242248339627
        Iteracao - PF -  8 206.5652457209889
        Iteracao - PF -  9 -409.8336780212043
        Iteracao - PF -  10 822.6777295821098


"""