import random
#importa a biblioteca do Python que seleciona um número randômico em um range

import BancoDePerguntas
#importa um arquivo na mesma pasta do Projeto que tem uma função que cria uma matriz de perguntas

import BancoDeAlternativas
#importa um arquivo na mesma pasta do Projeto que tem uma função que cria uma matriz de alternativas

perguntas=BancoDePerguntas.banco_de_perguntas()
#chamada da função banco_de_perguntas no arquivo BancoDePerguntas

alternativas=BancoDeAlternativas.banco_de_alternativas()
#chamada da função banco_de_alternativas no arquivo BancoDeAlternativas

respostas=[["B","B","C","B","D"],
           ["B","D","C","D","A"],
           ["D","B","B","C","D"],
           ["A","C","C","A","A"],
           ["C","D","D","D","B"]]
#uma variável que recebe uma matriz de strings referente as alternativas certas
#rij = r-resposta(string) i-nivel(linha) j-número(coluna)

def imprimePergunta(i,j):
    print(perguntas[i][j])
#função para resgatar valores na matriz perguntas e imprimir

def validacaoResposta(contadorDeFases,ajuda):
    while True:
        entrada=input("Qual é a alternativa certa? ").upper()
        if entrada == "A" or entrada == "B" or entrada == "C" or entrada == "D":
            break
        if entrada == "2" and contadorDeFases < 4 and ajuda == 0:
            break
        if entrada == "1" and contadorDeFases == 4:
            break
    return entrada
def jogo(perguntasRespondidas):
    contadorDeAcertos=0
    contadorDeFases=0
    continuar = True
    desistir = False
    ajuda = 0
    perguntasFeita = []
    while contadorDeFases != 5 and continuar:
    #loop crescente para execultar os 5 níveis do jogo, começa no 0 até o 5 e vai de 1 em 1
        sorte=random.randrange(5)
        if not perguntasRespondidas:
            perguntasFeita.append(perguntas[contadorDeFases][sorte])
        else:
            print(perguntasRespondidas[0][contadorDeFases])
            while perguntas[contadorDeFases][sorte] in perguntasRespondidas:
                sorte=random.randrange(5)
            perguntasFeita.append(perguntas[contadorDeFases][sorte])
        """
        Falta implementar a lógica de pular pergunta, ele pode pular 3x em diferentes fases,
        menos na última fase independente se ele ainda tem pulos.
        """
        print("{}ª Fase".format(contadorDeFases+1))
        imprimePergunta(contadorDeFases,sorte)#chamada de função que imprime a pergunta dependendo do nível e número sorteado
        
        if contadorDeFases < 4 and ajuda == 0:
            print("Aperte 2 para pedir ajuda")
        if contadorDeFases == 4:
            print("Você pode desistir apertando 1")
        certa = respostas[contadorDeFases][sorte]
        BancoDeAlternativas.imprimeAlternativas(contadorDeFases,sorte,ajuda,certa)#chamada de função que imprime as alternativas dependendo do nível e número sorteado
        entrada = validacaoResposta(contadorDeFases,ajuda)
        
        if entrada == "2":
            imprimePergunta(contadorDeFases,sorte)
            ajuda = ajuda + 1
            ajuda = BancoDeAlternativas.imprimeAlternativas(contadorDeFases,sorte,ajuda,certa)
            entrada = validacaoResposta(contadorDeFases,ajuda)
        
        if entrada == "1":
            continuar = False
            desistir = True
            
        if entrada==respostas[contadorDeFases][sorte]:#verifica se o usuário acertou a pergunta
            contadorDeAcertos = contadorDeAcertos + 1
            contadorDeFases = contadorDeFases + 1
        else:#caso a variável que contém a resposta do usuário não é igual a resporta certa da pergunta
            if contadorDeFases <= 4 and desistir == False:
                print("Resposta errada")
                print("A resposta certa é: ",respostas[contadorDeFases][sorte])
                continuar = False
            if desistir:
                print("Você desistiu!")
                continuar = False
            
    if contadorDeFases == 0:
        print("Você ganhou 500,00 Reais")
    else:
        if contadorDeAcertos == 1:
            print("Você ganhou 5.000,00 Reais")
        elif contadorDeAcertos == 2:
            print("Você ganhou 50.000,00 Reais")
        elif contadorDeAcertos == 3:
            print("Você ganhou 250.000,00 Reais")
        elif contadorDeAcertos == 4:
            if desistir:
                print("Você ganhou 500.000,00 Reais")
            else:
                print("Você ganhou 250.000,00 Reais")
        elif contadorDeAcertos == 5:
            print("Você ganhou 1.000.000,00 Reais")
    return perguntasFeita

repetir = True            
perguntasRespondidas = []

while repetir:
    print(perguntasRespondidas)
    perguntasRespondidas.append(jogo(perguntasRespondidas))
    
    
    reiniciar = input("Deseja jogar novamente (S/N): ").upper()
    
    if reiniciar == "S":
        repetir = True
    else:
        repetir = False
