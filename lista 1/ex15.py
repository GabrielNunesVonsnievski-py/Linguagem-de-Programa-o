"15) Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
tela dizendo se está “quente”, “frio” ou “agradável”."
temperatura = float(input("Digite a temperatura atual:"))
if temperatura < 20:
    print(f"Esta uma temperatura fria")
if temperatura > 20:
    print(f"Esta temperatura está agradável")
if temperatura > 30:
    print(f"TA MUITO CALOR IRMÂO!!!!!!")
