## Interactive Help
O Python possui um sistema interativo de ajuda que permite que você obtenha informações sobre módulos, classes, funções e outros elementos. Existem algumas maneiras de acessar essa ajuda:

- **Função `help()`**: Chamando `help(objecto)`, você recebe informações detalhadas sobre o objeto, incluindo sua documentação (docstrings), métodos disponíveis e outros detalhes. Por exemplo, `help(print)` fornece informações sobre a função `print`.

- **Uso do `?` no Jupyter Notebook**: Se você estiver usando um Jupyter Notebook, pode colocar um ponto de interrogação `?` após o nome de uma função ou variável para obter informações sobre ela. Por exemplo, `print?`.

- **Função `dir()`**: Esta função lista todos os atributos e métodos disponíveis em um objeto. Por exemplo, `dir(str)` lista todos os métodos associados ao tipo de dado `str`.

## Docstrings
Docstrings (ou "strings de documentação") são uma parte importante da documentação de um código Python. Elas são usadas para documentar módulos, classes e funções. Uma docstring é uma string que é a primeira declaração no corpo de uma função ou classe, e é usada para fornecer informações sobre seu propósito, uso e comportamento.

```python
def soma(a, b):
    """
    Retorna a soma de dois números.
    
    Argumentos:
    a -- primeiro número
    b -- segundo número
    
    Retorna:
    A soma de a e b.
    """
    return a + b
```

Docstrings são acessíveis por meio da função `help()` e do atributo especial `.__doc__`.

## Argumentos Opcionais
Em Python, funções podem ter argumentos opcionais com valores padrão. Se um argumento não for passado, o valor padrão é usado. Isso permite funções mais flexíveis.

```python
def saudacao(nome, cumprimento="Olá"):
    return f"{cumprimento}, {nome}!"

# Usando valores padrão
print(saudacao("Maria"))  # Saída: Olá, Maria!

# Substituindo o valor padrão
print(saudacao("João", "Bom dia"))  # Saída: Bom dia, João!
```

Argumentos opcionais são úteis para fornecer flexibilidade sem exigir que o usuário insira valores para cada argumento.

## Escopo de Variáveis
O escopo determina a visibilidade e a vida útil de variáveis. Em Python, existem diferentes tipos de escopo:

- **Escopo Local**: Variáveis declaradas dentro de uma função. Elas só são acessíveis dentro daquela função.
- **Escopo Global**: Variáveis declaradas no nível do módulo, fora de funções. Elas são acessíveis por todo o módulo.
- **Escopo Enclosure**: Escopo envolvente, como em funções aninhadas.
- **Escopo Built-in**: Escopo de funções e variáveis embutidas no Python.

```python
x = 10  # variável global

def minha_funcao():
    x = 5  # variável local
    print("Local:", x)

minha_funcao()  # Saída: Local: 5
print("Global:", x)  # Saída: Global: 10
```

Para usar variáveis globais dentro de uma função, use a palavra-chave `global`. Para modificar variáveis em escopos envolventes, use `nonlocal`.

## Retorno de Resultados
A instrução `return` é usada para retornar um valor de uma função. Uma função pode retornar um único valor, múltiplos valores (como uma tupla), ou nada (`None`).

```python
def soma(a, b):
    return a + b  # Retorna um valor

def operacoes(a, b):
    return a + b, a - b, a * b, a / b  # Retorna uma tupla

resultado = soma(2, 3)
print("Soma:", resultado)  # Saída: Soma: 5

resultado_operacoes = operacoes(10, 2)
print("Operações:", resultado_operacoes)  # Saída: Operações: (12, 8, 20, 5.0)
```

A palavra-chave `return` pode ser usada para sair antecipadamente de uma função e retornar um resultado. Se nenhuma instrução `return` for encontrada, a função retorna implicitamente `None`.
