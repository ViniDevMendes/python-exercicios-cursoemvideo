# Leia um número inteiro.

# Permita que o usuário escolha entre:
# 1 - Binário
# 2 - Octal
# 3 - Hexadecimal
# Mostre o resultado da conversão.

numero = int(input("Digite um número inteiro: "))

print("Escolha a conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

opcao = int(input("Digite a opção: "))

if opcao == 1:
    print(bin(numero)[2:])
elif opcao == 2:
    print(oct(numero)[2:])
elif opcao == 3:
    print(hex(numero)[2:])
else:
    print("Opção inválida")