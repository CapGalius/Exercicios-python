# programa de exercícios

print("-------------------------------------------------")
print("-----------------------Programa------------------")
print("--------------------------de---------------------")
print("------------------------Vendas-------------------")
print("-------------------------------------------------")

fatura = []
total = 0
venda = ""
iniciochk = False

print("Aperte 1 para venda.")
print("Aperte 2 para final.")

while iniciochk == False:
    try:
        venda = int(input("Digite a opção: "))
    except ValueError:
        print("Digite apenas 1 para venda ou 2 para encerrar.")
    try:
        if venda == 1 or venda == 2:
            iniciochk = True
            break
     
    except ValueError:
        print("Digite apenas 1 para venda ou 2 para encerrar.")
        iniciochk = False  
        
while venda is not 2:
    try:    
        produto = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        fatura.append([produto,preco])       
        total += preco
        venda = int(input("Deseja comprar mais um produto? (1-SIM) (2-NÃO)"))
    except ValueError:
        print("Repita a operação. No campo preço")
        print("insira somente números.  Centavos use '.' ")
        
print("Seus produtos comprados foram: ")
print("-"*50)
for i in fatura:
    print(i[0],"-","R$",i[1])
print(f"O total de sua fatura foi R$",total)
if venda == 2:
    print("Venda encerrada")
