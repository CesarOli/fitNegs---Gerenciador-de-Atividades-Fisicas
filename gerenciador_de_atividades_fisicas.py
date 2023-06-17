import mysql.connector
from time import sleep

config = { 
    'host': 'localhost',
    'user': 'CesarOli',
    'password': '6joiasthanos',
    'database': 'Gerenciador_de_Atividades_Fisicas'
}

conectar = mysql.connector.connect(**config)

if conectar.is_connected():
    sleep(2)
    print('Conexão ao banco de dados realizada com sucesso.')
else:
    sleep(2)
    print('Falha na conexão.')

def tabelaExiste(conexao, tabela):
    cursor = conexao.cursor()
    cursor.execute(f'SHOW TABLES LIKES "{tabela}"')
    resultado = cursor.fetchone()
    cursor.close()
    return resultado is not None
    
'''def dadosDasAtividades():
    atividade = input('Informe a atividade praticada: ')
    tempo = input('Informe o tempo de duração desta atividade (HH:MM) : ')
    distancia = float(input('Informe a distancia percorrida nesta atividade: '))
    calorias = int(input('Informe a quantidade de calorias queimadas nesta atividade: '))
    data = input('Informe a data da atividade: ')
    hora = input('Informe a hora em que você realizou esta atividade: ')

    return atividade, tempo, distancia, calorias, data, hora'''

conectar.close()
