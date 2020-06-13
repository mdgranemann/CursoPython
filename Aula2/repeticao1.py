# Estrutura de repetição FOR

# Estrutu de código repetida
# print('Aluno', 1)
# print('Aluno', 2)
# print('Aluno', 3)
# print('Aluno', 4)
# print('Aluno', 5)

# Laço for com a funcao range de 1-5
for i in range(1,6):
    print('Aluno', i)

# Laço for com a função range apenas com limite final
for i in range(5):
    print('Aluno', i+1)

# cadastro com repetição
for i in range(2):
    nome = input('Digite seu nome:')
    sobrenome = input('Digite seu sobrenome:')
    idade = int( input('Digite sua idade:') )
    print("Usuario cadastrado:\n", nome, sobrenome,'Idade:',idade)