'''
numero = 1
limite = int(input("Digite até qual numero você quer contar: "))

while numero <= limite: #enquanto o numero for menor ou igual que 5
    print(numero) #exibe o numero

    #o simbolo de += serve para fazer uma soma com atribuição
    #numero += 1 ==> numero = numero + 1
    numero += 1 #soma 1 na variavel número
'''

#lower() transforma para minusculo
# print(nome.lower())

#upper() transforma para maiusculo
# print(nome.upper())

#startswith(stringBuscada) faz uma busca no inicio da palvra 
# print(nome.startswith('a')) #busca palavras que iniciam com 'a'

#endswith(stringBuscada) faz uma busca no final da palvra 
# print(nome.endswith('a')) #busca palavras que terminam com 'a'

while True:
    nome = input("Digite um nome: ")
    if nome.lower().startswith('a'): 
        print("Nome: ", nome)
    else:
        print("Nome não aceito!")


