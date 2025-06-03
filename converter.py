import argparse
from utils import gerar_ascii_art, salvar_ascii_em_arquivo

def main():
    parser = argparse.ArgumentParser(description="Converte imagens para ASCII Art.")
    parser.add_argument("--input", required=True, help="Caminho da imagem de entrada")
    parser.add_argument("--output", help="Arquivo de saída (opcional)")
    parser.add_argument("--width", type=int, default=100, help="Largura da saída em caracteres")

    args = parser.parse_args()

    try:
        ascii_art = gerar_ascii_art(args.input, largura=args.width)
        if args.output:
            salvar_ascii_em_arquivo(ascii_art, args.output)
            print(f"ASCII Art salva em {args.output}")
        else:
            print(ascii_art)
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()

