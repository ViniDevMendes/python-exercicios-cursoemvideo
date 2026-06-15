# Leia o comprimento de três segmentos.
#
# Verifique se eles podem formar um triângulo.
#
# Caso formem:
# - Equilátero (3 lados iguais)
# - Isósceles (2 lados iguais)
# - Escaleno (3 lados diferentes)

a = float(input("Digite o primeiro segmento: "))
b = float(input("Digite o segundo segmento: "))
c = float(input("Digite o terceiro segmento: "))

# Verificação se forma triângulo
if a + b > c and a + c > b and b + c > a:

    if a == b and b == c:
        print("Triângulo EQUILÁTERO")
    elif a == b or a == c or b == c:
        print("Triângulo ISÓSCELES")
    else:
        print("Triângulo ESCALENO")
else:
    print("Não é possível formar um triângulo")