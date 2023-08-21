"7) Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15%
de aumento."


produto = float(input(f"Digite o valor do produto: "))
desconto = produto - (produto * 0.05)
aumento = produto + (produto * 0.15)
print(f"O aumento de preço foi para:",aumento)
print(f"O desconto de preço foi para:",desconto)
