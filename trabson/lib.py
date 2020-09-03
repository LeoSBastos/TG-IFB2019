from le import Le
from conexos import Conexos
from buscas import Busca
class Lib:
    def __init__(self,matrix,cost,a,b):
        self.matrix = matrix
        self.cost = cost
        self.le = Le(self.matrix, self.cost)
        self.cx = Conexos(self.le) 
        self.a = a
        self.b = b
    def run(self):
        self.le.read()
        self.le.res()
        b=Busca(self.a,self.b,self.le.vt,self.le.edges)
        if self.cost:
            res = b.ucs()
        else:
            res = b.bfs()
        if res is not None:
            print(b.caminho)
        #cx.Solve()
