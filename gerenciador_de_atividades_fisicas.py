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

conectar.close()