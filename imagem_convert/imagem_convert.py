from PIL import Image
import os
lista_arquivos = os.listdir("imagem_convert\images")
for arquivo in lista_arquivos:
    imagem = Image.open(f"imagem_convert\images/{arquivo}")
    imagem.save(f"imagem_convert\jpg/{arquivo.replace('webp', 'jpg')}")
