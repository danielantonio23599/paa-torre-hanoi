class Solver:

    def __init__(self, numDiscos, torreA, torreB, torreC):
        self.torreA = list(reversed(range(1, numDiscos + 1)))
        self.torreB = []
        self.torreC = []
        self.numDiscos = numDiscos
        self.nomeA = torreA
        self.nomeB = torreB
        self.nomeC = torreC
        self.imprimir()

    def solver(self, num, torreO, torreD, torreT):
        if num > 0:
            # chama recursivamente até o num = 1, invertendo a torre de destino com a auxiliar
            self.solver(num - 1, torreO, torreT, torreD)
            self.mover(torreO, torreD)# move
            # chama a recurção novamente para mover da torre auxiliar para a torre de destino, utilizando a origem como auxiliar
            self.solver(num - 1, torreT, torreD, torreO)


    def imprimir(self):
        for i in reversed(range(self.numDiscos)):
            print(
                f" | {self.torreA[i] if len(self.torreA) > i else ' '} | {self.torreB[i] if len(self.torreB) > i else ' '} | {self.torreC[i] if len(self.torreC) > i else ' '} |")
        print(f" | {self.nomeA} | {self.nomeB} | {self.nomeC} |")

    def mover(self, nomeO, nomeD):
        valor = None
        if nomeO == self.nomeA:
            valor = self.torreA[-1]
            self.torreA.pop()
        elif nomeO == self.nomeB:
            valor = self.torreB[-1]
            self.torreB.pop()
        elif nomeO == self.nomeC:
            valor = self.torreC[-1]
            self.torreC.pop()
        if nomeD == self.nomeA:
            self.torreA.append(valor)
        elif nomeD == self.nomeB:
            self.torreB.append(valor)
        elif nomeD == self.nomeC:
            self.torreC.append(valor)
        print(f' mover o numero {valor} , {nomeO} -> {nomeD} ')
        self.imprimir()
