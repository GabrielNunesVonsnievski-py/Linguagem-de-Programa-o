""" 32) Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram
obtidos os seguintes dados:
a. Código da cidade; (digitado pelo usuário)
b. Número de veículos de passeio (em 1999); (digitado pelo usuário)
c. Número de acidentes de trânsito com vítimas (em 1999). (digitado pelo usuário)
Deseja-se saber:
b. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
c. Qual a média de veículos nas cinco cidades juntas;
d. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio. """


def main():
    maior_indice_acidentes = -1
    menor_indice_acidentes = float('inf')
    cidade_maior_indice = ""
    cidade_menor_indice = ""
    total_veiculos = 0
    total_acidentes = 0
    cidades_menos_2000_veiculos = 0
    total_acidentes_menos_2000_veiculos = 0
    
    for _ in range(5):
        codigo_cidade = input("Digite o código da cidade: ")
        veiculos_passeio = int(input("Digite o número de veículos de passeio (em 1999): "))
        acidentes_vitimas = int(input("Digite o número de acidentes de trânsito com vítimas (em 1999): "))
        
        indice_acidentes = acidentes_vitimas / veiculos_passeio
        
        if indice_acidentes > maior_indice_acidentes:
            maior_indice_acidentes = indice_acidentes
            cidade_maior_indice = codigo_cidade
        
        if indice_acidentes < menor_indice_acidentes:
            menor_indice_acidentes = indice_acidentes
            cidade_menor_indice = codigo_cidade
        
        total_veiculos += veiculos_passeio
        total_acidentes += acidentes_vitimas
        
        if veiculos_passeio < 2000:
            cidades_menos_2000_veiculos += 1
            total_acidentes_menos_2000_veiculos += acidentes_vitimas
    
    media_veiculos = total_veiculos / 5
    media_acidentes_menos_2000_veiculos = total_acidentes_menos_2000_veiculos / cidades_menos_2000_veiculos
    
    print(f"Maior índice de acidentes: {maior_indice_acidentes:.2f} - Cidade: {cidade_maior_indice}")
    print(f"Menor índice de acidentes: {menor_indice_acidentes:.2f} - Cidade: {cidade_menor_indice}")
    print(f"Média de veículos nas cinco cidades: {media_veiculos:.2f}")
    print(f"Média de acidentes nas cidades com menos de 2000 veículos: {media_acidentes_menos_2000_veiculos:.2f}")

if __name__ == "__main__":
    main()
