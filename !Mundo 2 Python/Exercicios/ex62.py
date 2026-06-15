# Melhore o exercício anterior, perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

termo = primeiro_termo
cont = 10

while cont != 0:
    i = 0

    while i < cont:
        print(termo, end=" → ")
        termo += razao
        i += 1

    print()

    cont = int(input("Quer mostrar mais quantos termos? (0 para parar): "))

print("Progressão finalizada.")