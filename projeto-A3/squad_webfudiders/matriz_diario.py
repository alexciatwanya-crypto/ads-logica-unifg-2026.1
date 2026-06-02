
# A MATRIZ PRINCIPAL do sistema
# Cada linha = [nome, nota1, nota2, nota3]
# Exemplo:
#   diario = [
#       ["Maria", 5.0, 6.0, 4.0],
#       ["Joao",  8.0, 9.0, 8.5]
#   ]

diario = []  # começa vazio; alunos são adicionados pela função abaixo


# ------------------------------------------------------------
# 1. ADICIONAR ALUNO NA MATRIZ
# ------------------------------------------------------------
def adicionar_aluno(nome):
    """
    Cria uma nova linha na matriz com o nome do aluno
    e três notas zeradas.
    Exemplo de linha criada: ["Maria", 0.0, 0.0, 0.0]
    """
    nova_linha = [nome, 0.0, 0.0, 0.0]
    diario.append(nova_linha)
    print(f"  Aluno '{nome}' adicionado ao diário.")


# ------------------------------------------------------------
# 2. LANÇAR NOTA (item 2.2)
# ------------------------------------------------------------
def lancar_nota(nome, numero_nota, valor):
    """
    Atualiza uma nota específica de um aluno na matriz.

    Parâmetros:
        nome        -> nome do aluno (string)
        numero_nota -> qual nota: 1, 2 ou 3
        valor       -> valor entre 0.0 e 10.0

    A matriz tem este formato por índice:
        [0] = nome
        [1] = nota 1
        [2] = nota 2
        [3] = nota 3
    Por isso: índice da nota = numero_nota (1, 2 ou 3)
    """
    # Valida o valor da nota
    if valor < 0.0 or valor > 10.0:
        print("  ERRO: nota deve ser entre 0.0 e 10.0")
        return False

    # Percorre a matriz procurando o aluno pelo nome
    for linha in diario:
        if linha[0] == nome:          # linha[0] é o nome
            linha[numero_nota] = valor # atualiza a nota na posição certa
            print(f"  Nota {numero_nota} de '{nome}' atualizada para {valor}")
            return True

    print(f"  ERRO: aluno '{nome}' não encontrado.")
    return False


# ------------------------------------------------------------
# 3. CALCULAR MÉDIA DE UM ALUNO (item 2.3)
# ------------------------------------------------------------
def calcular_media(linha):
    """
    Recebe UMA linha da matriz e calcula a média das 3 notas.

    Exemplo:
        linha = ["Maria", 5.0, 6.0, 4.0]
        média = (5.0 + 6.0 + 4.0) / 3  →  5.0
    """
    nota1 = linha[1]   # índice 1 = nota 1
    nota2 = linha[2]   # índice 2 = nota 2
    nota3 = linha[3]   # índice 3 = nota 3
    media = (nota1 + nota2 + nota3) / 3
    return round(media, 2)   # arredonda para 2 casas decimais


# ------------------------------------------------------------
# 4. DEFINIR STATUS (aprovado / reprovado / recuperação)
# ------------------------------------------------------------
def definir_status(media):
    """
    Retorna o status do aluno com base na média calculada.

    Regras (ajuste conforme o professor pedir):
        média >= 7.0  →  Aprovado
        média >= 5.0  →  Recuperação
        média <  5.0  →  Reprovado
    """
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"


# ------------------------------------------------------------
# 5. PROCESSAR TODO O DIÁRIO — FOR ANINHADO (desafio)
# ------------------------------------------------------------
def processar_diario():
    """
    Percorre a matriz inteira com for aninhado e calcula
    a média + status de TODOS os alunos de uma vez.

    Retorna uma lista de resultados:
        [nome, nota1, nota2, nota3, media, status]
    """
    resultados = []

    # FOR DE FORA: percorre cada linha (cada aluno)
    for linha in diario:
        nome  = linha[0]
        media = calcular_media(linha)
        status = definir_status(media)

        # FOR DE DENTRO: percorre só as notas (índices 1, 2, 3)
        notas = []
        for i in range(1, 4):      # i = 1, 2, 3
            notas.append(linha[i]) # coleta cada nota

        resultado = [nome, notas[0], notas[1], notas[2], media, status]
        resultados.append(resultado)

    return resultados


# ------------------------------------------------------------
# 6. EXIBIR RELATÓRIO FORMATADO NA TELA
# ------------------------------------------------------------
def exibir_relatorio():
    """
    Imprime uma tabela com todos os alunos, notas, médias e status.
    Esta função é chamada pelo menu do Aluno 1 (opção 4 - Relatórios).
    """
    if len(diario) == 0:
        print("  Nenhum aluno cadastrado ainda.")
        return

    resultados = processar_diario()

    print()
    print("=" * 62)
    print(f"  {'NOME':<15} {'N1':>5} {'N2':>5} {'N3':>5} {'MÉDIA':>7}  STATUS")
    print("=" * 62)

    for r in resultados:
        nome   = r[0]
        n1     = r[1]
        n2     = r[2]
        n3     = r[3]
        media  = r[4]
        status = r[5]
        print(f"  {nome:<15} {n1:>5.1f} {n2:>5.1f} {n3:>5.1f} {media:>7.2f}  {status}")

    print("=" * 62)
    print()


# ------------------------------------------------------------
# 7. BUSCAR UM ALUNO ESPECÍFICO
# ------------------------------------------------------------
def buscar_aluno(nome):
    """
    Retorna a linha completa de um aluno ou None se não existir.
    Útil para o Aluno 4 (POO) consultar os dados.
    """
       for linha in diario:
        if linha[0] == nome:
            return linha
    return None

#git
#-------------------------
if __name__ == "__main__":
    print("=== TESTE DO MÓDULO matriz_diario.py ===\n")

    # Adiciona alunos
    adicionar_aluno("Maria")
    adicionar_aluno("Joao")
    adicionar_aluno("Ana")

    # Lança notas
    lancar_nota("Maria", 1, 5.0)
    lancar_nota("Maria", 2, 6.0)
    lancar_nota("Maria", 3, 4.0)

    lancar_nota("Joao", 1, 8.0)
    lancar_nota("Joao", 2, 9.0)
    lancar_nota("Joao", 3, 8.5)

    lancar_nota("Ana", 1, 4.5)
    lancar_nota("Ana", 2, 5.0)
    lancar_nota("Ana", 3, 6.0)

    # Testa nota inválida
    print()
    print("Tentando lançar nota inválida (12):")
    lancar_nota("Maria", 1, 12)

    # Exibe relatório
    print()
    exibir_relatorio()

    # Mostra matriz crua para entender a estrutura
    print("Matriz diario (lista de listas):")
    for i, linha in enumerate(diario):
        print(f"  diario[{i}] = {linha}")