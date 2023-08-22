""" 20) Leia a idade e o tempo de servic¸o de um trabalhador e escreva se ele pode ou nao se aposentar.
As condições para aposentadoria são:
• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos. """

idade = int(input(f"Digite sua idade: "))
tempodeserviço = int(input(f"Digite o seu tempode serviço em anos: "))

if (idade > 65):
    print(f"Você ja pode se aposentar")
else:
    print(f"Você não pode se aposentar")

if tempodeserviço >= 30:
    print(f"Você pode se aposentar")
else:
    print(f"Você não pode se aposentar")

if idade >= 60 and tempodeserviço >= 25:
    print(f"Você ja pode se aposentar")
else:
    print(f"Você não pode se aposentar")