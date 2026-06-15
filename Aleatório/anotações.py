# -~-~-~-~-~-~-~-~- Tipos primitivos ~-~-~-~-~-~-~-~-~-

#   int()  --> Para números inteiros ------------ 17, 21, 35, 42

#   float() -> Números de ponto flutuante ---2.3, 1.6, 14.9, -67.1

#   bool() --> Armazena True ou False --------True, False

#   str() ----> Conjunto de caracteres -------- 'narigudo', 'Pedro', 'feioso'

#   type() ---> Indica o tipo primitivo da var -  x = 'Sapo Tunado'   print(type(x)) logo seu tipo primitivo é string

# -~-~-~-~-~-~-~- Operadores Aritméticos ~-~-~-~-~-~-~-

#   + -> Adição              ** -> Potencia
#   - -> Subtração           // -> Divisão inteira
#   * -> Multiplicação        % -> Resto da divisão
#   / > Divisão -


#            Ordem de Precedência

#   1° -> ()
#   2° -> **
#   3° -> *  /  //  %
#   4° -> +  -


# ~-~-~-~-~-~-~--~-~-~ Módulos -~-~-~-~-~-~-~-~-~-~-~

#   Import > Importa uma biblioteca - import math

#   from math import cos -> Importa somente a funçao cos da biblioteca math

#   math -> Biblioteca de operadores aritméticos {

#      sqrt()  ---> Raiz Quadrada de um numero ------- raiz = math.sqrt(numero)
#      floor() ---> Arredonda o numero para baixo ---- 5,23 fica 5,00
#      ceil() -----> Retorna um valor inteiro ---------------- 5,23 fica 5
#      hypot() ---> Retorna a hipotenusa dos catetos - math.hypot(co, ca)
#      pow() ----> Potencia de um numero ---------------- pow(2, 3) = 2³ = 8
#      radians()-> Converte em graus radianos ---------- print(math.radians(180))
#      cos() -----> Retorne o cosseno em radianos --- print(math.cos(math.radians(x)))
#      sin() ------> Retorne o seno em radianos --------- print(math.sin(math.radians(x)))
#      tan() -----> Retorne a tangente em radianos---- print(math.tan(math.radians(x)))
#   }

#   random -> Gerar numeros pseudoaleatorios {

#       randint() > Retorna um numero inteiro no range --------------- random.randint(1, 10)
#       choice() --> Retorna um elemento aleatório da sequência - random.choice(x)
#       shuffle() > Embaralha a sequência x no lugar ------------------- random.shuffle(y)
#   }


# -~-~-~-~-~-~-~-~- Manipulando Textos ~-~-~-~-~-~-~-~-

#   frase = 'ESTOU APRENDENDO A PROGRAMAR EM PYHTON'

#   frase[9] ------> Pega os caracteres das posições indicadas ------------------- letra E
#   frase[9:13] -> Pega os caracteres das posições indicadas ------------------- ENDE
#   frase[9:18:2]--> Pega os caracteres das posições indicadas pulando 2 - EDNOA
#   len() -------------> Mostra quantas letras tem a frase COM ESPAÇO -------------------------------- len(frase) = 38 letras
#   count() ---------> Conta quantas vezes aparece a letra escolhida ----------- frase.count('s')
#   find() ------------> Procura os caracteres escolhido ---------------------------------- frase.find('aprendendo')
#   replace() ------> Troca uma palavra por outra na frase --------------------------- frase.replace('python','JavaScript')
#   upper() ---------> Colocar todas as outras letras em maiúsculo -------------- frase.upper()
#   lower() ---------> Colocar todas as outras letras em minusculo -------------- frase.lower()
#   capilalize() ---> Coloca todas a frase em minusculo menos a 1 letra --- frase.capitalize()
#   title() ------------> Todas as palavras começa com letra maiúscula --------- frase.title()
#   strip() -----------> Tira o espaço do começo e no fim da frase ----------------- frase.strip()  frase.lstrip()  frase.rstrip()
#   split() -----------> Vai ocorrer uma divisão entre os espaços da frase ----- frase.split()
#   .join() -----------> Juntar uma coisa com a outra -------------------------------------- '-'.join.frase Estou-aprendendo-a-programar-em-python

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# -~-~-~-~-~-~-~-~- Cores no texto ~-~-~-~-~-~-~-~-

# Estilo                                              Texto               Background (Mesmas cores do Texto)      
 
# 0 = sem formatação                              30 = Branco                 40 = Fundo branco
# 1 = Negrito                                     31 = Vermelho               41 = Fundo vermelho
# 4 = Sublinhado                                  32 = Verde                  42 = Fundo verde
# 7 = Inverter a configurações                    33 = Amarelo                43 = Fundo amarelo
# fundo vai pra letra e letra vai pra fundo       34 = Azul                   44 = Fundo azul                  \033[0;33;44m
#                                                 35 = Rosa                   45 = Fundo rosa
#                                                 36 = Ciano                  46 = Fundo ciano
#                                                 37 = Cinza (Padrão)         47 = Fundo cinza


# Teste (Fundo vermelho letra branca) = \033[0;30;41m
# Teste (Fundo azul, sublinhado, letra amarela) = \033[4;33;44m
# Teste (Fundo amarelo com letra roxa) = \033[';35;43m
# Teste (Fundo verde com letra branca) = \033[30;42m - Obs: Nessa não tem padrão de estilo, sendo colocado o padrão (0)
# Teste (Fundo preto letra cinza) = \033[m - Obs: Petro e letra cinza = cor padrão do terminal
# Teste (Fundo branco com letra preta) = \033[7;30m - Obs: 7 é inversão e 30 é letra branca