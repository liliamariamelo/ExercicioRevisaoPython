lista_1 = []
lista_2 = []

for i in range(10):
  valores_1 = int(input("Digite o Valor para ser adicionado a primeira lista: "))
  lista_1.append(valores_1)
print("======SEGUNDA LISTA======")
for i in range(10):
  valores_2 = int(input("Digite o Valor para ser adicionado a segunda lista: "))
  lista_2.append(valores_2)


lista_3 = []
for i in range(10):
  lista_3.append(lista_1[i])
  lista_3.append(lista_2[i])

print("Lista Final:",lista_3)