from config import PAIS
from helpers import top_noticias


if __name__ == '__main__':
    noticias = top_noticias(PAIS)

    print('Listando as top notícias do país selecionado')
    for numero in range(len(noticias)):
        print(f"{numero + 1} - {noticias[numero]}")

