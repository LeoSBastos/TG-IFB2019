class Vertix: #Classe Vertice
    def __init__(self,n, matriz = False, cost=1): #Construtor
        self.value=n #numero do vertice
        self.next=[] #Vetor de Vertices próximos
        if not matriz:
            self.prev=[] #Vetor de Vertices anteriores
        self.length=0 #numero de arestas dele
        self.cost = cost
        self.matriz=matriz
    
    def __eq__(self,other): #Metodo equals
        return self.value==other

    def __lt__(self, other):
        return self.cost < other.cost 

    def __repr__(self): #Representação dele
        return str(self.value)

    def __str__(self): #Metodo toString
        return str(self.value)

    def add(self,v): #Metodo para adicionar a aresta
        self.next.append(v) #adiciona a aresta
        if not self.matriz:
            self.prev.append(v) #adiciona a aresta
        self.length+=1 #aumenta o numero de arestas