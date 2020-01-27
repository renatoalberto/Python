"""
Dunder Name e Dunder Main (Dunder - Duble Under)

Dunder Name -> __name__
Dunder Main -> __main__

Em Python são utilizados dunder para criar funções, atributos, propriedades e etc utilizando
Double Under para não gerar conflito com o nome desses elementos na programação

# Na linguagem C, temos um programa da seguinte forma:

int main(){
    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:

public static void main(String[], args){

}

# Em Python, se executarmos um código diretamente na linha de comando, internamente o
Python atribuirá à variável __name__ o valor __main__ indicando que este módulo é o módulo
de execução principal.

# Quando um módulo é importado, a variável __name__ passa a receber o nome do proprio módulo


"""
from funcoes_com_parametros import soma_impares

# if a seguir é necessário para saber se o módulo está sendo executado diretamente
if __name__ == '__main__':
    print(soma_impares(range(10)))
