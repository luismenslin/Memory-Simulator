from queue import Empty
import random

memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''
for i in range(100):
    if(random.randint(0,11) >= 5):
        memoria[i] = 'x'
    else:
        memoria[i] = ' '
print(memoria)

while(opcao != 4):
    contador = []
    maior = []
    menor = []
    print("1 - First Choice")
    print("2 - Best Choice")
    print("3 - Worst Choice")
    print("4 - End the algorithm")
    print("Choose the algorithm by the number")
    opcao = int(input())
    if (opcao == 4):
        break
    print("Type the size of the information")
    tamanho = int(input())
    print("Type something to fill the spaces")
    letra = input()

    if(opcao == 1): 
        for i in range(100):  
            if (memoria[i] == ' '): 
                contador.append(i) 
                if (len(contador) == tamanho): 
                    for i in range(tamanho):
                        memoria[contador[i]] = letra 
                    break 
            else:
                contador = [] 
    else:

        if (opcao == 2):
            for i in range(100):
                if (memoria[i] == ' '):
                    contador.append(i) 
                else:
                    if (len(menor) == 0 and len(contador) == tamanho):
                        menor = contador
                        break
                    contador = []
            for i in range(tamanho):
                memoria[menor[i]] = letra
        else:

            if(opcao == 3):
                for i in range(100):
                    if (memoria[i] == ' '):
                        contador.append(i)
                    else:
                        if (len(maior) == 0):
                            maior = contador
                        if (len(contador) > len(maior) and len(contador) >= tamanho):
                            maior = contador
                        contador = []
                for i in range(tamanho):
                    memoria[maior[i]] = letra
    print(memoria)
print("Process ended!")