from vertix import Vertix
from queue import Queue, LifoQueue, PriorityQueue, deque
from edge import Edge


class Busca:
    def __init__(self, start, end, lista, edges):
        self.list = lista
        for index, val in enumerate(lista):
            if val.value == start:
                self.start = val
        self.end = end
        self.caminho = []
        self.edges = edges

    def bfs(self):
        if self.start.value == self.end:
            return self.start
        filha = Queue()
        visited = list()
        filha.put(self.start)
        while not filha.empty():
            vertice, caminho = filha.get()
            if vertice.value in visited:
                continue
            # se ele for o nó buscado o retorna
            if vertice.value == self.end:
                self.caminho.append(caminho)
                return vertice
            # senão o adiciona na lista de visited
            visited.append(vertice.value)
            for adj in vertice.next:
                if adj.value not in visited:
                    e = next(x for x in self.edges if x.v1 == vertice and x.v2 == adj)
                    filha.put([adj, "{} -> {}".format(e.v1.value, e.v2.value)])
            self.caminho.append(caminho)
        return None

    def dfs(self):
        if self.start.value == self.end:
            return self.start
        elgin = LifoQueue()
        visited = list()
        elgin.put(self.start)
        while not elgin.empty():
            # retira da pilha o mais externo para poder testar
            vertice = elgin.get()
            # se este nó já foi visitado vai para o próximo da pilha
            if vertice.value in visited:
                continue
            # se ele for o nó buscado o retorna
            if vertice.value == self.end:
                return vertice
            # senão o adiciona na lista de visited
            visited.append(vertice.value)
            # visita os nós filhos e os adiciona na pilha
            for adj in vertice.next:
                if adj.value not in visited:
                    elgin.put(adj)
        return None

    def ucs(self):
        if self.start.value == self.end:
            return self.start
        pne = PriorityQueue()
        visitados = list()
        pne.put((0, [self.start, "Inicio -> {}".format(self.start.value)]))
        while not pne.empty():
            # retira da pilha o mais externo para poder testar
            cost, [vertice, caminho] = pne.get()
            # se este nó já foi visitado vai para o próximo da pilha
            if vertice.value in visitados:
                continue
            # se ele for o nó buscado o retorna
            if vertice.value == self.end:
                self.caminho.append(caminho)
                return vertice
            # senão o adiciona na lista de visitados
            visitados.append(vertice.value)
            for adj in vertice.next:
                if adj.value not in visitados:
                    e = next(x for x in self.edges if x.v1 == vertice and x.v2 == adj)
                    pne.put((float(e.cost)+cost, [adj, "{} -> {}".format(e.v1.value, e.v2.value)]))
            self.caminho.append(caminho)
        return None
