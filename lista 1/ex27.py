""" 27) Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 """
def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

def main():
    numero = int(input("Digite um número inteiro para calcular o fatorial: "))
    
    if numero < 0:
        print("O fatorial não é definido para números negativos.")
    else:
        fatorial = calcular_fatorial(numero)
        print(f"{numero}! = {fatorial}")

if __name__ == "__main__":
    main()
