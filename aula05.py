idades = [15, 25, 26, 30, 40] #criando uma lista => [], essa lista tem 5 itens e 4 posições (0 a 4)

print('Lista: ', idades) #exibindo a lista

print('Posição 0: ')
print([0]) #exibe a posição 0 da lista
print('Posição 2: ')
print([2]) #exibe a posição 2 da lista
print('Posição 4: ')
print([4]) #exibe a posição 4 da lista

idades[2] = 25

print(idades)

# determinar o tamanho da lista, onde n é o nome da lista analisada
print(len(idades))

#inserindo novo item no final da lista
idades.append(50)
print("append(50): ", idades)

#inserindo novo item em uma posição desejada, onde o primeiro valor é a posição e o segundo é o item a ser inserido
idades.insert(0, 1)
idades.insert("0, 1: ", idades)

# remove um item por valor na lista
idades.remove(30)
print("remove(30): ", idades)

# remove um item por posição da lista
del idades[1]
print("idades[1]: ", idades)

# somar todos os valores de uma lista => sum()
soma = sum(idades)
print("Soma todos os valores dentro da lista", soma)

#slicing: fatia a lista em uma menor com base no intervalo
novaLista = idades[2:5]
print("idades[2:5]: ", novaLista)

# posição inversa 
print("idades[-1]: ", idades[-1])
print("idades[-4]: ", idades[-4])
print("idades[-5]: ", idades[-5])
print("idades[-6]: ", idades[-6])

# invertendo uma lista
idades_inversa = idades[::-1]
print("idades inversa: ", idades_inversa)

# ordenando uma lista
idades_ordenadas = sorted(idades_inversa)
print("Idades ordenadas=>sorted(idades_inversa): ", idades_ordenadas)

nova_lista = [30,20,80,1,50]

crescente = sorted(nova_lista)
print('Crescente: ', crescente)

# reverse=True faz com que a lista seja ordenada de forma decrescente
decrescente = sorted(nova_lista, reverse=True)
print('Decrescente: ', decrescente)