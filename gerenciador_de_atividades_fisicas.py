import mysql.connector
from time import sleep

config = { 
    'host': 'localhost',
    'user': 'CesarOli',
    'password': '6joiasthanos',
    'database': 'Gerenciador_de_Atividades_Fisicas'
}

conectar = None

def conectarBancoDados():
    global conectar
    conectar = mysql.connector.connect(**config)
    if conectar.is_connected():
        sleep(2)
        print('Conexão ao banco de dados realizada com sucesso.')
    else:
        sleep(2)
        print('Falha na conexão.')

def tabelaExiste(conexao, tabela):
    cursor = conexao.cursor()
    cursor.execute(f'SHOW TABLES LIKE "{tabela}"')
    resultado = cursor.fetchone()
    cursor.close()
    return resultado is not None

def usarTabelaAtividades(conexao):
    cursor = conectar.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS Gerenciador_de_Atividades_Fisicas')
    cursor.execute('USE Gerenciador_de_Atividades_Fisicas')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS atividadesFisicas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            atividade_fisica VARCHAR(150),
            tempo_da_atividade TIME,
            distancia DECIMAL(8,2),
            calorias_queimadas INT,
            data_da_atividade DATE,
            hora_da_atividade TIME
        )
    ''')
    cursor.close()

while True:
    escolha = input('Deseja fazer conexão ao Banco de Dados? (S/N): ')
    if escolha.upper() == 'S':
        conectarBancoDados()
        break
    elif escolha.upper() == 'N':
        break
    else:
        print('Opção inválida. Digite S para sim ou N para não.')

if conectar:
    usarTabelaAtividades(conectar)
    atividade, tempo, distancia, calorias, data, hora = dadosDasAtividades()
    conectar.commit()

if conectar:
    conectar.close()
