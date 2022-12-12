def banco_de_perguntas():#função sem parâmetro de entrada que retorna uma matriz

    #p00-p04 perguntas fáceis
    p00="Em que estado brasileiro nasceu a apresentadora Xuxa?"
    p01="Qual é o nome dado ao estado da água em forma de gelo?"
    p02="Qual era o apelido da cantora Elis Regina?"
    p03="Quem é a namorada do Mickey?"
    p04="Qual é o personagem do folclore brasileiro que tem uma perna só?"
    
    #p10-p14 perguntas fáceis
    p10="Fidel Castro nasceu em que país?"
    p11="Quem proclamou a república no Brasil em 1889?"
    p12="Quem é o patrono do exército brasileiro?"
    p13="Quem era o apresentador que reprovava os calouros tocando uma buzina?"
    p14="O que era Frankenstein, de Mary Shelley?"

    #p20-p24 perguntas médias
    p20="Quantos jogadores um jogo de vôlei reúne na quadra?"
    p21="Qual é o país do tango?"
    p22="Que imperador pôs fogo em Roma?"
    p23="A cidade de Pompéia, que foi soterrada por um vulcão fica em qual desses países?"
    p24="Como é chamado quem nasce em Milão, na Itália?"

    #p30-p34 perguntas médias
    p30="Que profissional usa uma ferramenta chamada formão?"
    p31="Em qual estádio Pelé marcou seu milésimo gol?"
    p32="O que é um oboé?"
    p33="Como eram chamados os pilotos suicidas da Segunda Guerra?"
    p34="O que é gôndola?"

    #p40-p44 perguntas difíceis
    p40="Em qual espécie o macho choca os ovos e a fêmea procura alimento?"
    p41="Em qual país está localizado o “Muro das lamentações”?"
    p42="Qual desses países não fica na Ásia?"
    p43="Qual desses astros de filmes de ação é belga?"
    p44="Onde foi conduzida a vitória das forças aliadas na Segunda Guerra Mundial?"

    #lista com 5 listas dentro(matriz), cada lista possui 5 variáveis do tipo string
    perguntas=[[p00,p01,p02,p03,p04],
               [p10,p11,p12,p13,p14],
               [p20,p21,p22,p23,p24],
               [p30,p31,p32,p33,p34],
               [p40,p41,p42,p43,p44]]

    return perguntas #retorna uma "matriz" com 25 strings
