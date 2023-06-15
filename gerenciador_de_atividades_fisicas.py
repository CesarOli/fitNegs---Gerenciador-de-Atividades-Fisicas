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

cursor = conectar.cursor()

cursor.execute('''
    CREATE TABLE atividadesFisicas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        atividade_fisica VARCHAR(150),
        tempo_da_atividade TIME,
        distancia DECIMAL(8,2),
        calorias_queimadas INT,
        data_da_atividade DATE,
        hora_da_atividade TIME
    )
''')

conectar.close()
