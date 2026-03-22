import sqlite3;

conexao = sqlite3.connect('campeonato.db')

conexao.execute('''
CREATE TABLE IF NOT EXISTS CAMPEONATO(
id INTEGER PRIMARY KEY AUTOINCREMENT,
Clube TEXT,
Pontos INTEGER,
Vitorias INTEGER,
Empates INTEGER,
Derrotas INTEGER,
Jogos INTEGER,
Gols_marcados INTEGER,
Gols_sofridos INTEGER,
Saldo_gols INTEGER,
Aproveitamento DECIMAL)''')

conexao.commit()


def inserir():
    clube = input('Digite o nome do clube: ')
    vitorias = int(input('Digite a quantidade de vitorias: '))
    derrotas = int(input('Digite a quantidade de derrotas: '))
    empates = int(input('Digite a quantidade de empates: '))
    jogos = vitorias+empates+derrotas
    pontos = vitorias*3 + empates

    gols_marcados = int(input('Gols marcados: '))
    gols_sofridos = int(input('Gols sofridos: '))
    saldo = gols_marcados - gols_sofridos

    aproveitamento = (pontos/(jogos*3)) *100 if jogos > 0 else 0

    conexao.execute(
        'INSERT INTO CAMPEONATO VALUES (NULL,?,?,?,?,?,?,?,?,?,?)',
        (clube,pontos,vitorias,empates,derrotas,jogos,gols_marcados,gols_sofridos,saldo,aproveitamento)
        )
        
    conexao.commit()

    print(f'Clube {clube} inserido com sucesso!')

def consulta_clube ():
    nome = input('Digite o nome do clube: ')
    cursor = conexao.cursor()

    cursor.execute(
        'SELECT * FROM campeonato WHERE clube LIKE ?',(nome+'%',)
        )
    resultado = cursor.fetchall()

    if len(resultado) == 0:
        print('Nenhum clube encontrado!')

    else:
        header = ['ID', 'Clube', 'Pontos', 'Vitórias', 'Empates', 'Derrotas', 'Jogos',
          'Gols Marcados', 'Gols Sofridos', 'Saldo de Gols', 'Aproveitamento']

        print(f'{header[0]:<3} {header[1]:<10} {header[2]:<7} {header[3]:<8} {header[4]:<7} '
              f'{header[5]:<8} {header[6]:<5} {header[7]:<13} {header[8]:<13} {header[9]:<12} {header[10]:<13}')
    
        for x in resultado:
            print(f'{x[0]:<3} {x[1]:<10} {x[2]:<7} {x[3]:<8} {x[4]:<7} {x[5]:<8} {x[6]:<5} '
            f'{x[7]:<13} {x[8]:<13} {x[9]:<12} {x[10]:<6.2f}%')


    
        

def consulta_pontos():
    pontuacao = int(input('Pontos: '))
    cursor = conexao.cursor()

    cursor.execute(
        'SELECT Clube,Pontos FROM campeonato WHERE pontos >= ?', (pontuacao,)
        )
    resultado = cursor.fetchall()

    if len(resultado) == 0:
        print('Nenhum clube encontrado com essa pontuação')

    else:
        print('Clube\tPontos')
        for x in resultado:
            print(f'{x[0]}\t{x[1]}\t')

    

def consulta_aproveitamento():
    aproveitamento = float(input('Aproveitamento: '))
    cursor = conexao.cursor()

    cursor.execute(
        'SELECT Clube,Aproveitamento FROM campeonato WHERE Aproveitamento >= ?', (aproveitamento,)
        )
    resultado = cursor.fetchall()

    if len(resultado) == 0:
        print('Nenhum clube encontrado com esse aproveitamento')

    else:
        print('Clube\tAproveitamento')
        for x in resultado:
            print(f'{x[0]}\t{x[1]:.2f}%\t')

    
    
while True:
    print('\n----MENU----')
    print('1-Inserir Dados')
    print('2-Pesquisar Clube')
    print('3-Consultar Pontuação')
    print('4-Consultar Aproveitamento')
    print('5-Sair')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        inserir()

    elif escolha == '2':
        consulta_clube()

    elif escolha == '3':
        consulta_pontos()

    elif escolha == '4':
        consulta_aproveitamento()

    elif escolha == '5':
        print('Encerrando Programa...')
        break

    else:
        print('Opção Inválida! Tente Novamente')













        
