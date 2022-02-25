from bs4 import BeautifulSoup

#Arquivos
html = open('xml/publicacoes_davi.txt', 'r')
dados = open('dados/publicacoes_davi.txt', 'a')

#Lendo html do arquivo
conteudo = html.read()

#Instanciando o BeautifulSoup
site = BeautifulSoup(conteudo, 'html.parser')

#Encontrando todas as linhas (cada linha corresponde a uma publicação)
publicacoes = site.findAll('tr')

#Contador de td
count_td = 0

for publicacao in publicacoes:
    #Encontrar td dentro de tr
    informacoes = publicacao.findAll('td')

    #Percorrer cada coluna da linha
    for informacao in informacoes:
        #Ignorar primeira coluna
        if (count_td == 0): 
            count_td += 1
            continue
        
        link = informacao.find('a')

        if(link is None):
            texto = informacao.text
            dados.write(texto.replace('\n                   ', ''))
        else: 
            dados.write(link['href']) 

        dados.write('\n')

    count_td = 0
    dados.write('+++++++++++++++++++++++++++++++++++++++++++++++\n')

#Após o fim do algoritmo fecha o programa
html.close()
dados.close()