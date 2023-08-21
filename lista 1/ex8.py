"8) Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m²."

largura = float(input(f"Digite a largura da sua parede em metros: "))
altura = float(input(f"Digite a altura da sua parede em metros: "))
area = altura * altura
tinta = area * altura

print(f"A área da sua parede é de:",area)
print(f"Você precisará de",tinta,"litros de tinta para pinta-la")
