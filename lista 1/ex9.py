"9) Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
Euros."

nome = input(f"Digite seu nome: ")
dinheiro = int(input(f"Digite a quantia do seu dinheiro: "))
dollar = dinheiro * 4,98
euro = dinheiro * 5,43
print(f"O valor em Dóllares é: ",dollar)
print(f"O valor em Euros é: ",euro)
