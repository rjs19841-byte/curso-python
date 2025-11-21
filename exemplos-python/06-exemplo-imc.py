import os

os.system("cls")

print("Exemplo IMC")
print("-------------------------------------------")

altura = float(input ("Escreva sua altura: "))

peso = float(input ("Escreva seu peso: "))

imc = peso / (altura * altura)

print("-------------------------------------------")
print ("Seu IMC é ", round(imc,2))