from buscas import Busca


class Conexos:
    def __init__(self, le):
        self.list = le.vt
        self.le = le
        self.i = 0

    def Solve(self, lista=None):
        if lista is None:
            lista = self.list
        aux = []
        i = lista[0]
        for l in lista:
            b = Busca(lista, i, l.value)
            res = b.dfs()
            if res == None:
                aux.append(l)
                lista.remove(l)
        if len(aux) != 0:
            self.Solve(aux)
        self.le.res('conexos{}.txt'.format(self.i), False, lista)
        self.i += 1
