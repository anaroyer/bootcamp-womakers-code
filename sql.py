import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(60), idade INT, curso VARCHAR(100))')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Marcos", 22, "Medicina")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "Isabela", 24, "Fisioterapia")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "Gustavo", 27, "Educação Física")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "Gabriela", 20, "Medicina")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "Maria", 23, "Direito")')

#3 a) Selecionar todos os registros da tabela "alunos".

dados = cursor.execute('SELECT * FROM alunos')
for linha in dados:
    print(linha)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
for linha in dados:
    print(linha)

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

dados = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')
for linha in dados:
    print(linha)

# d) Contar o número total de alunos na tabela
dados = cursor.execute('SELECT * FROM alunos')
num_alunos = 0
for linha in dados:
    num_alunos += 1
print(num_alunos)

#4 a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade=25 WHERE nome="Isabela"')

# b) Remova um aluno pelo seu ID
cursor.execute('DELETE FROM alunos WHERE id=3')

conexao.commit()
conexao.close