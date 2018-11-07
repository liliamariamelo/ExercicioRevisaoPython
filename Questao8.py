notas_lidas = 0
lista_notas = []
lista_reversa = []
while True:
  nota_X= int(input("Digite uma nota: "))

  if nota_X == -1:
    break
  
  notas_lidas += 1
  lista_notas.append(nota_X)
  lista_reversa = lista_notas[::-1]

print("")
print("A) A quantidade valores lidos foi: %d\n"%(notas_lidas))

print("B) Os valores na ordem que foram informados:")
for i in range(len(lista_notas)):
  print(lista_notas[i], end = " ")

print("")

print("")
print("C) Os valores na ordem inversa que foram informados um abaixo do outro:")
for j in range(len(lista_reversa)):
  print(lista_reversa[j], end = " ",)
  print("")

print("")
somaVetor = 0
for k in range(len(lista_notas)):
  somaVetor += lista_notas[k]

print("D) A soma dos valores dos elementos do vetor eh: %d\n" %(somaVetor))
print("E) A media dos valores do elementos do vetor eh: %d\n"%(somaVetor/len(lista_notas)))

acima_Media = 0
for l in range(len(lista_notas)):
  if lista_notas[l] > somaVetor/len(lista_notas):
    acima_Media +=1

print("F) A quantidade de valores acima da media eh: %d\n"%(acima_Media))

abaixoSete = 0
for m in range(len(lista_notas)):
  if lista_notas[m] < 7:
    abaixoSete+=1

print("G) A quantidade de valores abaixo de sete eh: %d\n"%(abaixoSete))

print("H) Programa finalizado!") 