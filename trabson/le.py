from vertix import Vertix
from edge import Edge
class Le:
    def __init__(self, matrix=False,cost=False):
        self.n=0 #N do output
        self.vt=[] #Array de Vertices
        self.count=0 #M do output
        self.matriz=[]
        self.matrix=matrix
        self.cost=cost
        self.edges=[]
    def read(self):
        with open("data.txt") as file: #Abrir arquivo
            data=file.readlines() #Pega o arquivo e faz um array de linhas
            self.n=int(data.pop(0)) #Tira a primeira linha e coloca no N
            if self.matrix:
                self.matriz=[[0 for i in range(n)] for i in range(n)]
            self.count=len(data) #Verifica o numero de linhas restantes e coloca no M
            for dt in data: #Para cada linha em data
                flag1 = False #Ele indentificou o primeiro Vertice?
                flag2 = False #Ele indentificou o segundo Vertice?
                flag3 = False #Ele fez a operacao?
                if not self.cost:
                    v1,v2 = (int(x) for x in dt.rstrip().split(" ")) #Separa pelo espaço e coloca em
                                                                    #duas variaveis
                else:
                    d=dt.rstrip().split(" ")
                    v1,v2,v3=(int(d[0]),int(d[1]),float(d[2]))
                if(len(self.vt) == 0): #Se o Array for vazio
                    if self.matrix:
                        aux = Vertix(v1,True) #Cria o objeto Vertice para os dois
                        aux2 = Vertix(v2,True) #Cria o objeto Vertice para os dois
                        self.matriz[v1-1][v2-1] = self.matriz[v2-1][v1-1] = 1
                    else:
                        aux = Vertix(v1) #Cria o objeto Vertice para os dois
                        aux2 = Vertix(v2) #Cria o objeto Vertice para os dois
                    aux.add(aux2) #Adiciona a aresta
                    aux2.add(aux) #Adiciona a aresta
                    self.vt.append(aux) #Adiciona no vetor
                    self.vt.append(aux2) #Adiciona no vetor
                    if self.cost:
                        aux3=Edge(aux,aux2,v3)
                        aux4=Edge(aux2,aux,v3)
                    else:
                        aux3=Edge(aux,aux2)
                        aux4=Edge(aux2,aux)
                    self.edges.append(aux3)
                    self.edges.append(aux4)
                    

                else:
                    aux=None #Reseta as auxiliares
                    aux2=None #Reseta as auxiliares
                    for v in self.vt: #Para cada vertice no array
                        if(v==v1 and not flag1): #Se o valor do vertice for igual
                                                #ao primeiro e ja nao tiver sido
                                                #setado
                            flag1=True #Seta a flag1
                            aux=v #seta o vertice na aux
                            if(flag2): #se o vertice 2 ja tiver sido setado
                                flag3=True #seta que a operacao ocorreu
                                v.add(aux2) #Adiciona a aresta
                                aux2.add(v) #Adiciona a aresta
                                if self.cost:
                                    aux3=Edge(v,aux2,v3)
                                    aux4=Edge(aux2,v,v3)
                                else:
                                    aux3=Edge(v,aux2)
                                    aux4=Edge(aux2,v)
                                self.edges.append(aux3)
                                self.edges.append(aux4)
                                if self.matrix:
                                    self.matriz[v1-1][v2-1] = self.matriz[v2-1][v1-1] = 1
                        if(v==v2 and not flag2): #Se o valor do vertice for igual
                                                #ao segundo e ja nao tiver sido
                                                #setado
                            flag2=True #Seta a flag2
                            aux2=v #seta o vertice na aux2
                            if(flag1): #se o vertice 1 ja tiver sido setado
                                flag3=True #seta que a operacao ocorreu
                                v.add(aux) #Adiciona a aresta
                                aux.add(v) #Adiciona a aresta
                                if self.cost:
                                    aux3=Edge(aux,v,v3)
                                    aux4=Edge(v,aux,v3)
                                else:
                                    aux3=Edge(aux,v)
                                    aux4=Edge(v,aux)
                                self.edges.append(aux3)
                                self.edges.append(aux4)

                                if self.matrix:
                                    self.matriz[v1-1][v2-1] = self.matriz[v2-1][v1-1] = 1
                    if not flag3: #Se nao tiver ocorrido a operacao
                        if(aux==None and aux2==None): #Se nao tiver encontrado
                                                    #nenhum dos dois vertices
                            aux=Vertix(v1) #Cria o objeto Vertice para os dois
                            aux2=Vertix(v2) #Cria o objeto Vertice para os dois
                            aux.add(aux2) #Adiciona a aresta
                            aux2.add(aux) #Adiciona a aresta
                            self.vt.append(aux) #Adiciona no vetor
                            self.vt.append(aux2) #Adiciona no vetor
                        elif (aux==None): #Se o primeiro nao tiver sido encontrado
                            aux=Vertix(v1) #Cria o objeto Vertice para o primeiro
                            aux.add(aux2) #Adiciona a aresta
                            aux2.add(aux) #Adiciona a aresta
                            self.vt.append(aux) #Adiciona no vetor
                        elif (aux2==None): #Se o segundo nao tiver sido encontrado
                            aux2=Vertix(v2) #Cria o objeto Vertice para o segundo
                            aux.add(aux2) #Adiciona a aresta
                            aux2.add(aux) #Adiciona a aresta
                            self.vt.append(aux2) #Adiciona no vetor
                        if self.cost:
                            aux3=Edge(aux,aux2,v3)
                            aux4=Edge(aux2,aux,v3)
                        else:
                            aux3=Edge(aux,aux2)
                            aux4=Edge(aux2,aux)
                        self.edges.append(aux3)
                        self.edges.append(aux4)
                        if self.matrix:
                            self.matriz[v1-1][v2-1] = self.matriz[v2-1][v1-1] = 1
    def res(self, filename="res.txt",res=True, vetor=None):
        if vetor is None:
            vetor=self.vt
        vetor.sort(key=lambda x: x.value) #Ordena o vetor de acordo com o numero dele
        with open(filename,mode='w+') as f: #Abre o arquivo pra escrita
            if res:
                f.write("# n = {}\n".format(self.n)) #Escreve no arquivo
                f.write("# m = {}\n".format(self.count)) #Escreve no arquivo
                for v in vetor: #Para cada vertice em vetor
                    f.write("{} {}\n".format(v.value,v.length)) #Escreve no arquivo
                if self.matrix:
                    for l in self.matriz: #para cada linha na matriz 
                        print(l) #escreve a linha no arquivo
            else:
                for v in vetor: #Para cada vertice em vetor
                    f.write("{} \n".format(v.value)) #Escreve no arquivo