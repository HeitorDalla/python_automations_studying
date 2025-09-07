# Verificar se a professora é 'Carolina' e exibir apenas os alunos dela

# Abrir o arquivo de texto
arquivo = open('C:\\Users\Admin\\Desktop\\automations\\python_automations_studying\\automations\\notepad\\Alunos.txt')
arquivo = open('C:\\Users\Admin\\Desktop\\automations\\python_automations_studying\\automations\\notepad\\Professora.txt')

linhas = arquivo.readlines()

for linha in linhas:
    # print(linha)

    # Quebra de linha
    quebra_linha = linha.split(',') # vai criar uma lista de cada linha
    # print(quebra_linha)

    # Faz uma única divisão e pega os itens a partir da coluna 1 (tira a primeira coluna)
    linha = [item.split(';', 1)[1] for item in quebra_linha]
    # print(linha)

    # Separando a linha em coluna atravéz do delimitador ';'
    separaLinhaEmColuna = linha[0].split(';')
    # print(separaLinhaEmColuna)

    # Pegando a posição do nome da professora
    professora = separaLinhaEmColuna[0]

    if professora == 'Carolina':
        # Pegando o nome do aluno
        nome_aluno = separaLinhaEmColuna[2]
        print(nome_aluno)

        # Verificando que não pegue a primeira linha (rótulos)

        if separaLinhaEmColuna[3] == 'Linha 1':
            print("-------------------")
        else:
            nota1 = int(separaLinhaEmColuna[3])
            nota2 = int(separaLinhaEmColuna[4])
            nota3 = int(separaLinhaEmColuna[5])
            nota4 = int(separaLinhaEmColuna[6])
            faltas = int(separaLinhaEmColuna[7])

            media = nota1 + nota2 + nota3 + nota4 / 4
            print("A média é: ", media)

            if faltas > 4:
                print("Voce reprovou por falta!!")
            else:
                if media < 3:
                    print("Voce reprovou por media!")
                elif media < 6:
                    print("Voce esta de recuperação!")
                else:
                    print("Voce não reprovou!")
                    print('-------------------')