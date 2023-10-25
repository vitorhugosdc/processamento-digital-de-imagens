import numpy as np
import cv2
import matplotlib.pyplot as plt

def high_boost_filtering(img_path, k=4.5, blur_mask_size=(3, 3)):
    # Carregar a imagem
    #img = f_x_y
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
    # máscara de média
    blur_mask = np.ones(blur_mask_size, dtype=np.float32) / (blur_mask_size[0] * blur_mask_size[1])
    
    #1. Borrar a imagem original
    #img_blurred = f^_ (f_borrada)
    img_blurred = cv2.filter2D(img, -1, blur_mask)
    
    #2.  Subtrai a imagem borrada da original (a diferença resultante é chamada de máscara)
    #mask = g_mascara(x,y)
    mask = cv2.subtract(img, img_blurred)
    
    # 3. Adicionar a máscara à imagem original
    #img_highboost = g_x_y
    img_highboost = cv2.addWeighted(img, 1, mask, k, 0)
    
    return img, img_blurred, mask, img_highboost

def show_individual_image(img, title):
    plt.figure(figsize=(6,6))
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.subplots_adjust(left=0, right=1, top=0.95, bottom=0)
    
def show_comparison(img_path, k=4.5):    
    original_img, blurred_img, mask, highboost_img = high_boost_filtering(img_path, k)

    show_individual_image(original_img, "Original Image")
    show_individual_image(blurred_img, "Blurred Image")
    show_individual_image(mask, "Mask")
    show_individual_image(highboost_img, "Highboost Image")

    plt.show()

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
    img_path = selecionar_imagem()
    k = float(input("Digite o valor de k: "))
    show_comparison(img_path, k)

if __name__ == "__main__":
    main()
