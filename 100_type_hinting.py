"""
Type Hinting - Dica de Tipo (Pep 484 - Python 3.5)

Solução formal de indicar estaticamente o tipo de um dado em uma linguagem de programação em que a
tipagem de dados é dinâmica. Python vai continuar sendo uma linguagem de tipagem dinâmica.

É possível utilizar Type Hinting em umas funções e outras não, o MyPy vai avaliar comente as
que foram implementado o Type Hinting

Utilizando Type Hinting demonstra em uma entrevista para uma empresa que seu conhecimento é mais avançado.

Pós:
    1ª Facilita encontrar erros antes de executar o código
       - A própria IDE te alerta sobre os erros
       - MyPy - Faz a checagem de tipos e de uso para correção, tornando o código mais robusto
    2ª Melhora a documentação do Código
    3ª Melhora o funcionamento das IDEs para autocomplete e sugestões

Contra:
    1ª Estranhamento inicial
    2ª Implementação completa somente na versão 3.7
    3ª Ligeira queda de performance

"""
# ---------------------------------------------------------------------------------------


def cumprimentar(nome: str) -> str:
    return f'Olá , {nome}'


print(cumprimentar('Renato'))


# ---------------------------------------------------------------------------------------
def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        print(f'{texto.title()}\n{"=" * len(texto)}')
    else:
        print(f' {texto.title()} '.center(50, '='))


cabecalho('geek university')
cabecalho('geek university', alinhamento=False)

# Sintaxe correta -----------------------------------------------------------------------
# Correto
texto: str = 'Geek'

# Incorreto
texto:str = 'Geek'
texto : str = 'Geek'
