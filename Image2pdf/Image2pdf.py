import os

from PIL import Image
from reportlab.pdfgen import canvas

# Obtém o diretório atual onde o script é executado
diretorio_atual = os.getcwd()


# Função para criar um PDF para cada imagem no diretório atual
def cria_pdfs_para_imagens(diretorio):
    # Lista todos os arquivos no diretório atual
    arquivos = os.listdir(diretorio)

    # Verifica cada arquivo no diretório atual
    for arquivo in arquivos:
        # Verifica se é um arquivo de imagem suportado
        if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Caminho completo para a imagem
            caminho_imagem = os.path.join(diretorio, arquivo)

            # Nome do arquivo PDF de saída baseado no nome da imagem
            nome_pdf = os.path.splitext(arquivo)[0] + '.pdf'
            caminho_pdf = os.path.join(diretorio, nome_pdf)

            # Abre a imagem usando Pillow para obter as dimensões
            img = Image.open(caminho_imagem)
            largura, altura = img.size

            # Cria um PDF para cada imagem com o tamanho da imagem
            c = canvas.Canvas(caminho_pdf, pagesize=(largura, altura))
            try:
                # Insere a imagem no PDF sem redimensionamento
                c.drawInlineImage(caminho_imagem, 0, 0, width=largura, height=altura)

                # Salva o arquivo PDF
                c.save()
                print(f'PDF gerado com sucesso: {caminho_pdf}')

            except Exception as e:
                print(f"Erro ao processar imagem {caminho_imagem}: {e}")


# Chama a função para criar PDFs para todas as imagens no diretório atual
cria_pdfs_para_imagens(diretorio_atual)
