from time import sleep
import os

# Listas com palavras-chave de cada vaga
cientista_palavras = ['Python', 'Banco De Dados', 'Machine Learning', 'Resolução de problemas', 'Estatística']
analista_palavras = ['Python', 'Power Bi', 'SQL', 'Boa Comunicação']

candidatos_total     = {} # Dicionário que vai receber os candidatos inscritos
candidatos_analista  = {} # Dicionário que vai receber os candidatos inscritos para analista de dados
candidatos_cientista = {} # Dicionário que vai receber os candidatos inscritos para cientista de dados

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
            else:
                if vaga == '1':
                    candidatos_total[nome] = 'Analista de dados'
                elif vaga == '2':
                    candidatos_total[nome] = 'Cientista de dados'        
                resumo = input('Insira um pequeno resumo do currículo do participante: ')

    elif opcao == 4:
        print(f'Foram cadastrados {len(candidatos_total)} candidatos.')
        
    elif opcao == 5: # Sair do programa
        print(('programa encerrado.'))
        menu = False
