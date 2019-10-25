import lib as l

if __name__ == "__main__":
    while True:
        res = input("Voce deseja que a representacao seja matriz? Ou Lista? ")
        if (res.lower() == "matriz"):
            l.matrix = True
            break
        elif(res.lower() == "lista"):
            l.matrix = False
            break
        else:
            print("Você nao digitou uma resposta valida.")
    l.read()
    l.res()
