from queue import Empty
import random

#Luis Felipe Menslin

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
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    if (opcao == 4):
        break
    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utiliada")
    letra = input()

    if(opcao == 1): #Primeira escolha
        for i in range(100):  
            if (memoria[i] == ' '): # Identificando as casas vazias
                contador.append(i) # Gravando a localização da(s) vazia(s)
                if (len(contador) == tamanho): # Se a quantidade de casas gravadas é suficiente pra suportar o tamanho informado
                    for i in range(tamanho):
                        memoria[contador[i]] = letra # Gravando o programa no primeiro espaço com tamanho suficiente
                    break 
            else:
                contador = [] # Se a quantidade de espaços vazios contados antes de encontrar um valor, não foi suficiente para armazenar o programa, ele zera a contagem.
    else:

        if (opcao == 2): #Melhor escolha
            for i in range(100):
                if (memoria[i] == ' '): # Identificando as casas vazias
                    contador.append(i) # Gravando a localização da(s) vazia(s)
                else:
                    if (len(menor) == 0 and len(contador) == tamanho): # O programa vai ser gravado somente 1 vez e quando o tamanho for igual a quantidade de posições gravadas no contador
                        menor = contador
                        break
                    contador = [] # Caso ele encontre um valor preenchido e não entre na condição ele zera o contador
            for i in range(tamanho):
                memoria[menor[i]] = letra # Gravando o programa nas coordenadas em que o espaço disponivel é exatamente do tamanho do programa 
        else:

            if(opcao == 3): # Pior escolha
                for i in range(100):
                    if (memoria[i] == ' '): # Identificando as casas vazias
                        contador.append(i) # Gravando a localização da(s) vazia(s)
                    else:
                        if (len(maior) == 0): # Executa só uma vez
                            maior = contador # Gravando o primeiro valor do maior
                        if (len(contador) > len(maior) and len(contador) >= tamanho): # Condição pra substituir o maior
                            maior = contador
                        contador = [] # Zerando o contador
                for i in range(tamanho):
                    memoria[maior[i]] = letra # Gravando o valor na memoria
    print(memoria)
print("Processo finalizado!")