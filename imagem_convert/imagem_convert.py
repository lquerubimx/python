from PIL import Image
import os
lista_arquivos = os.listdir('images')
for arquivo in lista_arquivos:
    imagem = Image.open(f"images/{arquivo}")
    imagem.save(f"jpg/{arquivo.replace('webp', 'jpg')}")
