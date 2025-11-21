import os

os.system("cls")

print("Exemplos de desconto")
print("----------------------------------")

preco_real = float(input("Digite o preço original do produto:"))
desconto = float(input("Digite porcentagem do desconto: "))

desconto = preco_real * (desconto /100)

print("Valor do desconto ",desconto)
print("Preço fnal com desconto: ", desconto)

