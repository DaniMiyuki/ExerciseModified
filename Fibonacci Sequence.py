def funcao(numero):
    t1 = 0
    t2 = 1
    cont = 0
    print(t1, t2, end=' ')
    for ind in range(0, numero - 2):
        t3 = t1 + t2
        print(t3, end=' ')
        t1 =t2
        t2= t3
        cont +=1
    return t3


nE = int(input('Digite o numero de sequencia desejada: '))
funcao(nE)