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
candidatos_analista  = {} # Dicionário que vai receber os candidatos inscritos para analista de dados {nome : resumo}
candidatos_cientista = {} # Dicionário que vai receber os candidatos inscritos para cientista de dados {nome : resumo}

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
                    palavra_chave(analista_palavras, resumo, candidatos_analista)
                    
                elif vaga == '2':
                    candidatos_total[nome] = 'Cientista de dados'        
                    resumo = input('Insira um pequeno resumo do currículo do participante para a vaga de Cientista de dados: ').title()
                    palavra_chave(cientista_palavras, resumo, candidatos_cientista)
            
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
                palavra_chave(analista_palavras, resumo, candidatos_analista)
                sleep(0.5)
                print('Candidato adicionado!')
            elif vaga == '2':
                candidatos_total[nome] = 'Cientista de dados'        
                resumo = coluna[2].title()
                palavra_chave(cientista_palavras, resumo, candidatos_cientista)
                sleep(0.5)
                print('Candidato adicionado!')
            sleep(1)
    elif opcao == 3: # opção que remove o ultimo candidato cadastrado
        if len(candidatos_total) != 0:
            remove = candidatos_total.popitem()
            print(f'O ultimo candidato foi: {remove[0]}')
            print(f'Removendo...')
            sleep(2)
            if remove[0] in candidatos_analista:
                candidatos_analista.pop(remove[0])
            if remove[0] in candidatos_cientista:
                candidatos_cientista.pop(remove[0])
        else:
            print('Nenhum candidato cadastrado.')
            sleep(2.5)
    elif opcao == 4: # Opção que mostra os resultados
        print(f'Candidatos cadastrados: {len(candidatos_total)}\nCandidatos para analistas de dados: {len(candidatos_analista)}\nCandidatos para cientista de dados: {len(candidatos_cientista)}\n{len(candidatos_total) - (len(candidatos_analista) + len(candidatos_cientista))} Não cumpriram os requisitos das palavras chaves')
        print(f'Candidatos para Analistas de dados: {list(candidatos_analista.keys())}')
        print(f'Candidatos para Cientistas de dados: {list(candidatos_cientista.keys())}')
        if encerrar_menu() == False:
            menu = False
    elif opcao == 5: # Sair do programa
        print(('programa encerrado.'))
        menu = False
    else:
        print('Por favor, digite uma opção válida.')
        sleep(2.5)