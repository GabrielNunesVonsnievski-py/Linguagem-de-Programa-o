"17) Fac¸a um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes formulas (onde h corresponde à altura): "

nota1 = float(input("Digite a nota de sua prova peso 10:"))
nota2 = float(input("Digite a nota de sua prova peso 5:"))
nota3 = float(input("Digite a sua outra nota peso 5:"))
if ( nota2 > 5 or nota2 < 0):
    print(f'ERRO')
elif ( nota3 > 5 or nota3 < 0):
    print(f'ERRO')
else:
    nota4 = nota2 + nota3 
final = (nota1 + nota4)/2
print(f'A sua média é de:{final}')
if (final >= 6):
    print(f'Você passou com a média de: {final}')
else:
    print(f'Você reprovou coma média de: {final}')
