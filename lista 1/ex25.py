""" 25) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
usuário, mostrando uma mensagem de erro e voltando a pedir as informações. """

def main():
    while True:
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        
        if usuario != senha:
            print("Cadastro realizado com sucesso!")
            break
        else:
            print("Erro: A senha não pode ser igual ao nome de usuário. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
