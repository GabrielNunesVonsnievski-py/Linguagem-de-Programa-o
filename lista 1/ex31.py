""" 31) Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador
perder. Mostre ao final, o total de vitórias consecutivas que o jogador conquistou no jogo. """

import random

def main():
    print("Jogo de Par ou Ímpar")
    
    vitorias_consecutivas = 0
    while True:
        jogador_escolha = input("Escolha par (p) ou ímpar (i): ")
        jogador_numero = int(input("Digite um número: "))
        
        computador_numero = random.randint(1, 10)
        total = jogador_numero + computador_numero
        
        resultado = "par" if total % 2 == 0 else "ímpar"
        
        print(f"Você escolheu {jogador_escolha}.")
        print(f"Você jogou {jogador_numero} e o computador jogou {computador_numero}.")
        print(f"Total: {total} é {resultado}.")
        
        if (jogador_escolha == "p" and total % 2 == 0) or (jogador_escolha == "i" and total % 2 != 0):
            vitorias_consecutivas += 1
            print("Você venceu!")
        else:
            print("Você perdeu.")
            break
        
    print(f"Total de vitórias consecutivas: {vitorias_consecutivas}")

if __name__ == "__main__":
    main()
