"6) Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode
comprar."

carteira = float(input("Digite o valor de reais em sua carteira: "))
dollar = carteira /5.41

print(f"Com esse dinheiro na sua carteira você pode comprar {round(dollar, 2)} dólares.")
