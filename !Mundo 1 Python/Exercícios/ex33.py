# Faça um programa que leia três números e mostre qual é o maior e qual é o menor
#           JEITO DO VÍDEO

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando qual é menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando qual é maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))

#     OUTRAs FORMAs DE FAZER (NÃO FOI EU QUE FIZ)
 
# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
# n3 = int(input('Digite um último número: '))
# l = [n1, n2, n3]
# l.sort()
# print(f'O maior número é {l[2]} e o menor é {l[0]}')

# # --------------------------------------------------------------

# n1 = int(input('digite primeiro numero: ')) 
# n2 = int(input('digite segundo numero: '))
# n3 = int(input('digite terceiro numero: '))
# print('o maior numero é', max(n1, n2, n3))
# print('o menor numero é', min(n1, n2, n3))