"16) Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
conversão."

temperatura = float(input("Digite a temperatura que deseja reverter: "))
escolha = int(input(f"Escolha 1-Fahrenheit para Celsius\n 2-Celsius para Fahrenheit:"))


if (escolha == 1):
    print((temperatura - 32) /1.8)
if (escolha == 2):
    print(temperatura + 273)
