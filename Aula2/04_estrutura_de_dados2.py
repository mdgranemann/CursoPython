# Tuplas
# O conjunto de dados não poderá ser alterado
tupla = (10,12,15,89,44,55)
print(tupla)
print(tupla[1])
print(tupla[1:3])
# Código abaixo gera exceção pois a tupla não permite alterações
# tupla[1] = 88
print(tupla)
lista_notas = [10,8,6,4]
# Criando uma tupla com tipos de dados diferentes, incluindo lista
tupla_aluno = ('Maykon', 'Dyego', 15, [10,8,6,4] )
# Modifincando o item da lista dentro da tupla
tupla_aluno[3][2] = 8 
print(tupla_aluno)

# Convertendo tupla em lista
lista_aluno = list(tupla_aluno)
print(lista_aluno)



# Dicionários
aluno = {'nome':'Maykon', 'sobrenome':'Granemann','idade': 15,'lista_notas':[10,8,6,4] }
aluno2 = {'nome':'Dyego', 'sobrenome':'Granemann','idade': 18,'lista_notas':[9,8,5,6] }
# Criando lista de dicionários
lista = [aluno,aluno2]
print(aluno)
print(aluno['nome'])
# Alterando dado do dicionário
aluno['nome'] = 'Tadeu'
print(aluno)
# Alterando dado da lista dentro do dicionário
aluno['lista_notas'][3] = 9
print(aluno)

# não é possivel acessar dados do dicionário pelo index
# print(aluno[0])

# Imprimindo lista de dicionários utilizando for
print('Imprimindo com for ....')
for a in lista:
    # imprimindo cada dado do dicionário através das chaves
    print(a['nome'])
    print(a['sobrenome'])
    print(a['idade'])
    print(a['lista_notas'])
