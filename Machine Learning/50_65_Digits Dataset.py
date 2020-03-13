"""
Digits Dataset - Reconhecimento de Imagem

Esses conjunto de dados consiste em imagens de dígitos de 0 a 9, escritos a mão. Vamos treinar nosso computador
para reconhecer esse tipo de imagem, logo após vamos apresentar uma imagem de um digito escrito a mão e o computador
irá dizer qual o digito está escrito.

O Digits Dataset é composto por:
    - 1797 observações, imagens de dígitos escrito a mão;
    - Cada observação possui 64 variáveis.
    - Cada variável representa uma cor na escala de cinza, que vai de (0 Branco) à (16 Preto).
    - A dimensão da imagem é de 8 x 8 pixels, um total de 64 pixels.

Digits Dataset faz parte do pacote sklearn :
from sklearn.datasets import load_digits
digits = load_digits()
"""