# Redes Neurais - Redimensionalidade
Redução de Dimensionalidade em Imagens para Redes Neurais


### Projeto para redução de dimensionalidade em imagens.

Material esse proposto para prática de dimensionalizar imagens para utilização em Redes Neurais, apresentado para a formação de Machine Learning Especialista na DIO.
https://web.dio.me/track/formacao-machine-learning-specialist

Seguindo o algoritmo de binarização apresentado, demonstração de uma implementação em Python para transformar uma imagem colorida (entrada.jpg) para níveis de cinza (0 a 255) e para binarizada utilizando a média da vizinhança e soma ponderada da vizinhança (0 e 255), preto e branco.


Explicando o uso dos parametros
     Sintaxe : cv2.adaptiveThreshold (source, maxVal, adaptiveMethod, thresholdType, blocksize, constant)

    Parâmetros:
    -> fonte : array de imagem de entrada (canal único, 8 bits ou ponto flutuante)
    -> maxVal : valor máximo que pode ser atribuído a um pixel.
    -> adaptiveMethod : o método adaptativo decide como o valor limite é calculado.

     cv2.ADAPTIVE_THRESH_MEAN_C : Valor limite = (média dos valores da área de vizinhança - valor constante). Em outras palavras, é a média da vizinhança blockSize × blockSize de um ponto menos constante.


    cv2.ADAPTIVE_THRESH_GAUSSIAN_C : Valor limite = (soma ponderada em Gauss dos valores de vizinhança - valor constante). Em outras palavras, é uma soma ponderada da vizinhança blockSize × blockSize de um ponto menos constante.

    -> thresholdType : o tipo de limite a ser aplicado.
    -> blockSize : tamanho de uma vizinhança de pixel que é usada para calcular um valor limite.
    -> constante : um valor constante que é subtraído da média ou soma ponderada dos pixels da vizinhança. 
    
    
    Material retirado do site:
    https://acervolima.com/python-tecnicas-de-limiarizacao-usando-opencv-conjunto-2-limiar-adaptativo/
