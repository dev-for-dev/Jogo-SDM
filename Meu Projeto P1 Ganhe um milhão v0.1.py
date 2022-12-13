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
    print(perguntas[i][j],"\n")
#função para resgatar valores na matriz perguntas e imprimir

def validacaoResposta(contadorDeFases,ajuda,pulos):
    while True:
        entrada=input("Qual é a alternativa certa? ").upper()
        if entrada == "A" or entrada == "B" or entrada == "C" or entrada == "D":
            break
        if entrada == "1" and contadorDeFases < 4 and ajuda == 1:
            print("\n{}ª Fase do jogo".format(contadorDeFases+1))
            break
        if entrada == "2" and contadorDeFases < 4 and pulos > 0:
            break
        if entrada == "3" and contadorDeFases == 4:
            break
    return entrada

def pularPergunta(pulos,perguntasPuladas,contadorDeFases,sorte):
    if pulos > 0:
        perguntasPuladas.append(perguntas[contadorDeFases][sorte])
        while perguntas[contadorDeFases][sorte] in perguntasPuladas:
            sorte=random.randrange(5)
    return sorte
            
def imprimeAuxilio(ajuda,pulos,contadorDeFases,contadorDeAcertos,desistir,dinheiro):
    if contadorDeFases < 4:
        print("\n{}ª Fase do jogo valendo {:.2f} R$".format(contadorDeFases+1,premio(contadorDeFases,contadorDeAcertos,desistir,dinheiro)*2))
        print("Você tem {} ajuda, aperte 1 para usa-la".format(ajuda))
        print("Você tem {} pulos, aperte 2 para pular\n".format(pulos))
    else:
        print("\n{}ª Fase do jogo valendo {:.2f} R$".format(contadorDeFases+1,1000000))
        print("Você NÃO tem mais ajuda")
        print("Você NÃO tem mais pulos")
        print("Você pode desistir apertando 3\n")

def premio(contadorDeFases,contadorDeAcertos,desistir,dinheiro):
    if contadorDeFases == 0:
         dinheiro = dinheiro/2
    else:
        if contadorDeAcertos == 1:
            dinheiro = (dinheiro*10)/2
        elif contadorDeAcertos == 2:
            dinheiro = (dinheiro*100)/2
        elif contadorDeAcertos == 3:
            dinheiro = (dinheiro*500)/2
        elif contadorDeAcertos == 4:
            if desistir:
                dinheiro = (dinheiro*500)
            else:
                dinheiro = (dinheiro*500)/2
        elif contadorDeAcertos == 5:
            dinheiro = (dinheiro*1000)
    return dinheiro

def jogo(perguntasRespondidas,contadorDeJogos):
    contadorDeAcertos=0
    contadorDeFases=0
    continuar = True
    desistir = False
    ajuda = 1
    pulos = 3
    perguntasFeita = []
    perguntasPuladas = []
    dinheiro = 1000.00
    while contadorDeFases != 5 and continuar:#loop crescente para execultar os 5 níveis do jogo, começa no 0 até o 5 e vai de 1 em 1
        sorte=random.randrange(5)
        if contadorDeJogos == 1:
            perguntasFeita.append(perguntas[contadorDeFases][sorte])
        else:
            for i in range(contadorDeJogos):
                while perguntas[contadorDeFases][sorte] in perguntasRespondidas[i][contadorDeFases]:
                    sorte=random.randrange(5)
            perguntasFeita.append(perguntas[contadorDeFases][sorte])

        
        imprimeAuxilio(ajuda,pulos,contadorDeFases,contadorDeAcertos,desistir,dinheiro)
        imprimePergunta(contadorDeFases,sorte)#chamada de função que imprime a pergunta dependendo do nível e número sorteado
        
        certa = respostas[contadorDeFases][sorte]
        BancoDeAlternativas.imprimeAlternativas(contadorDeFases,sorte,ajuda,certa)#chamada de função que imprime as alternativas dependendo do nível e número sorteado
        entrada = validacaoResposta(contadorDeFases,ajuda,pulos)

        while entrada == "2" and pulos > 0 or entrada == "1":
            if entrada == "2":
                sorte = pularPergunta(pulos,perguntasPuladas,contadorDeFases,sorte)
                pulos -= 1
                imprimeAuxilio(ajuda,pulos,contadorDeFases,contadorDeAcertos,desistir,dinheiro)
                imprimePergunta(contadorDeFases,sorte)
                BancoDeAlternativas.imprimeAlternativas(contadorDeFases,sorte,ajuda,certa)
            if entrada == "1":
                ajuda += 1
                imprimeAuxilio(ajuda-2,pulos,contadorDeFases,contadorDeAcertos,desistir,dinheiro)
                imprimePergunta(contadorDeFases,sorte)
                ajuda = BancoDeAlternativas.imprimeAlternativas(contadorDeFases,sorte,ajuda,certa)
            entrada = validacaoResposta(contadorDeFases,ajuda,pulos)

        if entrada == "3":
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
            
    
    print("Você ganhou {:.2f} Reais".format(premio(contadorDeFases,contadorDeAcertos,desistir,dinheiro)))
    return perguntasFeita

repetir = True            
perguntasRespondidas = []
contadorDeJogos=0
while repetir:
    perguntasRespondidas.append(jogo(perguntasRespondidas,contadorDeJogos))
    contadorDeJogos += 1
    if contadorDeJogos == 5:
        perguntasRespondidas = []
        contadorDeJogos = 0
    
    reiniciar = input("Deseja jogar novamente (S/N): ").upper()
    
    if reiniciar == "S":
        repetir = True
    else:
        repetir = False
