"""
Por que testar o nosso código?
   - reduzir bugs (problemas) no código existente;
   - testes garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos;
   - testes garantem que bugs que foram corrigidos anteriormente continuem corrigidos;
   - testes garantem que a refatoração do nosso código que costumamos fazer não tragam novos bugs;

Pode acontecer:
   - testes tornam a desenvolvimento mais lento;
   - os testes podem ser maiores que o proprio código desenvolvido;

TDD - Teste Driver Developer (Desenvolvimento Guiado por Testes)
   - O teste é escrito primeiro;                                                      (Red)
   - Após o teste criado, desenvolvemos o código mínimo para satisfazer o teste;      (Green)
   - Refatora para a correta funcionalidade;                                          (Refactor)
   - O ciclo se repete até a entrega do produto final;

"""


class Gato:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando.')


# Testes manuais ----------------------------------------------------------------------------------
felix = Gato('Felix')
print(f'O nome do gato é {felix.nome}')
felix.miar()

