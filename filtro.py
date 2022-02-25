arquivo = open('dados/publicacoes_davi.txt', 'r')
destino = open('dados_filtrados.txt', 'w')

conteudo = arquivo.read()

novo_conteudo = conteudo.replace("""+++++++++++++++++++++++++++++++++++++++++++++++
Título
Autores

Revista/Periódico


Volume


Número

Página(s)
Ano
Editora
Arquivo/Link""", '')

novo_conteudo = novo_conteudo.replace("""+++++++++++++++++++++++++++++++++++++++++++++++









""", '')

novo_conteudo = novo_conteudo.replace("                \n", '')


destino.write(novo_conteudo)