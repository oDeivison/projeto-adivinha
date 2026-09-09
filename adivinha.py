import random

a = random.randint(1, 100)
print('Jogo de adivinhação')
print("Tente adivinhar o numero que estou pensando entre 0 a 100!")

c = n = 0
while n != a:
    n = int(input('Informe um número: '))

    if c == 7:
        print(f'Você errou e acabou as tentivas, o numero era {a}')
        break

    if n > a:
        print('Você errou! o numero secreto é menor')
        c += 1

    elif n < a:
        print('Você errou! o numero secreto é maior')
        c += 1

if c != 7:
    print(f'Você acertou com {c + 1} tentativas')

#teste 