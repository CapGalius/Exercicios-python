#Cálculo de IMC

print("----Cálculo de IMC -----")
print("-"*25)
print("---Insira seus dados:---")

nome = input("Insira seu nome: ").capitalize
print("Insira seu peso e altura. Use ponto '.' para decimais")
while True:
    try:
        peso = float(input("Insira seu peso: "))
        altura = float(input("Insira sua altura: "))
        sexo = int(input(" Digite 1 para Mas. ou 2 para Fem."))
        break
    except Exception as e:
        print("Dados errados. Repita a operação!")
    
def CIMC():
    if sexo == 1:
        lista = [20.7, 26.4, 27.8, 31.1]
    elif sexo == 2:
        lista = [19.1, 25.8, 27.3, 32.3]
    
    imc = peso / (altura**2)
    print("-"*25)
    print("O valor de seu IMC é {:.2f}".format(imc))
    print("-"*25)
    
    if imc < lista[0]:
        print(nome,":está abaixo do peso.")
    elif lista[0] < imc < lista[1]:
        print(nome,"Seu peso está normal.")
    elif lista[1] < imc < lista[2]:
        print(nome,"Seu peso está um  pouco acima do normal.")
    elif lista[2] < imc < lista[3]:
        print(nome,"Seu peso está acima do ideal.")
    elif imc > lista[3]:
        print(nome,"Você está obeso.")

CIMC()