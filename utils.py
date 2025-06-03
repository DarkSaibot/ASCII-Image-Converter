from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def redimensionar_imagem(imagem, nova_largura=100):
    largura, altura = imagem.size
    proporcao = altura / largura
    nova_altura = int(nova_largura * proporcao * 0.55)
    return imagem.resize((nova_largura, nova_altura))

def converter_para_cinza(imagem):
    return imagem.convert("L")

def mapear_pixels_para_ascii(imagem):
    pixels = imagem.getdata()
    carecteres = "".join(ASCII_CHARS[pixel * len(ASCII_CHARS) // 256] for pixel in pixels)
    return carecteres

def gerar_ascii_art(imagem_path, largura=100):
    try:
        imagem = Image.open(imagem_path)
    except Exception as e:
        raise IOError(f"Erro ao abrir imagem: {e}")
    

    imagem = redimensionar_imagem(imagem, nova_largura=largura)
    imagem = converter_para_cinza(imagem)
    ascii_str = mapear_pixels_para_ascii(imagem)

    pixel_count = len(ascii_str)
    ascii_art = "\n".join(ascii_str[i:i+largura] for i in range(0, pixel_count, largura))
    return ascii_art

def salvar_ascii_em_arquivo(ascii_art, caminho_saida):
    with open(caminho_saida, "w", encoding='utf-8') as f:
        f.write(ascii_art)
        

