# programa de exercícios

print("----------------------------------------")
print("------------------Programa--------------")
print("---------------------de-----------------")
print("-------------------Vendas---------------")
print("----------------------------------------")

fatura = []
venda = 0
total = 0
 
print(" Aperte 1 para venda.")
print(" Aperte 2 para final.")
venda = int(input("Digite a opção: "))
while venda == 1:
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    fatura.append([produto,preco])       
    total += preco
    venda = int(input("Deseja comprar mais um produto? (1-SIM) (2-NÃO)"))

print("Seus produtos comprados foram: ")
for i in fatura:
    print(i[0],"-","R$",i[1])
print(f"O total de sua fatura foi R$",total)
if venda == 2:
    print("Venda encerrada")
