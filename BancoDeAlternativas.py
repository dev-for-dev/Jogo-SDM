import random
def banco_de_alternativas():#função sem parâmetro de entrada que retorna uma matriz

    #alternativas referentes a p00-p04 perguntas fáceis
    a00=["a)RIO DE JANEIRO","b)RIO GRANDE DO SUL","c)SANTA CATARINA","d)GOIÁS"]
    a01=["a)LÍQUIDO","b)SÓLIDO","c)GASOSO","d)VAPOROSO"]
    a02=["a)GAUCHINHA","b)PAULISTINHA","c)PIMENTINHA","d)ANDORINHA"]
    a03=["a)MARGARIDA","b)MINNIE","c)A PEQUENA SEREIA","d)OLÍVIA PALITO"]
    a04=["a)CUCA","b)NEGRINHO DO PASTOREIO","c)BOITATÁ","d)SACI-PERERÊ"]

    #alternativas referentes a p10-p14 perguntas fáceis
    a10=["a)JAMAICA","b)CUBA","c)EL SALVADOR","d)MÉXICO"]
    a11=["a)DUQUE DE CAXIAS","b)MARECHAL RONDON","c)DOM PEDRO II","d)MARECHAL DEODORO"]
    a12=["a)MARECHAL DEODORO","b)BARÃO DE MAUÁ","c)DUQUE DE CAXIAS","d)MARQUÊS DE POMBAL"]
    a13=["a)RAUL GIL","b)BOLINHA","c)FLÁVIO CAVALCANTI","d)CHACRINHA"]
    a14=["a)MONSTRO","b)GORILA","c)PRÍNCIPE","d)SAPO"]

    #alternativas referentes a p20-p24 perguntas médias
    a20=["a)SEIS","b)OITO","c)DEZ","d)DOZE"]
    a21=["a)URUGUAI","b)ARGENTINA","c)PARAGUAI","d)ESPANHA"]
    a22=["a)TRAJANO","b)NERO","c)BRUTUS","d)CALÍGULA"]
    a23=["a)JAPÃO","b)MÉXICO","c)ITÁLIA","d)ESTADOS UNIDOS"]
    a24=["a)MILANENSE","b)MILANOSO","c)MILISTA","d)MILANÊS"]

    #alternativas referentes a p30-p34 perguntas médias
    a30=["a)CARPINTEIRO","b)RELOJOEIRO","c)CONFEITEIRO","d)BOMBEIRO"]
    a31=["a)MORUMBI","b)PACAEMBU","c)MARACANÃ","d)MINEIRÃO"]
    a32=["a)VULCÃO","b)COMIDA","c)INSTRUMENTO MUSICAL","d)TRIBO INDÍGENA"]
    a33=["a)CAMICASES","b)SASHIMIS","c)HARAQUIRIS","d)SUMÔS"]
    a34=["a)EMBARCAÇÃO","b)BRINQUEDO","c)MÚSICA","d)SÍMBOLO"]

    #alternativas referentes a p40-p44 perguntas difíceis
    a40=["a)ANDORINHA","b)PATO SELVAGEM","c)PINGÜIM","d)MARRECO"]
    a41=["a)ALEMANHA","b)BRASIL","c)VENEZUELA","d)ISRAEL"]
    a42=["a)PAQUISTÃO","b)JAPÃO","c)TAILÂNDIA","d)EGITO"]
    a43=["a)ARNOLD SCHWARZENEGGER","b)SYLVESTER STALLONE","c)STEVEN SEAGAL","d)JEAN CLAUDE VAN DAMME"]
    a44=["a)CANNES","b)NORMANDIA","c)CAPRI","d)MARSELHA"]

    #lista com 5 listas dentro(matriz), cada lista possui 5 variáveis do tipo string
    alternativas=[[a00,a01,a02,a03,a04],
                  [a10,a11,a12,a13,a14],
                  [a20,a21,a22,a23,a24],
                  [a30,a31,a32,a33,a34],
                  [a40,a41,a42,a43,a44]]

    return alternativas #retorna uma "matriz" com 25 strings

def imprimeAlternativas(i,j,ajuda,certa):
    alternativas = banco_de_alternativas()
    letras={"A":0,"B":1,"C":2,"D":3}
    if ajuda == 1:
        correta=alternativas[i][j][letras[certa]]
        
        errada=random.randrange(4)
        while errada == letras[certa]:
            errada=random.randrange(4)
        
        if letras[certa] > errada:
            print(alternativas[i][j][errada])
            print(correta)
        else:
            print(correta)
            print(alternativas[i][j][errada])
        return ajuda + 1
    else:
        for i in alternativas[i][j]:
            print(i)
