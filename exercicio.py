#Criei uma lista chamada filmes com o nome dos 10 primeiros filmes mais bem avaliados no
#site no IMDB. Imprima o resultado.

filmes = ['Um Sonho de Liberdade','O Poderoso Chefão','Batman - O Cavaleiro das Trevas',
          'O Poderoso Chefão II','12 Homens e uma Sentença','A Lista de Schindler',
          'O Senhor dos Anéis: O Retorno do Rei','Pulp Fiction - Tempo de Violência',
          'O Senhor dos Anéis: A Sociedade do Anel','Três Homens em Conflito']

print(filmes)


# Substituindo o valor no índice 0 pelo valor no índice 1 usando o método insert
# Consegui resolver sem o uso do pop , mais simples.
filmes.insert(0, filmes[1])

print(filmes)


#Aconteceu um erro no seu ranking. Simule a duplicação dos três últimos filmes da lista.
#Imprima o resultado.


filmes.append('Três Homens em Conflito')
filmes.append('Três Homens em Conflito')
filmes.append('Três Homens em Conflito')

atualizandofilmes = list(set(filmes))

print(filmes)
print(atualizandofilmes)


#Repita os exercícios da parte 1 (listas). Os elementos da lista filmes devem ser dicionários
#no seguinte formato: {'nome': <nome-do-filme>, 'ano': <ano do filme>},
#'sinopse': <sinopse do filme>} .


filme = {
    'primeiro' : {
        'nome' : 'Um Sonho de Liberdade',
        'ano' : '1994',
        'sinopse' : 'Dois homens presos se reúnem ao longo de vários anos, encontrando consolo e eventual redenção através de atos de decência comum.',
    },
    'segundo' : {
        'nome' : 'O Poderoso Chefão',
        'ano' : '1972',
        'sinopse' : 'O patriarca idoso de uma dinastia do crime organizado transfere o controle de seu império clandestino para seu filho relutante.',
    },
    'terceiro' : {
        'nome' : 'Batman - O Cavaleiro das Trevas',
        'ano' : '2008',
        'sinopse' : 'Agora com a ajuda do tenente Jim Gordon e do promotor público Harvey Dent, Batman tem tudo para banir o crime de Gotham City de uma vez por todas. Mas em breve, os três serão vítimas do Coringa, que pretende lançar Gotham em uma anarquia.',
    },
    'quarto' : {
        'nome' : 'O Poderoso Chefão II',
        'ano' : '1974',
        'sinopse' : 'Em 1950, Michael Corleone, agora à frente da família, tenta expandir o negócio do crime a Las Vegas, Los Angeles e Cuba. Paralelamente, é revelada a história de Vito Corleone, e de como saiu da Sicília e chegou a Nova Iorque.',
    },
    'quinto' : {
        'nome' : '12 Homens e uma Sentença',
        'ano' : '1957',
        'sinopse' : 'O julgamento de um assassinato em Nova Iorque é frustrado por um único membro, cujo ceticismo força o júri a considerar cuidadosamente as evidências antes de dar o veredito.',
    },
    'sexto' : {
        'nome' : 'A Lista de Schindler',
        'ano' : '1993',
        'sinopse' : 'Na Polônia ocupada pelos alemães durante a Segunda Guerra Mundial, o industrial Oskar Schindler começa a ser preocupar com seus trabalhadores judeus depois de testemunhar sua perseguição pelos nazistas.',
    },
    'cetimo' : {
        'nome' : 'O Senhor dos Anéis: O Retorno do Rei',
        'ano' : '2003',
        'sinopse' : 'Gandalf e Aragorn lideram o Mundo dos Homens contra o exército de Sauron para desviar o olhar de Frodo e Sam quando eles se aproximam á Montanha da Perdição com o Um Anel.',
    },
    'oitavo' : {
        'nome' : 'Pulp Fiction - Tempo de Violência',
        'ano' : '1994',
        'sinopse' : 'As vidas de dois assassinos da máfia, um boxeador, um gângster e sua esposa, e um par de bandidos se entrelaçam em quatro histórias de violência e redenção.',
    },
    'nono' : {
        'nome' : 'O Senhor dos Anéis: A Sociedade do Anel',
        'ano' : '2001',
        'sinopse' : 'Um manso hobbit do Condado e oito companheiros partem em uma jornada para destruir o poderoso Um Anel e salvar a Terra-média das Trevas.',
    },
    'decimo' : {
        'nome' : 'Três Homens em Conflito',
        'ano' : '1966',
        'sinopse' : 'Um impostor se junta com dois homens para encontrar fortuna num remoto cemitério.',
    }
}
