"4) Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre
ele."

dado = input("Digite algo para saber todos os seus dados:")
print(type(dado))

print(f"Numéricos",dado.isalnum())
print(f"String",dado.isalpha())
print(f"Decimal",dado.isdecimal())
print(f"É um digito",dado.isdigit())
print(f"Está em caixa baixa",dado.islower())
print(f"Está em caixa alta",dado.isupper())
