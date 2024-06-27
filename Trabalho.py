def exibir_menu():
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Remover aluno")
    print("4 - Procurar aluno")
    print("5 - Listar aprovados")
    print("6 - Listar reprovados")
    print("7 - Procurar pelo nome do aluno")
    print("8 - Média da turma B1")
    print("9 - Média da turma B2")
    print("10 - Média da turma geral")
    print("11 - Diário da turma")
    print("0 - Sair")

def adicionar_aluno(alunos):
    ra = input("RA (5 caracteres): ").strip()
    nome = input("Nome (até 27 caracteres): ").strip()
    nota_b1 = float(input("Nota B1 (0 a 10): ").strip())
    nota_b2 = float(input("Nota B2 (0 a 10): ").strip())
    media = (nota_b1 + nota_b2) / 2
    alunos.append({"ra": ra, "nome": nome, "nota_b1": nota_b1, "nota_b2": nota_b2, "media": media})
    print("Aluno adicionado com sucesso.")

def listar_alunos(alunos):
    for aluno in alunos:
        print(f"RA: {aluno['ra']}, Nome: {aluno['nome']}, Nota B1: {aluno['nota_b1']}, Nota B2: {aluno['nota_b2']}, Média: {aluno['media']}")

def remover_aluno(alunos):
    ra = input("RA do aluno a remover: ").strip()
    for aluno in alunos:
        if aluno['ra'] == ra:
            alunos.remove(aluno)
            print("Aluno removido com sucesso.")
            return
    print("Aluno não encontrado.")

def procurar_aluno(alunos):
    ra = input("RA do aluno a procurar: ").strip()
    for aluno in alunos:
        if aluno['ra'] == ra:
            print(f"RA: {aluno['ra']}, Nome: {aluno['nome']}, Nota B1: {aluno['nota_b1']}, Nota B2: {aluno['nota_b2']}, Média: {aluno['media']}")
            return
    print("Aluno não encontrado.")

def listar_aprovados(alunos):
    for aluno in alunos:
        if aluno['media'] >= 7:
            print(f"RA: {aluno['ra']}, Nome: {aluno['nome']}, Média: {aluno['media']}")

def listar_reprovados(alunos):
    for aluno in alunos:
        if aluno['media'] < 7:
            print(f"RA: {aluno['ra']}, Nome: {aluno['nome']}, Média: {aluno['media']}")

def procurar_nome_aluno(alunos):
    nome = input("Nome do aluno a procurar: ").strip().lower()
    for aluno in alunos:
        if nome in aluno['nome'].lower():
            print(f"RA: {aluno['ra']}, Nome: {aluno['nome']}, Nota B1: {aluno['nota_b1']}, Nota B2: {aluno['nota_b2']}, Média: {aluno['media']}")
            return
    print("Aluno não encontrado.")

def media_turma_b1(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    media = sum(aluno['nota_b1'] for aluno in alunos) / len(alunos)
    print(f"Média da turma B1: {media:.2f}")

def media_turma_b2(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    media = sum(aluno['nota_b2'] for aluno in alunos) / len(alunos)
    print(f"Média da turma B2: {media:.2f}")

def media_turma_geral(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    media = sum(aluno['media'] for aluno in alunos) / len(alunos)
    print(f"Média geral da turma: {media:.2f}")

def diario_turma(alunos):
    print("--------------------------------------------------------")
    print("                   Diário da turma")
    print("--------------------------------------------------------")
    print("RA    Nome                      Nota B1  Nota B2   Média")
    print("--------------------------------------------------------")
    for aluno in alunos:
        ra = aluno['ra'].ljust(5)
        nome = aluno['nome'].ljust(27)
        nota_b1 = f"{aluno['nota_b1']:.2f}".rjust(6)
        nota_b2 = f"{aluno['nota_b2']:.2f}".rjust(6)
        media = f"{aluno['media']:.2f}".rjust(6)
        print(f"{ra} {nome} {nota_b1} {nota_b2} {media}")
    media_b1 = sum(aluno['nota_b1'] for aluno in alunos) / len(alunos)
    media_b2 = sum(aluno['nota_b2'] for aluno in alunos) / len(alunos)
    media_geral = sum(aluno['media'] for aluno in alunos) / len(alunos)
    print("--------------------------------------------------------")
    print(f"                  Médias da Turma  {media_b1:.2f}     {media_b2:.2f}    {media_geral:.2f}")
    print("--------------------------------------------------------")

def main():
    alunos = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            adicionar_aluno(alunos)
        elif opcao == '2':
            listar_alunos(alunos)
        elif opcao == '3':
            remover_aluno(alunos)
        elif opcao == '4':
            procurar_aluno(alunos)
        elif opcao == '5':
            listar_aprovados(alunos)
        elif opcao == '6':
            listar_reprovados(alunos)
        elif opcao == '7':
            procurar_nome_aluno(alunos)
        elif opcao == '8':
            media_turma_b1(alunos)
        elif opcao == '9':
            media_turma_b2(alunos)
        elif opcao == '10':
            media_turma_geral(alunos)
        elif opcao == '11':
            diario_turma(alunos)
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
