import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função que altera faixas de matizes em uma imagem.
def alteraFaixaMatizes(caminho_img, m, x):
    # Carregando a imagem.
    img = cv2.imread(caminho_img)

    # Convertendo a imagem de BGR (padrão OpenCV) para o espaço de cor HSV.
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Isolando o canal de matiz (Hue) da imagem HSV.
    hue = hsv[:, :, 0]
    
    # Calculando os limites superiores e inferiores do intervalo de matizes que serão alterados.
    limite_superior = np.mod((m + x)/2, 180)
    limite_inferior = np.mod((m - x)/2, 180)
    
    # Convertendo a matriz do canal de matiz para uint16 para evitar overflow durante operações.
    hue = hue.astype(np.uint16)
    
    # Determinando os pixels cujas matizes estão dentro do intervalo definido.
    # Considerando o caso em que os matizes circulam passando pelo 0 (por exemplo, de 170 a 10)
    if(limite_inferior < limite_superior):
        mascara = (hue >=  limite_inferior) & (hue <= limite_superior)
    else:
        mascara = (hue >= limite_inferior) | (hue <= limite_superior)
    
    # Alterando as matizes dos pixels selecionados pela máscara (rotacionando-os em 90 graus, ou seja, um semicirculo).
    hue[mascara] = np.mod(hue[mascara] + 90, 180)
    
    # Atualizando a imagem HSV com o canal de matiz modificado, retornando para uint8.
    hsv[:,:,0] = hue.astype(np.uint8)

    # Convertendo a imagem de volta do espaço HSV para BGR.
    img_saida = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # Plotando a imagem original e a imagem alterada lado a lado
    plt.figure(figsize=(14, 8))
    plt.subplot(1, 2, 1)
    plt.title("Imagem Original", fontsize=16)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(img_saida, cv2.COLOR_BGR2RGB))
    plt.title("Imagem Alterada", fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# Solicitando os valores de m e x do usuário.
m = int(input("Digite o valor de m: "))
x = int(input("Digite o valor de x: "))

caminho_img = "passaros.jpg"
alteraFaixaMatizes(caminho_img, m, x)