from time import sleep
import os

def encerrar_menu(): # Função que encerra o menu
    voltar = int(input('Deseja encerrar o programa?\n[1] Sim\n[2] Não\nDigite aqui:'))
    if voltar == 1:
        print(('programa encerrado.'))
        return False

def palavra_chave(lista, curriculo, dicionario):
    for palavra in lista:
        if palavra in curriculo:
            dicionario[nome] = curriculo

# Listas com palavras-chave de cada vaga
cientista_palavras = ['Python', 'Banco De Dados', 'Machine Learning', 'Resolução De Problemas', 'Estatística']
analista_palavras = ['Python', 'Power Bi', 'SQL', 'Boa Comunicação']

candidatos_total     = {} # Dicionário que vai receber os candidatos inscritos {nome : vaga}
candidatos_analista  = {} # Dicionário que vai receber os candidatos inscritos para analista de dados {nome : resumo}
candidatos_cientista = {} # Dicionário que vai receber os candidatos inscritos para cientista de dados {nome : resumo}

menu = True

while menu == True:

    os.system('cls')
    opcao = int(input('O que deseja fazer?\n[1] Inserir candidatos\n[2] Ler arquivo .csv\n[3] Deletar o ultimo candidato cadastrado\n[4] Verificar resultados\n[5] Sair do programa\nDigite aqui:'))

    if opcao == 1: # Opção de inserir candidatos 
        sleep(0.5)
        os.system('cls')
        candidatos = int(input('Quantos candidatos serão cadastrados? '))
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
            print(candidatos_total)
            print(candidatos_analista)
            print(candidatos_cientista)
    elif opcao == 4:
        print(f'Foram cadastrados {len(candidatos_total)} candidatos.')
        
    elif opcao == 5: # Sair do programa
        print(('programa encerrado.'))
        menu = False

print(candidatos_total)
print(candidatos_analista)
print(candidatos_cientista)