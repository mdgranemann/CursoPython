
lista_alunos = []

for i in range(2):
    dict_aluno = {}
    dict_aluno['nome'] = input('Digite o nome:')
    dict_aluno['sobrenome'] = input('Digite o sobrenome:')
    dict_aluno['idade'] = input('Digite a idade:')
    lista_alunos.append(dict_aluno)

for a in lista_alunos:
    print('Usuário cadastrado:', a['nome'], a['sobrenome'], a['idade'])