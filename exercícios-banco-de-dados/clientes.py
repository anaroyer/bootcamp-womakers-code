import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
cursor.execute('CREATE TABLE clientes (id INT, nome VARCHAR(100), idade INT, saldo FLOAT)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "Marcos", 34, 3050.0)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, "Gabriel", 31, 1700.0)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, "Rodrigo", 39, 450.0)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, "Isabela", 27, 5600.0)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (5, "Maria", 24, 120.0)')

# 6 a) Selecione o nome e a idade dos clientes com idade superior a 30 anos
dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
for linha in dados:
    print(linha)
# b) Calcule o saldo médio dos clientes
dados =  cursor.execute('SELECT saldo FROM clientes')
saldo_sum = 0
i = 0
for linha in dados:
    saldo_sum += linha[0]
    i += 1


saldo_medio = saldo_sum / i
print(saldo_medio)

# c) Encontre o cliente com o saldo máximo
dados = cursor.execute('SELECT saldo FROM clientes ORDER BY saldo')
for linha in dados:
    print(linha)

# d) Conte quantos clientes têm saldo acima de 1000
dados = cursor.execute('SELECT * FROM clientes WHERE saldo > 1000')
contagem = 0
for linha in dados:
    contagem +=1
print(contagem)

# 7 a) Atualize o saldo de um cliente específico
cursor.execute('UPDATE clientes SET saldo= 300.0 WHERE nome = "Maria"')

# b) Remova um cliente pelo seu ID
cursor.execute('DELETE FROM clientes WHERE id=2')

# 8 Junção de tabelas
"""Crie uma segunda tabela chamada "compras" com os campos: id
(chave primária), cliente_id (chave estrangeira referenciando o id
da tabela "clientes"), produto (texto) e valor (real). Insira algumas
compras associadas a clientes existentes na tabela "clientes".
Escreva uma consulta para exibir o nome do cliente, o produto e o
valor de cada compra. """
cursor.execute('CREATE TABLE compras (id INT, cliente_id INT, produto VARCHAR(100), valor FLOAT)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 3, "Skate", 350.0)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 5, "Camiseta", 109.0)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (3, 1, "Lego", 790.0)')

dados = cursor.execute('SELECT nome, produto, valor FROM clientes LEFT JOIN compras ON clientes.id = compras.cliente_id')
for linha in dados:
    print(linha)


dados = cursor.execute('SELECT nome, produto, valor FROM clientes FULL JOIN compras ON clientes.id = compras.cliente_id')
for linha in dados:
    print(linha)



conexao.commit()
conexao.close