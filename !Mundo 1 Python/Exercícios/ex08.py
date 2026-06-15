# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidadede tinta necessária para pintá-la. 
# sabendo que cada litro de tinta pinta uma área de 2m²
#           JEITO DO VIDEO

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você irá precisar de {}L de tinta'.format(tinta))

#        JEITO QUE EU FIZ
# altura = float(input('Digite qual a altura da sua parede: '))
# largura = float(input('Digite a largura da sua parede: '))
# resultado = altura * largura
# print('A área da sua parede é de {}m²'.format(resultado))
# tinta = resultado / 2
# print('Para pintar essa parede, você irá precisar de {:.2f} litros de tinta'.format(tinta))