# Lista de Exercícios — Matrizes e Listas Bidimensionais em Python

**Tema:** Matrizes / listas bidimensionais — arrays em nível introdutório  
**Conteúdos mobilizados:** lista de listas, acesso por índices `matriz[i][j]`, tabelas simples, boletins, grades, pequenas simulações e uso de matrizes em projetos.  
**Público-alvo:** estudantes iniciantes em programação.  
**Linguagem sugerida:** Python.  

---

## Objetivos da lista

Ao resolver esta lista, o estudante deverá ser capaz de:

1. Criar matrizes simples usando listas de listas.
2. Acessar e alterar elementos com índices duplos.
3. Percorrer matrizes com laços aninhados.
4. Calcular totais, médias, maiores e menores valores em tabelas.
5. Representar boletins, grades de assentos, presença e pequenas simulações.
6. Identificar erros comuns em matrizes, como índice fora dos limites e linhas irregulares.

---

## Orientações gerais

- Resolva os exercícios em arquivos `.py` separados ou em um notebook, conforme orientação do professor.
- Sempre teste o código após cada pequena alteração.
- Use nomes de variáveis significativos, como `linha`, `coluna`, `notas`, `boletim`, `sala` e `presencas`.
- Quando usar `i` e `j`, lembre-se: em geral, `i` representa a linha e `j` representa a coluna.
- Ao final de cada exercício prático, escreva uma frase curta explicando o que as linhas e colunas representam.

---

# Parte 1 — Fixação conceitual

## Exercício 1 — Identificando linhas e colunas

Considere a matriz abaixo:

```python
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```

Responda:

1. Quantas linhas a matriz possui?
2. Quantas colunas existem em cada linha?
3. Qual valor está em `matriz[0][2]`?
4. Qual valor está em `matriz[2][1]`?
5. Explique, com suas palavras, por que `matriz[1][1]` retorna `50`.

---

## Exercício 2 — Verdadeiro ou falso

Classifique as afirmações como **V** ou **F**. Depois, corrija as falsas.

1. Em Python, o primeiro índice de uma lista é `1`.
2. Em `matriz[i][j]`, normalmente `i` indica a linha e `j` indica a coluna.
3. Uma lista de listas sempre possui o mesmo número de elementos em todas as linhas.
4. Uma matriz pode representar um boletim escolar.
5. Para percorrer uma matriz inteira, geralmente usamos laços aninhados.

---

## Exercício 3 — Complete as lacunas

Complete as frases com os termos adequados: **linha**, **coluna**, **lista externa**, **lista interna**, **elemento**.

1. Em uma matriz, cada sublista pode ser interpretada como uma __________.
2. A estrutura que agrupa todas as sublistas é chamada de __________.
3. O valor armazenado em uma posição específica é chamado de __________.
4. Em `matriz[2][0]`, o índice `2` seleciona a __________.
5. Em `matriz[2][0]`, o índice `0` seleciona a __________ dentro da linha.

---

# Parte 2 — Acesso e alteração de elementos

## Exercício 4 — Acesso direto

Considere:

```python
notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]
```

Escreva comandos `print()` para exibir:

1. A primeira nota do primeiro estudante.
2. A terceira nota do segundo estudante.
3. A segunda nota do terceiro estudante.
4. A terceira nota do quarto estudante.
5. A linha completa de notas do terceiro estudante.

---

## Exercício 5 — Alterando valores

Usando a matriz do exercício anterior, escreva comandos para:

1. Alterar a primeira nota do segundo estudante para `6.5`.
2. Alterar a terceira nota do quarto estudante para `7.0`.
3. Imprimir a matriz completa após as alterações.
4. Explicar quais posições foram alteradas usando a notação `notas[i][j]`.

---

## Exercício 6 — Erro de índice

Analise o código:

```python
dados = [
    [1, 2],
    [3, 4]
]

print(dados[2][0])
```

Responda:

1. Esse código executa corretamente? Por quê?
2. Quais são os índices válidos para as linhas dessa matriz?
3. Corrija o código para exibir o valor `3`.

---

# Parte 3 — Percorrendo matrizes

## Exercício 7 — Percurso por valor

Dada a matriz:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Escreva um programa que percorra a matriz e imprima todos os valores, um por linha, usando o formato:

```text
Valor: 1
Valor: 2
...
```

Use percurso por valor, isto é, sem usar `range(len(...))`.

---

## Exercício 8 — Percurso por índice

Usando a mesma matriz do exercício anterior, escreva um programa que imprima a posição e o valor de cada elemento no formato:

```text
Linha 0 Coluna 0 Valor 1
Linha 0 Coluna 1 Valor 2
...
```

Use `range(len(...))`.

---

## Exercício 9 — Soma geral

Crie um programa que calcule a soma de todos os valores da matriz abaixo:

```python
valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]
```

Ao final, exiba:

```text
Soma total: 45
```

---

## Exercício 10 — Contagem de pares

Usando a matriz do exercício anterior, conte quantos números pares existem.

Saída esperada:

```text
Quantidade de pares: 4
```

---

## Exercício 11 — Maior e menor valor

Crie um programa que encontre o maior e o menor valor da matriz abaixo:

```python
numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]
```

Exiba:

```text
Maior valor: 21
Menor valor: 3
```

---

## Exercício 12 — Localizando posição do maior valor

A partir da matriz do exercício anterior, além de encontrar o maior valor, mostre sua posição:

```text
Maior valor: 21
Linha: 1
Coluna: 1
```

---

# Parte 4 — Boletins e tabelas simples

## Exercício 13 — Média por estudante

Considere o boletim:

```python
nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]
```

Crie um programa que calcule e exiba a média de cada estudante.

Saída sugerida:

```text
Ana - Média: 8.17
Bruno - Média: 5.50
Carla - Média: 9.17
Diego - Média: 6.50
```

---

## Exercício 14 — Situação acadêmica

Amplie o exercício anterior. Agora, o programa deve exibir também a situação do estudante:

- média maior ou igual a `7.0`: **Aprovado**;
- média menor que `7.0`: **Recuperação**.

Saída sugerida:

```text
Ana - Média: 8.17 - Aprovado
Bruno - Média: 5.50 - Recuperação
Carla - Média: 9.17 - Aprovado
Diego - Média: 6.50 - Recuperação
```

---

## Exercício 15 — Maior média da turma

Usando os mesmos dados, identifique o estudante com a maior média.

Saída esperada:

```text
Maior média: Carla - 9.17
```

---

## Exercício 16 — Média por avaliação

Ainda usando a matriz de notas, calcule a média da turma em cada avaliação.

Saída sugerida:

```text
Avaliação 0 - Média: 7.13
Avaliação 1 - Média: 7.25
Avaliação 2 - Média: 7.63
```

---

## Exercício 17 — Avaliação com menor média

A partir do exercício anterior, identifique qual avaliação teve a menor média.

Saída esperada:

```text
Avaliação com menor média: 0
Média: 7.13
```

---

## Exercício 18 — Relatório de recuperação

Crie um programa que mostre apenas os estudantes em recuperação.

Saída esperada:

```text
Estudantes em recuperação:
Bruno - Média: 5.50
Diego - Média: 6.50
```

---

# Parte 5 — Grades, presença e pequenas simulações

## Exercício 19 — Grade de assentos

Considere a matriz:

```python
sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]
```

Em que:

- `"L"` representa assento livre;
- `"O"` representa assento ocupado.

Crie um programa que conte quantos assentos estão livres e quantos estão ocupados.

---

## Exercício 20 — Reservando assento

Usando a matriz `sala`, tente reservar o assento da linha `2`, coluna `1`.

Regras:

1. Se o assento estiver livre, altere para `"O"` e exiba `Reserva realizada`.
2. Se estiver ocupado, exiba `Assento indisponível`.
3. Ao final, imprima a matriz atualizada.

---

## Exercício 21 — Controle de presença

Crie uma matriz 4x5 para representar a presença de 4 estudantes em 5 aulas.

Use:

- `"P"` para presente;
- `"F"` para falta.

Depois, escreva um programa que conte o total de presenças e o total de faltas.

Exemplo de matriz:

```python
presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]
```

---

## Exercício 22 — Faltas por estudante

Usando a matriz de presença do exercício anterior, mostre quantas faltas cada estudante teve.

Saída sugerida:

```text
Estudante 0 - Faltas: 1
Estudante 1 - Faltas: 2
Estudante 2 - Faltas: 1
Estudante 3 - Faltas: 2
```

---

## Exercício 23 — Aula com mais faltas

Usando a mesma matriz de presença, descubra qual aula teve mais faltas.

Dica: agora será necessário percorrer por coluna.

---

## Exercício 24 — Jogo da velha: exibição do tabuleiro

Crie uma matriz 3x3 para representar um tabuleiro de jogo da velha:

```python
tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]
```

Escreva um programa que exiba o tabuleiro em formato visual:

```text
X | O |  
---------
  | X | O
---------
O |   | X
```

---

## Exercício 25 — Jogo da velha: jogada simples

Usando o tabuleiro do exercício anterior, faça uma jogada na linha `1`, coluna `0` com o símbolo `"X"`.

Regras:

1. Se a posição estiver vazia (`" "`), realize a jogada.
2. Se a posição estiver ocupada, informe que a jogada é inválida.
3. Exiba o tabuleiro atualizado.

---

# Parte 6 — Depuração e análise de código

## Exercício 26 — Corrigindo matriz irregular

Analise o código:

```python
dados = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

for i in range(len(dados)):
    for j in range(3):
        print(dados[i][j])
```

Responda:

1. Qual erro pode ocorrer?
2. Por que esse erro acontece?
3. Reescreva o código de forma segura usando `len(dados[i])`.

---

## Exercício 27 — Inicialização incorreta

Analise:

```python
matriz = [[0] * 3] * 3
matriz[0][0] = 1
print(matriz)
```

Responda:

1. Qual resultado provavelmente será exibido?
2. Por que esse comportamento pode confundir iniciantes?
3. Reescreva a criação da matriz usando compreensão de listas.

---

## Exercício 28 — Acumulador no lugar errado

O código abaixo deveria calcular a média de cada linha, mas possui erro lógico:

```python
notas = [
    [8, 7, 9],
    [5, 6, 5],
    [9, 10, 8]
]

soma = 0
for i in range(len(notas)):
    for j in range(len(notas[i])):
        soma += notas[i][j]
    media = soma / len(notas[i])
    print(media)
```

Responda:

1. Qual é o problema com a variável `soma`?
2. Corrija o código.
3. Explique por que a correção funciona.

---

# Parte 7 — Desafios integradores

## Exercício 29 — Sistema simples de boletim

Crie um programa completo que:

1. Armazene nomes de 5 estudantes.
2. Armazene 4 notas para cada estudante usando uma matriz.
3. Calcule a média de cada estudante.
4. Mostre a situação: aprovado, recuperação ou reprovado.
5. Use as regras:
   - média maior ou igual a `7.0`: aprovado;
   - média maior ou igual a `5.0` e menor que `7.0`: recuperação;
   - média menor que `5.0`: reprovado.
6. Mostre a maior média da turma.
7. Mostre a menor média da turma.

---

## Exercício 30 — Mapa de ocupação de laboratório

Crie um programa para representar um laboratório com 4 fileiras e 5 computadores por fileira.

Use:

- `"L"` para computador livre;
- `"O"` para computador ocupado;
- `"M"` para computador em manutenção.

O programa deve:

1. Exibir o mapa completo.
2. Contar computadores livres, ocupados e em manutenção.
3. Permitir ocupar uma posição livre.
4. Impedir ocupar uma posição em manutenção.
5. Informar se a posição digitada está fora dos limites da matriz.

---

## Exercício 31 — Matriz de vendas

Uma loja registrou as vendas de 3 produtos durante 4 semanas:

```python
vendas = [
    [20, 25, 18, 30],
    [15, 22, 20, 19],
    [30, 28, 35, 40]
]
```

Cada linha representa um produto e cada coluna representa uma semana.

Crie um programa que:

1. Calcule o total vendido por produto.
2. Calcule o total vendido por semana.
3. Identifique o produto com maior total vendido.
4. Identifique a semana com maior total vendido.

---

## Exercício 32 — Simulação de crescimento em grade

Considere uma grade 5x5 em que:

- `0` representa célula vazia;
- `1` representa célula ocupada.

Crie uma matriz inicial e faça uma simulação simples:

1. Conte quantas células estão ocupadas.
2. Altere manualmente três células vazias para ocupadas.
3. Conte novamente as células ocupadas.
4. Exiba a grade antes e depois.

---

# Parte 8 — Questões objetivas no padrão ENADE

## Questão 33

Considere o código:

```python
matriz = [
    [2, 4, 6],
    [8, 10, 12]
]

print(matriz[1][0])
```

O resultado impresso será:

A) `2`  
B) `4`  
C) `6`  
D) `8`  
E) `[8, 10, 12]`

---

## Questão 34

Uma matriz `notas` possui 5 linhas e 3 colunas. Considerando a indexação em Python, a última posição válida dessa matriz é:

A) `notas[5][3]`  
B) `notas[4][2]`  
C) `notas[3][4]`  
D) `notas[2][4]`  
E) `notas[1][1]`

---

## Questão 35

Considere a matriz:

```python
sala = [
    ["L", "O"],
    ["O", "L"]
]
```

Qual trecho conta corretamente os assentos livres?

A)

```python
livres = sala.count("L")
```

B)

```python
livres = 0
for linha in sala:
    for assento in linha:
        if assento == "L":
            livres += 1
```

C)

```python
livres = len(sala)
```

D)

```python
livres = 0
for assento in sala:
    if assento == "L":
        livres += 1
```

E)

```python
livres = sala["L"]
```

---

## Questão 36

Ao usar laços aninhados para percorrer uma matriz regular, é correto afirmar que:

A) O laço interno normalmente percorre as linhas, e o externo percorre as colunas.  
B) Não é possível usar `for` em matrizes.  
C) O laço externo pode percorrer as linhas, enquanto o laço interno percorre os elementos de cada linha.  
D) Matrizes só podem armazenar números inteiros.  
E) O acesso `matriz[i][j]` sempre retorna uma linha inteira.

---

## Questão 37

O código abaixo apresenta um problema:

```python
matriz = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

print(matriz[1][2])
```

A análise correta é:

A) O código imprime `5`.  
B) O código imprime `6`.  
C) O código apresenta erro, pois a linha de índice `1` não possui coluna de índice `2`.  
D) O código imprime `[4, 5]`.  
E) O código imprime `3`.

---

# Gabarito resumido

## Parte conceitual e objetiva

- Exercício 1: 3 linhas; 3 colunas; `30`; `80`; porque linha 1 é `[40, 50, 60]` e coluna 1 é `50`.
- Exercício 2: F, V, F, V, V.
- Exercício 3: linha; lista externa; elemento; linha; coluna.
- Exercício 6: não executa; índices válidos de linha são `0` e `1`; para exibir `3`, use `dados[1][0]`.
- Questão 33: D.
- Questão 34: B.
- Questão 35: B.
- Questão 36: C.
- Questão 37: C.

## Resultados esperados de exercícios selecionados

- Exercício 9: soma total `45`.
- Exercício 10: quantidade de pares `4`.
- Exercício 11: maior `21`, menor `3`.
- Exercício 12: maior `21`, linha `1`, coluna `1`.
- Exercício 13: Ana `8.17`, Bruno `5.50`, Carla `9.17`, Diego `6.50`.
- Exercício 15: maior média `Carla - 9.17`.
- Exercício 16: médias aproximadas `7.13`, `7.25`, `7.63`.
- Exercício 18: Bruno e Diego em recuperação.

---

# Sugestão de avaliação

| Critério | Descrição | Pontuação sugerida |
|---|---|---:|
| Criação correta de matrizes | Usa listas de listas de forma coerente | 2,0 |
| Acesso e alteração por índices | Usa `matriz[i][j]` corretamente | 2,0 |
| Percurso com laços aninhados | Percorre linhas e colunas sem erros | 2,0 |
| Resolução dos problemas aplicados | Calcula médias, contagens, buscas e relatórios | 3,0 |
| Clareza e organização do código | Usa bons nomes, comentários úteis e testes | 1,0 |

---

# Observação final ao estudante

Matrizes são úteis quando os dados têm uma organização natural em linhas e colunas. Antes de programar, sempre pergunte: **o que cada linha representa? O que cada coluna representa? A posição da célula tem significado para o problema?**
