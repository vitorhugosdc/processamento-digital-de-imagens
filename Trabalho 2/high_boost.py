import numpy as np
import cv2
import os

def high_boost_filtering(img_path, k=4.5, kernel_size=(3, 3)):
    # Carregar a imagem
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
    # Suavizar a imagem usando uma máscara de média
    kernel = np.ones(kernel_size, dtype=np.float32) / (kernel_size[0] * kernel_size[1])
    img_smoothed = cv2.filter2D(img, -1, kernel)
    
    # Calcular a imagem de detalhe
    detail_img = cv2.subtract(img, img_smoothed)
    
    # Aplicar high-boost
    img_enhanced = cv2.addWeighted(img, 1, detail_img, k, 0)
    
    return img_enhanced

def save_comparison(img_path, k=4.5):
    # Garantir que a pasta "resultados" exista
    if not os.path.exists("resultados"):
        os.mkdir("resultados")
    
    original_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    enhanced_img = high_boost_filtering(img_path, k)
    
    # Definir nomes de arquivo em formato .jpg
    #original_filename = os.path.splitext(os.path.basename(img_path))[0] + ".jpg"
    #enhanced_filename = "enhanced_" + os.path.splitext(os.path.basename(img_path))[0] + ".jpg"
    
# Definir nomes de arquivo
    original_filename = os.path.basename(img_path)
    enhanced_filename = "enhanced_k{}_".format(k) + original_filename
    
    cv2.imwrite(os.path.join("resultados", original_filename), original_img)
    cv2.imwrite(os.path.join("resultados", enhanced_filename), enhanced_img)

def selecionar_imagem():
    print("Selecione uma das imagens:")
    print("1 - 3.38.tif")
    print("2 - 3.40.tif")
    print("3 - Inserir seu próprio caminho de imagem")
    
    opcao = input("Digite o número correspondente à imagem desejada (1-3): ")

    if opcao == "1":
        return "3.38.tif"
    elif opcao == "2":
        return "3.40.tif"
    elif opcao == "3":
        return input("Digite o caminho completo da sua imagem: ")
    else:
        print("Opção inválida. Por favor, escolha novamente.")
        return selecionar_imagem()

def main():
    caminho_img = selecionar_imagem()
    k = float(input("Digite o valor de k: "))
    save_comparison(caminho_img, k)
    print(f"Imagens processadas e salvas na pasta 'resultados'.")

if __name__ == "__main__":
    main()
