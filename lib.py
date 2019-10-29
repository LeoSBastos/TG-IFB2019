n=0 #N do output
vt=[] #Array de Vertices
count=0 #M do output
matriz=[]
matrix=False
def read():
    global n #chamando para alterar a variavel global
    global count #chamando para alterar a variavel global
    global matriz #chamando para alterar a variavel matriz
    with open("data.txt") as file: #Abrir arquivo
        data=file.readlines() #Pega o arquivo e faz um array de linhas
        n=int(data.pop(0)) #Tira a primeira linha e coloca no N
        if matrix:
            matriz=[[0 for i in range(n)] for i in range(n)]
        count=len(data) #Verifica o numero de linhas restantes e coloca no M
        for dt in data: #Para cada linha em data
            flag1 = False #Ele indentificou o primeiro Vertice?
            flag2 = False #Ele indentificou o segundo Vertice?
            flag3 = False #Ele fez a operacao?
            v1,v2 = (int(x) for x in dt.split(" ")) #Separa pelo espaço e coloca em
                                                    #duas variaveis
            if(len(vt) == 0): #Se o Array for vazio
                if matrix:
                    aux = Vertix(v1,True) #Cria o objeto Vertice para os dois
                    aux2 = Vertix(v2,True) #Cria o objeto Vertice para os dois
                    matriz[v1-1][v2-1] = matriz[v2-1][v1-1] = 1
                else:
                    aux = Vertix(v1) #Cria o objeto Vertice para os dois
                    aux2 = Vertix(v2) #Cria o objeto Vertice para os dois
                aux.add(aux2) #Adiciona a aresta
                aux2.add(aux) #Adiciona a aresta
                vt.append(aux) #Adiciona no vetor
                vt.append(aux2) #Adiciona no vetor
            else:
                aux=None #Reseta as auxiliares
                aux2=None #Reseta as auxiliares
                for v in vt: #Para cada vertice no array
                    if(v==v1 and not flag1): #Se o valor do vertice for igual
                                             #ao primeiro e ja nao tiver sido
                                             #setado
                        flag1=True #Seta a flag1
                        if(flag2): #se o vertice 2 ja tiver sido setado
                            flag3=True #seta que a operacao ocorreu
                            v.add(aux2) #Adiciona a aresta
                            aux2.add(v) #Adiciona a aresta
                            if matrix:
                                matriz[v1-1][v2-1] = matriz[v2-1][v1-1] = 1
                        aux=v #seta o vertice na aux
                    elif(v==v2 and not flag2): #Se o valor do vertice for igual
                                             #ao segundo e ja nao tiver sido
                                             #setado
                        flag2=True #Seta a flag2
                        aux2=v #seta o vertice na aux2
                        if(flag1): #se o vertice 1 ja tiver sido setado
                            flag3=True #seta que a operacao ocorreu
                            v.add(aux) #Adiciona a aresta
                            aux.add(v) #Adiciona a aresta
                            if matrix:
                                matriz[v1-1][v2-1] = matriz[v2-1][v1-1] = 1
                if not flag3: #Se nao tiver ocorrido a operacao
                    if(aux==None and aux2==None): #Se nao tiver encontrado
                                                  #nenhum dos dois vertices
                        if not matrix:
                            aux=Vertix(v1) #Cria o objeto Vertice para os dois
                            aux2=Vertix(v2) #Cria o objeto Vertice para os dois
                        else:
                            aux=Vertix(v1, True) #Cria o objeto Vertice para os dois
                            aux2=Vertix(v2,True) #Cria o objeto Vertice para os dois
                        aux.add(aux2) #Adiciona a aresta
                        aux2.add(aux) #Adiciona a aresta
                        vt.append(aux) #Adiciona no vetor
                        vt.append(aux2) #Adiciona no vetor
                    elif (aux==None): #Se o primeiro nao tiver sido encontrado
                        if not matrix:
                            aux=Vertix(v1) #Cria o objeto Vertice para o primeiro
                        else:
                            aux=Vertix(v1, True) #Cria o objeto Vertice para os dois
                        aux.add(aux2) #Adiciona a aresta
                        aux2.add(aux) #Adiciona a aresta
                        vt.append(aux) #Adiciona no vetor
                    elif (aux2==None): #Se o segundo nao tiver sido encontrado
                        if not matrix:
                            aux2=Vertix(v2) #Cria o objeto Vertice para o segundo
                        else:
                            aux2=Vertix(v2, True) #Cria o objeto Vertice para os dois
                        aux.add(aux2) #Adiciona a aresta
                        aux2.add(aux) #Adiciona a aresta
                        vt.append(aux2) #Adiciona no vetor
                    if matrix:
                        matriz[v1-1][v2-1] = matriz[v2-1][v1-1] = 1
def res():
    vt.sort(key=lambda x: x.number) #Ordena o vetor de acordo com o numero dele
    with open("res.txt",mode='w+') as f: #Abre o arquivo pra escrita
        f.write("# n = {}\n".format(n)) #Escreve no arquivo
        f.write("# m = {}\n".format(count)) #Escreve no arquivo
        for v in vt: #Para cada vertice em vetor
            f.write("{} {}\n".format(v,len(v.next))) #Escreve no arquivo
        if matrix:
            for l in matriz: #para cada linha na matriz 
                print(l) #escreve a linha no arquivo

class Vertix: #Classe Vertice
    def __init__(self,n,matriz = False): #Construtor
        self.number=n #numero do vertice
        self.next=[] #Vetor de Vertices próximos
        if not matriz:
            self.prev=[] #Vetor de Vertices anteriores
        self.matriz=matriz
    
    def __eq__(self,other): #Metodo equals
        return self.number==other

    def __repr__(self): #Representação dele
        return str(self.number)

    def __str__(self): #Metodo toString
        return self.number

    def add(self,v): #Metodo para adicionar a aresta
        self.next.append(v) #adiciona a aresta
        if not self.matriz:
            self.prev.append(v) #adiciona a aresta