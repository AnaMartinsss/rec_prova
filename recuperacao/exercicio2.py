"""
2) Cadastro de Filmes

Objetivo:
Crie uma função chamada cadastrar_filmes() que simule um pequeno sistema de cadastro de filmes. Essa função deve:
- Utilizar uma tupla fixa chamada generos (por exemplo, ("Ação", "Comédia", "Drama", "Fantasia", "Terror")). feito
- Pedir ao usuário o título de 3 filmes e o índice do gênero (com base na tupla). feito
- Armazenar os dados em um dicionário, onde a chave é o título e o valor é o gênero (string). feito
- Ao final, exibir quantos filmes de cada gênero foram cadastrados feito.

Observação:
- Você pode usar uma lista para armazenar títulos antes de inseri-los no dicionário, mas não é obrigatório.
- A contagem de filmes por gênero pode ser feita percorrendo o dicionário ou usando outro dicionário auxiliar.

Exemplo de Chamada:
    cadastrar_filmes()
    # Durante a execução:
    # - O programa pede 3 filmes + índice do gênero
    # - Depois exibe quantos filmes de cada gênero foram cadastrados

Requisitos:
- Utilize ao menos uma tupla para gêneros.
- Armazene os filmes cadastrados em um dicionário.
- Exiba ao final um resumo da quantidade de filmes por gênero.
"""
# Solution:


def cadastrar_filmes():
    generos = ("Ação", "Comédia", "Drama", "Fantasia", "Terror")

    print("Gêneros disponíveis:")
    for i, genero in enumerate(generos):
        print(f"{i} - {genero}")

    filmes = {}
    for _ in range(3):
        titulo = input("Digite o título do filme: ")
        while True:
                indice_genero = int(input(f"Escolha o índice do gênero (0-{len(generos)-1}): "))
                if 0 <= indice_genero < len(generos):
                    filmes[titulo] = generos[indice_genero]
                    break
                else:
                    print("Por favor, escolha um índice válido.")
    

    print("\nResumo do cadastro de filmes:")
    for genero in generos:
        print(f"{genero}: {list(filmes.values()).count(genero)} filme(s)")

cadastrar_filmes()
