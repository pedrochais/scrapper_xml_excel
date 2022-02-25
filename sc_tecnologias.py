from bs4 import BeautifulSoup

#Arquivos
html = open('conteudo_tecnologias.txt', 'r')
dados = open('dados_tecnologias.txt', 'a')

#Lendo html do arquivo
conteudo = html.read()

#Instanciando o BeautifulSoup
site = BeautifulSoup(conteudo, 'html.parser')

#Encontrando conteúdos dentro da tag 'td'
tecnologias = site.find_all('td')

#Contador de dados (Limite: 6)
count = 0

for tecnologia in tecnologias:
    #Busca pela tag 'a'
    link = tecnologia.find('a')

    if(link is None): dados.write(tecnologia.text)
    else: dados.write(link['href'])

    dados.write('\n')

    count += 1
    if count == 6:
        dados.write('+++++++++++++++++++++++++++++++++++++++++++++++')
        count = 0

#Após o fim do algoritmo fecha o programa
html.close()
dados.close()