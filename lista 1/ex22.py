""" 22) Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for
digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles.
Desconsiderando o valor 1000 da parada.
 """

def main():
    numeros = []
    numero = int(input("Digite um número inteiro (ou 1000 para sair): "))
    
    while numero != 1000:
        numeros.append(numero)
        numero = int(input("Digite um número inteiro (ou 1000 para sair): "))
    
    total_numeros = len(numeros)
    soma = sum(numeros)
    
    print(f"Foram digitados {total_numeros} números.")
    print(f"A soma dos números digitados é: {soma}")

if __name__ == "__main__":
    main()

