class Solver:

    def __init__(self, numDiscos, torreA, torreB, torreC):
        self.torreA = list(reversed(range(1, numDiscos + 1)))
        self.torreB = []
        self.torreC = []
        self.numDiscos = numDiscos
        self.nomeA = torreA
        self.nomeB = torreB
        self.nomeC = torreC

    def solver(self):
        self.imprimir()

    def imprimir(self):
        for i in reversed(range(self.numDiscos)):
            print(f" | { self.torreA[i] if len(self.torreA) > i else ' '} | {self.torreB[i] if len(self.torreB) > i else ' '} | {self.torreC[i] if len(self.torreC) > i else ' '} |")
        print(f" | {self.nomeA} | {self.nomeB} | {self.nomeC} |")
