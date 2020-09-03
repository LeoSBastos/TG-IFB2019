class Edge:
    def __init__(self,v1,v2,cost=1):
        self.v1 = v1
        self.v2 = v2
        self.cost = cost

    def __lt__(self,other):
        return self.cost < other.cost