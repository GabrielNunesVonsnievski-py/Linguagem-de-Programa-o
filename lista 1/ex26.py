""" 26) Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres). """

def main():
    while True:
        nome = input("Digite o nome (maior que 3 caracteres): ")
        if len(nome) > 3:
            break
        else:
            print("Nome inválido. O nome deve ter mais que 3 caracteres.")

    while True:
        idade = int(input("Digite a idade (entre 0 e 150): "))
        if 0 <= idade <= 150:
            break
        else:
            print("Idade inválida. A idade deve estar entre 0 e 150.")

    while True:
        salario = float(input("Digite o salário (maior que zero): "))
        if salario > 0:
            break
        else:
            print("Salário inválido. O salário deve ser maior que zero.")

    while True:
        sexo = input("Digite o sexo ('f' para feminino ou 'm' para masculino): ")
        if sexo.lower() == 'f' or sexo.lower() == 'm':
            break
        else:
            print("Sexo inválido. Digite 'f' para feminino ou 'm' para masculino.")

    while True:
        estado_civil = input("Digite o estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo ou 'd' para divorciado): ")
        if estado_civil.lower() in ['s', 'c', 'v', 'd']:
            break
        else:
            print("Estado civil inválido. Digite 's', 'c', 'v' ou 'd'.")

    print("Cadastro realizado com sucesso!")

if __name__ == "__main__":
    main()
