# ---------------------------------------------------------------------------------------
import random

# https://www.alt-codes.net/suit-cards.php
NAIPES = '♠ ♡ ♣ ♢'.split()
CARTAS = '2 3 4 5 6 7 8 9 J Q K A'.split()

print(NAIPES)
print(CARTAS)

def criar_baralho(aleatorio = False):
    """Cria um baralho com 52 cartas"""
    baralho = [(n, c) for c in CARTAS for n in NAIPES]

    if aleatorio:
        random.shuffle(baralho)

    return baralho


def distribuir_cartas(baralho):
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


def jogar():
    """Inicia um jogo de cartas para 4 jogadores"""
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {jog: mao for jog, mao in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f'{c}{j}' for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()