from limiarizacao import limiarizar
from utils.procurar_imagem import procurar_imagem

def main():
    print('Escolha uma imagem para limiarizar:')
    try:
        imagem_path = procurar_imagem()
        limiarizar(imagem_path)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

