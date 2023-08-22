""" 28) Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para
cada eleitor votar e ao final mostrar o número de votos de cada candidato. """

def main():
    total_eleitores = int(input("Digite o número total de eleitores: "))
    
    candidato1_votos = 0
    candidato2_votos = 0
    candidato3_votos = 0
    
    for _ in range(total_eleitores):
        voto = int(input("Digite o número do candidato (1, 2 ou 3) em que deseja votar: "))
        
        if voto == 1:
            candidato1_votos += 1
        elif voto == 2:
            candidato2_votos += 1
        elif voto == 3:
            candidato3_votos += 1
        else:
            print("Voto inválido. Os candidatos são numerados de 1 a 3.")
    
    print("Resultado da eleição:")
    print(f"Bolsonaro: {candidato1_votos} votos")
    print(f"Lula: {candidato2_votos} votos")
    print(f"Djarana: {candidato3_votos} votos")

if __name__ == "__main__":
    main()
