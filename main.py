import lib as l
import time

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
    start_time = time.time()
    l.read()
    l.res()
    print("--- {} seconds ---".format((time.time() - start_time)))
