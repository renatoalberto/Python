# Implementando Type Hinting ------------------------------------------------------------
import random
from typing import List, Tuple, Dict

# https://www.alt-codes.net/suit-cards.php
NAIPES: List[str] = '♠ ♡ ♣ ♢'.split()
CARTAS: List[str] = '2 3 4 5 6 7 8 9 J Q K A'.split()

print(NAIPES)
print(CARTAS)

CARTA = Tuple[str, str]
BARALHO = List[CARTA]


def criar_baralho(aleatorio: bool = False) -> BARALHO:
    """Cria um baralho com 52 cartas"""
    baralho: BARALHO = [(c, n) for c in CARTAS for n in NAIPES]

    if aleatorio:
        random.shuffle(baralho)

    return baralho


def distribuir_cartas(baralho: BARALHO) -> Tuple[BARALHO, BARALHO, BARALHO, BARALHO]:
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4]


def jogar() -> None:
    """Inicia um jogo de cartas para 4 jogadores"""
    cartas: BARALHO = criar_baralho(aleatorio=True)
    jogadores: List[str] = 'P1 P2 P3 P4'.split()
    maos: Dict[str, BARALHO] = {jog: mao for jog, mao in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta: str = ' '.join(f'{c}{n}' for (c, n) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()