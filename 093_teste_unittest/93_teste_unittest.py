"""
Introdução ao módulo Unittest - Testes Unitários

https://docs.python.org/3/library/unittest.html

O que são unittests?
  - Teste unitário é a forma de se testar unidades individuais de código fonte.

Unidades Individuais podem ser:
  - funções;
  - métodos;
  - classes;
  - módulos;
  - etc...

Para criar nosso teste, criamos classes que herdam de unittest.TestCase e a partir
de então ganhamos todos os 'assertions' presentes do módulo.

TesteCase -> casos de teste para a sua unidade.

Para rodar os teste, utilizamos do módulo unittest.main()

Conhecendo as assertions:
    - assertEqual(a, b)         => a == b
    - assertNotEqual(a, b)      => a != b
    - assertTrue(x)             => bool(x) is True
    - assertFalse(x)            => bool(x) is False
    - assertIs(a, b)            => a is b
    - assertIsNot(a, b)         => a is not b
    - assertIsNone(x)           => x is None
    - assertIsNotNone(x)        => x is not None
    - assertIn(a, b)            => a in b
    - assertNotIn(a, b)         => a not in b
    - assertIsInstance(a, b)    => isinstance(a, b)
    - assertNotIsInstance(a, b) => not isinstance(a, b)

Por convenção todos os teste em um test case, devem ter seu nome iniciados
com test_...

Para executar os teste com unittest                 => python nome_do_modulo.py
Para executar os teste com unittest no modo verbose => python nome_do_modulo.py -v

Podemos acrescentar e é recomendado docstring nos nosso testes

"""
import unittest
