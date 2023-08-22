""" 33) Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os
códigos utilizados são:
 1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
a. O total de votos para cada candidato;
b. O total de votos nulos;
c. O total de votos em branco;
d. A percentagem de votos nulos sobre o total de votos;
e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o
valor zero.
 """
def main():
    candidatos = {
        1: "José",
        2: "João",
        3: "Maria",
        4: "Ana"
    }
    
    votos = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,  # Votos nulos
        6: 0   # Votos em branco
    }
    
    total_votos = 0
    
    while True:
        print("\nOpções de voto:")
        for codigo, nome in candidatos.items():
            print(f"{codigo} - {nome}")
        print("5 - Voto Nulo")
        print("6 - Voto em Branco")
        
        voto = int(input("\nDigite o código do candidato (ou 0 para encerrar): "))
        
        if voto == 0:
            break
        
        if voto in votos:
            votos[voto] += 1
            total_votos += 1
        else:
            print("Voto inválido. Insira um código de candidato válido (1 a 4) ou código de voto nulo (5) ou voto em branco (6).")
    
    print("\nResultado da eleição:")
    for candidato_codigo, candidato_nome in candidatos.items():
        print(f"{candidato_nome}: {votos[candidato_codigo]} votos")
    
    total_votos_nulos = votos[5]
    total_votos_brancos = votos[6]
    
    percentagem_nulos = (total_votos_nulos / total_votos) * 100
    percentagem_brancos = (total_votos_brancos / total_votos) * 100
    
    print(f"\nTotal de votos nulos: {total_votos_nulos}")
    print(f"Total de votos em branco: {total_votos_brancos}")
    print(f"Percentagem de votos nulos: {percentagem_nulos:.2f}%")
    print(f"Percentagem de votos em branco: {percentagem_brancos:.2f}%")

if __name__ == "__main__":
    main()
