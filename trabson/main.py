from lib import Lib

if __name__ == "__main__":
    while True:
        res = input("Voce deseja que a representacao seja matriz? Ou Lista? ")
        res2 = input("Tera custo ou nao? ")
        res3 = int(input("Qual o valor do vertice incial da busca? "))
        res4 = int(input("Qual o valor do vertice final da busca? "))

        if (res.lower() == "matriz"):
            if(res2.lower() == "sim"):
                l = Lib(True,True,res3,res4)
                break
            if(res2.lower() == "nao"):
                l = Lib(True,False,res3,res4)
                break
        elif(res.lower() == "lista"):
            if(res2.lower() == "sim"):
                l = Lib(False,True,res3,res4)
                break
            if(res2.lower() == "nao"):
                l = Lib(False,False,res3,res4)
                break
        else:
            print("Voce nao digitou uma resposta valida.")
    l.run()
