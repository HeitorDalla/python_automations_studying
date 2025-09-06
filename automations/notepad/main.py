# Abrir o arquivo de text
arquivo = open('C:\\Users\Admin\\Desktop\\automations\\python_automations_studying\\automations\\notepad\\Alunos.txt')

linhas = arquivo.readlines()

for linha in linhas:
    # Quebra de linha
    quebra_linha = linha.split(',')
    # print(quebra_linha)

    # Faz uma única divisão e pega os itens a partir da coluna 1 (tira a primeira coluna)
    linha = [item.split(';', 1)[1] for item in quebra_linha]
    # print(linha)

    # Separando a linha em coluna atravéz do delimitador ';'
    separaLinhaEmColuna = linha[0].split(';')
    # print(separaLinhaEmColuna)

    # Pegando o nome do aluno
    nome_aluno = separaLinhaEmColuna[2]

    print(nome_aluno)