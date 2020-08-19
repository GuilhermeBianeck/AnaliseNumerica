class Newton:
    def __init__(self, fun, funD, x1, n):
        self.fun = fun
        self.funD = funD
        self.x1 = x1
        self.n = n

    def run(self):
        for i in range(self.n):
            self.x1 = self.x1 - (self.fun(self.x1)/self.funD(self.x1))
            print(self.x1)


class PosicaoFalsa:
    def __init__(self, fun, a, b, n):
        self.fun = fun
        self.a = a
        self.b = b
        self.n = n

    def run(self):
        for i in range(self.n):
            fa = self.fun(self.a)
            fb = self.fun(self.b)
            c = self.b - ((fb*(self.b - self.a)) / (fb-fa))
            fc = self.fun(c)
            if (fa < 0 and fc < 0) or (fa > 0 and fc > 0):
                self.a = c
            else:
                self.b = c
            print(c)


class Secante:
    def __init__(self, fun, x0, x1, n):
        self.fun = fun
        self.x0 = x0
        self.x1 = x1
        self.n = n

    def run(self):
        for i in range(self.n):
            fx0 = self.fun(self.x0)
            fx1 = self.fun(self.x1)
            x2 = (self.x0*fx1 - self.x1*fx0)/(fx1 - fx0)
            print(x2)
            self.x1, self.x0 = x2, self.x1


class Gauss:
    def __init__(self, matrice):
        self.matrice = matrice

    def run(self):
        Tam = len(self.matrice[0]) - 1
        for j in range(Tam - 1):
            if self.matrice[j][j] == 0:
                for h in range(j + 1, Tam):
                    if self.matrice[h][j] != 0:
                        self.matrice[j][j], self.matrice[h][j] = self.matrice[h][j], self.matrice[j][j]
            for i in range(j + 1, Tam):
                value = -(self.matrice[i][j] / self.matrice[j][j])
                print(value)
                for h in range(j, Tam - 1):
                    self.matrice[i][h] = value * self.matrice[j][h] + self.matrice[i][h]
            
        for ll in self.matrice:
            print(ll)

class Jacobi:
    def __init__(self, matrix):
        self.matrix = [matrix[i][:-1] for i in range(len(matrix))]
        self.b = [matrix[i][-1] for i in range(len(matrix))]

    def show(self):
        print("Matrix")
        for i in range(len(self.matrix)):
            print(self.matrix[i])
        print(self.b)

    def diag(self):
        return [self.matrix[i][i] for i in range(len(self.matrix[0]))]
    
    def diagSubtract(self, diag):
        for i in range(len(diag)):
            self.matrix[i][i] -= diag[i]

    def zeros(self):
        return [0] * len(self.matrix[0])

    def dot(self, guess):
        return [sum([self.matrix[i][j] * guess[j] for j in range(len(self.matrix[i]))]) for i in range(len(self.matrix))]

    def subtractList(self, listA, listB):
        print "     Subtrai ", listB, "de ", listA
        return [listA[i] - listB[i] for i in range(len(listA))]
        
    def divideList(self, listA, listB):
        print "     Divide ", listA, "por ", listB
        return [listA[i] / listB[i] for i in range(len(listA))]
        

    def run(self, N=25, guess=None):
        result = []
        if guess is None:
            guess = self.zeros()
        
        diag = self.diag()
        self.diagSubtract(diag)

        for i in range(N):
            result.append(guess)
            print "     Iteracao -", i+1
            print "     Chute ", guess
            guess =  self.divideList(self.subtractList(self.b, self.dot(guess)), diag)
            print "     Chute ", guess
            print "\n"
        return result
        

class GaussSeidel:
    def __init__(self, matrix):
        self.matrix = [matrix[i][:-1] for i in range(len(matrix))]
        self.b = [matrix[i][-1] for i in range(len(matrix))]

    def show(self):
        print("Matrix")
        for i in range(len(self.matrix)):
            print(self.matrix[i])
        print(self.b)

    def run(self, guess):
        size = len(self.matrix)
        for j in range(size):
            d = self.b[j]
            for i in range(size):
                if j!=i:
                    #print "d = d -", self.matrix[j][i], "* ", guess[i] 
                    d -= self.matrix[j][i] * guess[i]

            print "Chute [",j,"] = ", d, "/", self.matrix[j][j], "=", (d / self.matrix[j][j])
            guess[j] = d / self.matrix[j][j]

        return guess

        


def main():

    matrix =  [[4,1,1,6],
                [2,5,2,3],
                [1,2,4,11]];
                    
    guess = [0, 0, 0];
    print "Exercicio 3 - A - Metodo Jacobi"
    Ann = Jacobi(matrix)
    Ann.show()
    answr = Ann.run(10, guess)
    print'                           ',('x{}'.format(1),'x{}'.format(2),'x{}'.format(3))
    for j in range(len(answr)):
            print"Iteracao ",j+1," -  Chute",(answr[j][0],'', answr[j][1],'', answr[j][2])

    print "\n\n"
    matrix =  [[3,2,1,2],[2,7,2,-3],[1,3,5,3]]
                    
    guess = [0,0,0];

    print "Exercicio 3 - B - Metodo Jacobi"

    Ann = Jacobi(matrix)
    Ann.show()
    answr = Ann.run(10, guess)
    print'                          ',('x{}'.format(1),'x{}'.format(2),'x{}'.format(3))
    for j in range(len(answr)):
            print"Iteracao ",j+1," -  Chute",(answr[j][0],'', answr[j][1],'', answr[j][2])
    print "\n\n"
    matrix =  [[1,1,-3,5],[0,-2,1,-3],[-4,1,-1,-2]]
                    
    guess = [1,0,0];

    print "Exercicio 3 - C - Metodo Jacobi"
    Ann = Jacobi(matrix)
    Ann.show()
    answr = Ann.run(10, guess)
    print'                           ',('x{}'.format(1),'x{}'.format(2),'x{}'.format(3))
    for j in range(len(answr)):
            print"Iteracao ",j+1," -  Chute",(answr[j][0],'', answr[j][1],'', answr[j][2])
    print "\n\n"
    matrix =  [[3,2,1,1],[1,-4,2,3],[1,-3,5,-1]]
                    
    guess = [0,0,0];

    print "Exercicio 3 - D - Metodo Jacobi"
    Ann = Jacobi(matrix)
    Ann.show()
    answr = Ann.run(10, guess)
    print'                           ',('x{}'.format(1),'x{}'.format(2),'x{}'.format(3))
    for j in range(len(answr)):
            print"      Iteracao ",j+1," -  Chute",(answr[j][0],'', answr[j][1],'', answr[j][2])



if __name__ == "__main__":
    main()
