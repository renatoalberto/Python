"""
POO - Classes

Em POO, classes nada mais são do que modelo dos objetos do mundo real sendo representados computacionalmente

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
  - Atributos - que representam as características de um objeto. Ou seja, com esses atributos conseguimos representar
                computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente iriamos poder saber
                se a lâmpada é 110w ou 220w, se ela é amarela, branca ou outra cor, qual é a luminosidade dela e etc.
  - Métodos   - (funções), representam o comportamento do objeto. Ou seja, as ações que este objeto pode realizar no
                seu sistema. No caso lâmpada, por exemplo, iriamos querer ligar e desligar.

Em Python, para definirmos uma classe utilizamos a palavra reservada "class"

Obs: quando nomeamos "nossas classes" em Python, utilizamos por convenção o nome inicial em maiúsculo. Se o nome
     for composto, utiliza-se as iniciais de ambas as palavras em maiúsculo, todas juntas "Camel Case". Classes
     internas do Python são nomeadas em minúsculos para podermos diferencias quais classes são internas ou nossas.


Dicas Geek: em computação não utilizamos: acentuação, caracteres especial, espaços ou similares para nome
            de classes, atributos, métodos, arquivos, diretórios e etc.

Obs: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos estes
     objetos de que serão mapeados para classes de "entidade".
"""


class Carro:
    pass


class ContaCorrente:
    pass


civic = Carro()
print(type(civic))  # <class '__main__.Carro'>
