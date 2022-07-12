cientista_palavras = ['Python', 'Banco De Dados', 'Machine Learning', 'Resolução de problemas', 'Estatística']
analista_palavras = ['Python', 'Power Bi', 'SQL', 'Boa Comunicação']

candidatos_total = {}

candidatos = int(input('Quantos candidatos serão cadastrados? '))

for candidato in range (candidatos, 0, -1):
    nome = input('Qual o nome completo do candidato? ')

    vaga = input('Para qual vaga o candidato está se escrevendo?\n[1] Analista de Dados\n[2] Cientista de dados\nDigite aqui: ')
    if vaga != '1' and vaga != '2':
        print('Vaga não disponível! Por favor, selecione uma das opções.')
    else:
        if vaga == '1':
            candidatos_total[nome] = 'Analista de dados'
        elif vaga == '2':
            candidatos_total[nome] = 'Cientista de dados'        
        resumo = input('Insira um pequeno resumo do currículo do participante: ')
