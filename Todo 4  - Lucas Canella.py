from time import sleep
import csv
import os

def encerrar_menu(): # Função que encerra o menu
    voltar = int(input('Deseja encerrar o programa?\n[1] Sim\n[2] Não\nDigite aqui:'))
    if voltar == 1:
        print(('programa encerrado.'))
        return False

def palavra_chave(lista, curriculo, dicionario): # Função que checa se o resumo do curriculo do candidato possui alguma das palavras chaves necessárias para a vaga.
    for palavra in lista:
        if palavra in curriculo:
            dicionario[nome] = curriculo

# Listas com palavras-chave de cada vaga
cientista_palavras = ['Python', 'Banco De Dados', 'Machine Learning', 'Resolução De Problemas', 'Estatística']
analista_palavras = ['Python', 'Power Bi', 'Sql', 'Boa Comunicação']

candidatos_total     = {} # Dicionário que vai receber os candidatos inscritos {nome : vaga}
candidatos_analistas = {}
candidatos_cientistas = {}
analista_palavra_chave  = {} # Dicionário que vai receber os candidatos inscritos para analista de dados que possuem palavra chave {nome : resumo}
cientista_palavra_chave = {} # Dicionário que vai receber os candidatos inscritos para cientista de dados que possuem palavra chave {nome : resumo}

menu = True

while menu == True:

    os.system('cls')
    opcao = int(input('O que deseja fazer?\n[1] Inserir candidatos\n[2] Ler arquivo .csv\n[3] Deletar o ultimo candidato cadastrado\n[4] Verificar resultados\n[5] Sair do programa\nDigite aqui:'))
    os.system('cls')
    if opcao == 1: # Opção de inserir candidatos 
        sleep(0.5)
        candidatos = input('Quantos candidatos serão cadastrados?')
        if candidatos.isnumeric() == False:
            print('Digite um número! Resetando o programa...')
            sleep(2.5)
        else:
            candidatos = int(candidatos)
            for candidato in range (candidatos, 0, -1):

                nome = input('Qual o nome completo do candidato? ')
                vaga = input('Para qual vaga o candidato está se escrevendo?\n[1] Analista de Dados\n[2] Cientista de dados\nDigite aqui: ')

                if vaga != '1' and vaga != '2':
                    print('Vaga não disponível! Por favor, selecione uma das opções.')
                    if encerrar_menu() == False:
                        menu = False

                elif vaga == '1':
                    candidatos_total[nome] = 'Analista de dados'
                    resumo = input('Insira um pequeno resumo do currículo do participante para a vaga de Analista de dados: ').title()
                    candidatos_analistas[nome] = resumo
                    palavra_chave(analista_palavras, resumo, analista_palavra_chave)
                    
                elif vaga == '2':
                    candidatos_total[nome] = 'Cientista de dados'
                    resumo = input('Insira um pequeno resumo do currículo do participante para a vaga de Cientista de dados: ').title()
                    candidatos_cientistas[nome] = resumo
                    palavra_chave(cientista_palavras, resumo, cientista_palavra_chave)
            
                sleep(0.5)
                os.system('cls')
    elif opcao == 2: # opção que lê um arquivo .csv
        with open('.\lucasCanellaDados.csv', mode = 'r') as arq: # É necessário salvar o arquivo .csv na mesma pasta que este arquivo e em uma pasta na área de trabalho
            leitor = csv.reader(arq, delimiter=';')
            linha = 1
            for coluna in leitor:
                if linha > 0:
                    nome = coluna[0]
            vaga = str(coluna[1])
            if vaga != '1' and vaga != '2':
                print('Vaga não disponível! Por favor, selecione uma das opções.')
                if encerrar_menu() == False:
                    menu = False

            elif vaga == '1':
                candidatos_total[nome] = 'Analista de dados'
                resumo = coluna[2].title()
                candidatos_analistas[nome] = resumo
                palavra_chave(analista_palavras, resumo, analista_palavra_chave)
                sleep(0.5)
                print('Candidato adicionado!')
            elif vaga == '2':
                candidatos_total[nome] = 'Cientista de dados'     
                resumo = coluna[2].title()
                candidatos_cientistas[nome] = resumo 
                palavra_chave(cientista_palavras, resumo, cientista_palavra_chave)
                sleep(0.5)
                print('Candidato adicionado!')
            sleep(1)
    elif opcao == 3: # opção que remove o ultimo candidato cadastrado
        if len(candidatos_total) != 0:
            remove = candidatos_total.popitem()
            print(f'O ultimo candidato foi: {remove[0]}')
            print(f'Removendo...')
            sleep(2)
            if remove[0] in analista_palavra_chave:
                analista_palavra_chave.pop(remove[0])
                candidatos_analistas.pop(remove[0])
            if remove[0] in cientista_palavra_chave:
                cientista_palavra_chave.pop(remove[0])
                candidatos_cientistas.pop(remove[0])
        else:
            print('Nenhum candidato cadastrado.')
            sleep(2.5)
    elif opcao == 4: # Opção que mostra os resultados
        print(f'Candidatos cadastrados: {len(candidatos_total)}')
        print('')
        print(f'Candidatos para analistas de dados: {len(candidatos_analistas)} - {len(analista_palavra_chave)} possuem alguma palavra chave no currículo.')
        print(f'Candidatos Analistas de dados que possuem palavra chave: {list(analista_palavra_chave.keys())}')
        print('')
        print(f'Candidatos para Cientista de dados: {len(candidatos_cientistas)} - {len(cientista_palavra_chave)} possuem alguma palavra chave no currículo.')
        print(f'Candidatos para Cientistas de dados que possuem palavra chave: {list(cientista_palavra_chave.keys())}')
        print('')
        ver_resultado = input('Deseja saber mais sobre algum candidato?\nDigite o nome dele(a) ou digite 0 para encerrar o programa: ')
        if ver_resultado == '0':
            if encerrar_menu() == False:
                menu = False
        elif ver_resultado in analista_palavra_chave:
            print('\n', ver_resultado ,':', candidatos_total[ver_resultado])
            print(analista_palavra_chave[ver_resultado], '\n')
            if encerrar_menu() == False:
                menu = False
        elif ver_resultado in cientista_palavra_chave:
            print('\n', ver_resultado ,':', candidatos_total[ver_resultado])
            print(cientista_palavra_chave[ver_resultado], '\n')
            if encerrar_menu() == False:
                menu = False
        else:
            print('Esse usuário não está cadastrado para nenhuma das vagas!')
            if encerrar_menu() == False:
                menu = False
    elif opcao == 5: # Sair do programa
        print(('programa encerrado.'))
        menu = False
    else:
        print('Por favor, digite uma opção válida.')
        sleep(2.5)