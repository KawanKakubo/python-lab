# Funções Lambda em Python

As funções lambda em Python são pequenas funções anônimas definidas usando a palavra-chave `lambda`. Elas são úteis quando precisamos de uma função curta e descartável para uma tarefa específica, sem a necessidade de defini-la usando a palavra-chave `def`.

### Sintaxe de uma Função Lambda

A sintaxe de uma função lambda é:
```python
lambda argumentos: expressão
```
- `argumentos`: são os parâmetros que a função lambda recebe.
- `expressão`: é a operação que a função lambda realiza e cujo resultado é retornado.

### Características das Funções Lambda
- São funções anônimas, ou seja, não possuem um nome definido.
- Podem ter qualquer número de argumentos, mas apenas uma expressão.
- A expressão é avaliada e retornada.
- Geralmente usadas para operações simples e curtas.

### Exemplo Simples de Função Lambda

**Exemplo básico de função lambda:**
```python
dobro = lambda x: x * 2
print(dobro(5))  # Saída: 10
```
Neste exemplo, `lambda x: x * 2` define uma função que multiplica o argumento `x` por 2. A função é então atribuída à variável `dobro`.

### Usando Funções Lambda com `map()`

A função `map()` aplica uma função a todos os itens em uma lista (ou outro iterável) e retorna um novo iterável com os itens modificados.

**Exemplo com `map()`:**
```python
numeros = [1, 2, 3, 4]
dobros = list(map(lambda x: x * 2, numeros))
print(dobros)  # Saída: [2, 4, 6, 8]
```
Aqui, `lambda x: x * 2` é aplicada a cada item da lista `numeros`.

### Usando Funções Lambda com `filter()`

A função `filter()` filtra elementos de uma lista (ou outro iterável) que retornam `True` para uma função fornecida.

**Exemplo com `filter()`:**
```python
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4, 6]
```
Aqui, `lambda x: x % 2 == 0` é usada para filtrar os números pares da lista `numeros`.

### Usando Funções Lambda com `sorted()`

A função `sorted()` pode usar uma função lambda como a chave para determinar a ordem dos elementos.

**Exemplo com `sorted()`:**
```python
pessoas = [("João", 25), ("Ana", 22), ("Carlos", 30)]
ordenado_por_idade = sorted(pessoas, key=lambda pessoa: pessoa[1])
print(ordenado_por_idade)
# Saída: [('Ana', 22), ('João', 25), ('Carlos', 30)]
```
Aqui, `lambda pessoa: pessoa[1]` é usada para ordenar a lista de tuplas pelo segundo elemento (idade).

### Funções Lambda em Expressões de Alta Ordem

Funções lambda são frequentemente usadas com funções de alta ordem, como `map()`, `filter()`, e `reduce()` (da biblioteca `functools`).

**Exemplo com `reduce()`:**
```python
from functools import reduce
numeros = [1, 2, 3, 4]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)  # Saída: 10
```
Aqui, `lambda x, y: x + y` é usada para acumular a soma dos elementos da lista `numeros`.

As funções lambda são uma ferramenta poderosa para tornar seu código mais conciso e legível quando usadas corretamente em Python.
