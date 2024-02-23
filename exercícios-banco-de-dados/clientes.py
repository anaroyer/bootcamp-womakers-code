import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE clientes (id INT, nome VARCHAR(100), idade INT, saldo FLOAT)')

conexao.commit()
conexao.close