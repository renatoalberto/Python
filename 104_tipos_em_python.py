# coleções ------------------------------------------------------------------------------
nomes: list = ['Geek', 'University']
versoes: tuple = (3, 4, 7)
opcoes: dict = {'ar': True, 'banco de couro': True}
valores: set = {3, 4, 5, 6, 7}

print(nomes)
print(versoes)
print(opcoes)
print(valores)

# {'nomes': <class 'list'>,
# 'versoes': <class 'tuple'>,
# 'opcoes': <class 'dict'>,
# 'valores': <class 'set'>}
print(__annotations__)

# coleções contendo tipos específicos ---------------------------------------------------
from typing import List, Tuple, Dict, Set

nomes: List[str] = ['Geek', 'University']
versoes: Tuple[int, int, int] = (3, 4, 7)
opcoes: Dict[str, bool] = {'ar': True, 'banco de couro': True}
valores: Set[int] = {3, 4, 5, 6, 7}

print(nomes)
print(versoes)
print(opcoes)
print(valores)

# {'nomes': typing.List[str],
# 'versoes': typing.Tuple[int, int, int],
# 'opcoes': typing.Dict[str, bool],
# 'valores': typing.Set[int]}
print(__annotations__)
