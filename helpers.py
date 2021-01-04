import requests
from config import CHAVE_API, PAIS, URL_BASE_TOP_HEADLINES


def top_noticias(pais):
    """
    Retorna as top noticias do site NewsApi.org
    :param pais: inserir o país para pesquisar as noticias
    :return: lista de noticias do país informado
    """
    url = f"{URL_BASE_TOP_HEADLINES}country={PAIS}&apiKey={CHAVE_API}"

    # Coletando dados em formato JSON
    resultado = requests.get(url).json()
    #print(resultado)

    # Pegando todos os artigos
    artigos = resultado['articles']
    #print(artigos)

    # Lista vazia para preencher com as noticias
    noticias = []

    for artigo in artigos:
        noticias.append(f"Título: {artigo['title']},"
                        f"Imagem: {artigo['urlToImage']},"
                        f"Publicado em: {artigo['publishedAt']}, ")

    #print(noticias)
    return noticias
