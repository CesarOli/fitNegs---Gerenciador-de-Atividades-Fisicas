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



def criarTabelaAlunos(conexao):
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Alunos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(150), idade INT, endereco VARCHAR(200), email VARCHAR(100))')
    cursor.close()

def inclusaoColunaSexo(conexao):
    if not tabelaExiste(conexao, 'Alunos'):
        cursor = conexao.cursor()
        cursor.execute('ALTER TABLE Alunos ADD COLUMN sexo VARCHAR(1)')
        cursor.execute('UPDATE Alunos SET verificado = TRUE')
        cursor.close()
        print('Coluna "sexo" adiciona com sucesso.')

def verificaColunaNaTabela(conexao, tabela, *colunas):
    cursor = conexao.cursor()
    cursor.execute(f'SHOW COLUMNS FROM {tabela}')
    colunaNaTabela = [coluna[0] for coluna in cursor.fetchall()]
    cursor.close()

    for coluna in colunas:
        if coluna not in colunaNaTabela:
            return False
    return True 

def inserirAluno(conexao):
    cursor = conexao.cursor()
    nome = input('Diga o nome do Aluno que deseja cadastrar: ')
    idade = input('Informe a idade do aluno: ')
    endereco = input('Qual endereço do aluno, somente a rua:  ')

    while True: 
        sexo = input('Informe o sexo do aluno (M/F): ').upper()
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print('Opção inválida, digite M para masculino ou F para Feminino.')
        
    email = input('Digite o email do aluno: ')
        
    cursor.execute('INSERT INTO  Alunos (nome, idade, endereco, sexo, email) VALUES (%s, %s, %s, %s, %s)', (nome, idade, endereco, sexo, email))
    conectar.commit()
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
    criarTabelaAlunos(conectar)
    inclusaoColunaSexo(conectar)
    inserirAluno(conectar)
    conectar.commit()

    while True:
        print('======= MENU DE OPÇÕES =======')
        print('1. Cadastrar Novo Aluno')
        print('2. Visualizar Alunos Cadastrados')
        print('3. Atualizar Alunos Cadastrados')
        print('4. Deletar Aluno')
        print('0. Sair')

        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            inserirAluno(conectar)
        elif opcao == '2':
            #implementar
            pass
        elif opcao == '3':
            #implementar
            pass
        elif opcao == '4':
            #implementar
            pass
        elif opcao == '0':
            sleep(2.5)
            print('Saindo do programa...')
            break
        else:
            sleep(1.5)
            print('Oção inválida. Digite um número válido.')

if conectar:
    conectar.close()
