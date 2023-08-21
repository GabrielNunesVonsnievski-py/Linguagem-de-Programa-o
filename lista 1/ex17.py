temperatura = float(input("Digite a temperatura que deseja reverter: "))
escolha = int(input(f"Escolha 1-Fahrenheit para Celsius\n 2-Celsius para Fahrenheit:"))


if (escolha == 1):
    print((temperatura - 32) /1.8)
if (escolha == 2):
    print(temperatura + 273)