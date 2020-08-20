import math


def F1(x0, h, f):
    return (f(x0) - f(x0 - h)) / h


def F2(x0, h, f):
    return (f(x0 + h) - f(x0 - h)) / 2*h


def F3(x0, h, f):
    return (f(x0 - 2*h) - 8*f(x0 - h) + 8*f(x0 + h) - f(x0 + 2*h)) / (12 * h)


hs = [.1, .05, .025, .0125]

x0 = 1  # p


def f1(x):
    return math.cos(x**x)


def f2(x):
    return math.sin(x)


def f3(x):
    return x**math.cos(x)


def f4(x):
    return math.exp(-x**2)


print('Questão 8 - EX - 1)')

for h in hs:
    print(' Aproximacao F1 com H =', h)
    print(" ",F1(x0, h, f1))
print()
for h in hs:
    print(' Aproximacao F2 com h =', h)
    print(F2(x0, h, f1))
print()
for h in hs:
    print(' Aproximacao F3 com h =', h)
    print(F3(x0, h, f1))

print('\nQuestão 8 - EX - 2)')

for h in hs:
    print(' Aproximacao F1 com h =', h)
    print(F1(x0, h, f2))
print()
for h in hs:
    print(' Aproximacao F2 com h =', h)
    print(F2(x0, h, f2))
print()
for h in hs:
    print(' Aproximacao F3 com h =', h)
    print(F3(x0, h, f2))

print('\nQuestão 8 - EX - 3)')

for h in hs:
    print(' Aproximacao F1 com h =', h)
    print(F1(x0, h, f3))
print()
for h in hs:
    print(' Aproximacao F2 com h =', h)
    print(F2(x0, h, f3))
print()
for h in hs:
    print(' Aproximacao F3 com h =', h)
    print(F3(x0, h, f3))

print('\nQuestão 8 - EX - 4)')

for h in hs:
    print(' Aproximacao F1 com h =', h)
    print(F1(x0, h, f4))
print()
for h in hs:
    print(' Aproximacao F2 com h =', h)
    print(F2(x0, h, f4))
print()
for h in hs:
    print(' Aproximacao F3 com h =', h)
    print(F3(x0, h, f4))

# import sympy as sy

# x = sy.Symbol('x')
# string = 'x ** x'
# f = sy.sympify(string)
# df = sy.diff(f, x, 2).subs(x, x0)
# print('exact:', df.evalf())


"""

Questão 8 - EX - 1)
 Aproximacao F1 com H = 0.1
  -0.7381240949060053
 Aproximacao F1 com H = 0.05
  -0.7878935990431524
 Aproximacao F1 com H = 0.025
  -0.8141874565698748
 Aproximacao F1 com H = 0.0125
  -0.8277032149599695

 Aproximacao F2 com h = 0.1
-0.008496589053044502
 Aproximacao F2 com h = 0.05
-0.002108804363901572
 Aproximacao F2 com h = 0.025
-0.0005262399402257812
 Aproximacao F2 com h = 0.0125
-0.00013149987951936864

 Aproximacao F3 com h = 0.1
-0.8415612982761268
 Aproximacao F3 com h = 0.05
-0.8414760256460218
 Aproximacao F3 com h = 0.025
-0.8414712906281226
 Aproximacao F3 com h = 0.0125
-0.841471003778195

Questão 8 - EX - 2)
 Aproximacao F1 com h = 0.1
0.5814407518041309
 Aproximacao F1 com h = 0.05
0.5611096003704552
 Aproximacao F1 com h = 0.025
0.5507638656255542
 Aproximacao F1 com h = 0.0125
0.5455473607818373

 Aproximacao F2 com h = 0.1
0.0053940225216976
 Aproximacao F2 com h = 0.05
0.0013501930201160806
 Aproximacao F2 com h = 0.025
0.00033765376633544675
 Aproximacao F2 com h = 0.0125
8.442003681336172e-05

 Aproximacao F3 com h = 0.1
0.5403005070032606
 Aproximacao F3 com h = 0.05
0.540302193338656
 Aproximacao F3 com h = 0.025
0.5403022988334759
 Aproximacao F3 com h = 0.0125
0.540302305428446

Questão 8 - EX - 3)
 Aproximacao F1 com h = 0.1
0.6339453451314703
 Aproximacao F1 com h = 0.05
0.5879145857912582
 Aproximacao F1 com h = 0.025
0.564283765667799
 Aproximacao F1 com h = 0.0125
0.552334003349344

 Aproximacao F2 com h = 0.1
0.005378749671497829
 Aproximacao F2 com h = 0.05
0.0013492344380143491
 Aproximacao F2 com h = 0.025
0.0003375937918925959
 Aproximacao F2 com h = 0.0125
8.441628742492102e-05

 Aproximacao F3 com h = 0.1
0.5402663631130586
 Aproximacao F3 com h = 0.05
0.5403000445577247
 Aproximacao F3 com h = 0.025
0.5403021643022908
 Aproximacao F3 com h = 0.0125
0.5403022970166111

Questão 8 - EX - 4)
 Aproximacao F1 com h = 0.1
-0.7697862505149877
 Aproximacao F1 com h = 0.05
-0.7535012778375649
 Aproximacao F1 com h = 0.025
-0.7447977865208766
 Aproximacao F1 com h = 0.0125
-0.7403184552503506

 Aproximacao F2 com h = 0.1
-0.007333039339652689
 Aproximacao F2 com h = 0.05
-0.0018378639929664986
 Aproximacao F2 com h = 0.025
-0.0004597534935440434
 Aproximacao F2 com h = 0.0125
-0.00011495633765142635

 Aproximacao F3 com h = 0.1
-0.7357680241529193
 Aproximacao F3 com h = 0.05
-0.7357594849270432
 Aproximacao F3 com h = 0.025
-0.7357589204984263
 Aproximacao F3 com h = 0.0125
-0.7357588847353493

"""