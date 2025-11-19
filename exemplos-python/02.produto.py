#Utilizado para executar comandos no cmd
import os

#limpando a tela
os.system("cls")

nome_produto = input("Digite o nome do produto: ")
preco = float (input("Digite o preço do produto: "))
desconto = float (input("Digita o percentual do desconto: "))

#calcular o desconto
valor_desconto = preco * desconto / 100

#calculando o preço final
preco_final = preco - valor_desconto

#exibir o preço final
print(f"produto: {nome_produto} - Preco final: R$ {preco_final}")
