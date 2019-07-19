nome = input("Digite o nome do aluno: ")

valid_nota = False

while valid_nota == False:
    nota1 = input("Digite nota da Prova 1: ")
    try:
        nota1 = float(nota1)
        if nota1 <0 or nota1 >10:
            print("Nota inválida. Use valores entre 0 e 10")
        else:
            valid_nota = True
    except:
        print("Nota inválida. Use apenas números e separe decimais com '.'")
    
valid_nota = False

while valid_nota == False:
    nota2 = input("Digite nota da Prova 2: ")
    try:
        nota2 = float(nota2)
        if nota2 <0 or nota2 >10:
            print("Nota inválida. Use valores entre 0 e 10")
        else:
            valid_nota = True
    except:
        print("Nota inválida. Use apenas números e separe decimais com '.'")

valid_faltas =  False
while valid_faltas == False:
    faltas = input("Digite o número de faltas: ")
    try:
        faltas = int(faltas)
        if faltas <0 or faltas >20:
            print("Número de faltas inválido. Use valores entre 0 e 20")
        else:
            valid_faltas = True
    except Exception as e::
        print("Númro de faltas inválido")

media = (nota1+nota2)/2
assid = (20-faltas)/20

if media >= 6 and assid >= 0.7:
    resultado = "Aprovado"
elif media < 6 and assid < 0.7:
    resultado = "Reprovado por média e por faltas."
elif media < 6:
    resultado = "Reprovado por média."
elif assid < 0.7:
    resultado =  "Reprovado por faltas."
else:
    print("Erro")

print("Nome: ",nome)
print("Média: ",media)
print("Assiduidade: ",str(assid*100)+'%')
print("Resultado: ", resultado)