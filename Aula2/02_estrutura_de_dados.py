idade = 151
lista_idades = [18,19,50,19,50,41,13,89,74]

print(idade)
# Imprimindo lista toda
print(lista_idades)
#imprimindo um item especifico da lista
print(lista_idades[1])

# Removendo um item da lista com a função remove
# remove a primeira ocorrencia do dado
lista_idades.remove(19)
print(lista_idades)

# Removendo dado com a função pop - 
# função remove pela posição do dado e retorna o valor do dado
retorno_do_pop = lista_idades.pop(1)
print(lista_idades)
print(retorno_do_pop)

# Removendo todos os dados da lista
#lista_idades.clear()

# Adicionando dados na lista com append
# adiciona o dado ao final da lista
lista_idades.append(idade)
lista_idades.append(18)
print(lista_idades)

# Mostrando o número de instancias do dado na lista
print( lista_idades.count(18) )

# Mostrando o número total de dados da lista
print( len(lista_idades) )

#------------ Fatiamento de lista
# Imprimindo os 3 primeiros itens
print(lista_idades[:3])
# Imprimindo os 3 ultimos itens
index_antepenultimo_item = len(lista_idades)-3
print( lista_idades[ index_antepenultimo_item : ] )
# Imprimindo dados do meio da lista
print( lista_idades[2:4])

print(lista_idades)
lista_idades.reverse()
print(lista_idades)

# Inserindo um dado em uma posição específica da lista
lista_idades.insert(2,152)
print(lista_idades)

# Inserindo o numero 153 apos o 152
index = lista_idades.index(152)
lista_idades.insert(index + 1, 153)
print(lista_idades)

