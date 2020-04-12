"""
POO - Métodos Mágicos

Métodos mágicos são todos os métodos que utilizam dunder "duplo underline" definidos em object

# dunder init -> método construtor de uma classe
# dunder str  -> representação do objeto, tem prioridade sobre o repr
# dunder repr -> representação do objeto, caso str não seja declarado
# dunder del  -> permite realizar ações antes da deleção física
# dunder add  -> ajusta comportamento da adição (+)
# dunder mul  -> ajusta comportamento da multiplicação (*)

"""


class Livro:
    def __init__(self, titulo, autor, pagina):
        self.titulo = titulo
        self.autor = autor
        self.pagina = pagina

    def __str__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __len__(self):
        return self.pagina

    def __del__(self):
        print(f'{self.titulo} foi deletado')

    def __add__(self, outro_livro):
        return f'{self} & {outro_livro}'

    def __mul__(self, quantidade):
        return [f'{contador+1}ª {self}' for contador in range(quantidade)]


livro1 = Livro('Python Rocks', 'Geek', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek university', 350)

# __str__   -> representação do objeto, tem prioridade sobre o repr
# __repr__  -> representação do objeto, caso str não seja declarado
#   - posição de memória na classe object
#   - título do livro na classe Livro (Override)
print(f'__str__ - {livro1}')
print(f'__str__ - {livro2}\n')

# __len__  -> representa o tamanho da classe, retorno tipo inteiro
#   - método abstrata na classe object
#   - quantidade de páginas na classe Livro
print(f'__len__ - {len(livro1)}')
print(f'__len__ - {len(livro2)}\n')

# __del__ -> permite realizar ações antes da deleção física
#   - imprime: Inteligência Artificial com Python foi deletado
del livro1
# print(livro1)  # Aqui já não é possível imprimir livro1

livro1 = Livro('Python Rocks', 'Geek', 400)

# __add__ -> ajusta comportamento da adição
#   - retorna as representações com __str__ separados por &
print(livro1 + livro2)

# __mul__ -> ajusta comportamento da multiplicação
#   - retorna lista repetindo a representação com __str__ acompanhado de um contador
print(livro1 * 3)
