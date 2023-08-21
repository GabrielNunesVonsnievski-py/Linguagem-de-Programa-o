"1) Faça um script que leia dois números e retorne como resultado a soma deles. Faça um script que leia algo
pelo teclado e mostra na tela o seu tipo de dado"

a = int(input(f"Digite um Número: "))
b = int(input(f"Digite outro Número: "))

print(f"A soma desses Números é",a + b)

dado = input(f"Digite algo pra saber seu tipo: ")
print(type(dado))
print(f"Alphanumerico",dado.isalpha())
print(f"Decimal",dado.isdecimal())
print(f"Lower",dado.islower())
print(f"Upper",dado.isupper())
print(f"Float",dado.isalnum())
