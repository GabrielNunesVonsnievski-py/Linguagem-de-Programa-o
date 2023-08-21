nome = input(f"Digite seu nome: ")
nht = float(input(f"Digite o numero de horas trabalhadas: "))
vlht = float(input(f"Digite o valor de horas trabalhadas: "))

salariobruto = nht * vlht
salariofinal = salariobruto /0.02

print(f"Numero de horas trabalhadas: ",nht)
print(f"Valor de horas trabalhadas: ",vlht)
print(f"Salario bruto: ",salariobruto)
print(f"salario final é: ",salariofinal)