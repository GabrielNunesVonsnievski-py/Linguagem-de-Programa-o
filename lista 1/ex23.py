""" 23) Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os
valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
não continuar a escrever valores. """

def main():
    numeros = []
    continuar = True

    while continuar:
        numero = int(input("Digite um número inteiro: "))
        numeros.append(numero)
        
        resposta = input("Deseja continuar? (s/n): ")
        if resposta.lower() != 's':
            continuar = False
    
    if numeros:
        media = sum(numeros) / len(numeros)
        maior_valor = max(numeros)
        menor_valor = min(numeros)
        
        print(f"Média dos valores: {media:.2f}")
        print(f"Maior valor: {maior_valor}")
        print(f"Menor valor: {menor_valor}")
    else:
        print("Nenhum valor foi inserido.")

if __name__ == "__main__":
    main()
