
diario = []


def adicionar_aluno(nome):
    # Cria uma linha nova para o aluno com as três notas zeradas
    # e coloca no final da matriz.

    nova_linha = [nome, 0.0, 0.0, 0.0]
    diario.append(nova_linha)
    print("Aluno", nome, "adicionado ao diário.")


def lancar_nota(nome, numero_nota, valor):
    
    if valor < 0.0 or valor > 10.0:
        print("Erro: a nota precisa ser entre 0.0 e 10.0.")
        return False

    if numero_nota not in [1, 2, 3]:
        print("Erro: o número da nota precisa ser 1, 2 ou 3.")
        return False

    for linha in diario:
        if linha[0] == nome:
            linha[numero_nota] = valor
            print("Nota", numero_nota, "de", nome, "atualizada para", valor)
            return True

    print("Erro: aluno", nome, "não encontrado no diário.")
    return False


def calcular_media(linha):
    
    nota1 = linha[1]
    nota2 = linha[2]
    nota3 = linha[3]

    media = (nota1 + nota2 + nota3) / 3

    return round(media, 2)


def definir_status(media):

    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"


def processar_diario():
    
    resultados = []

    for linha in diario:

        nome = linha[0]

        notas = []
        for i in range(1, 4):
            notas.append(linha[i])

        media  = calcular_media(linha)
        status = definir_status(media)

        resultados.append([nome, notas[0], notas[1], notas[2], media, status])

    return resultados


def exibir_relatorio():

    if len(diario) == 0:
        print("Nenhum aluno cadastrado ainda.")
        return

    resultados = processar_diario()

    print()
    print("=" * 62)
    print("  NOME            N1     N2     N3    MÉDIA  STATUS")
    print("=" * 62)

    for r in resultados:
        nome   = r[0]
        n1     = r[1]
        n2     = r[2]
        n3     = r[3]
        media  = r[4]
        status = r[5]

        print(f"  {nome:<15} {n1:>5.1f}  {n2:>5.1f}  {n3:>5.1f}  {media:>5.2f}  {status}")

    print("=" * 62)
    print()


def buscar_aluno(nome):

    for linha in diario:
        if linha[0] == nome:
            return linha

    return None


if __name__ == "__main__":

    print("Testando o módulo matriz_diario.py")
    print()

    adicionar_aluno("Maria")
    adicionar_aluno("Joao")
    adicionar_aluno("Ana")

    print()

    lancar_nota("Maria", 1, 5.0)
    lancar_nota("Maria", 2, 6.0)
    lancar_nota("Maria", 3, 4.0)

    lancar_nota("Joao", 1, 8.0)
    lancar_nota("Joao", 2, 9.0)
    lancar_nota("Joao", 3, 8.5)

    lancar_nota("Ana", 1, 4.5)
    lancar_nota("Ana", 2, 5.0)
    lancar_nota("Ana", 3, 6.0)

    print()
    print("Testando nota inválida:")
    lancar_nota("Maria", 1, 12.0)

    exibir_relatorio()

    print("Matriz crua (para entender a estrutura):")
    for i, linha in enumerate(diario):
        print("  diario[" + str(i) + "] =", linha)

    print()
