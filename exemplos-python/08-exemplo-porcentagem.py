import os

os.system("cls")

print("Exemplo de Porcentagem ")

valor_total = float (input("Digite o valor total: "))
porcentagem = float (input("Digite a porcentagem: "))

valor_parte = valor_total *(porcentagem / 100)

print("Valor do desconto: ",valor_parte)

