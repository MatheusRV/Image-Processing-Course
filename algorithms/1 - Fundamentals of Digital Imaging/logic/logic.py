# Universidade Federal de Viçosa - Campus Rio Paranaíba
# Sistemas de Informação - Processamento Digital de Imagens
#
# Professor: Joao Mari
# Autores:
#          - MatheusRV (3929)
#          - iguit0 (3902)
#          - ThiagoMunich (3628)
#
# Fundamentos de imagens digitais - Operações lógicas sobre imagens
# Como Executar:
#  $ python logic.py <img_entrada_1> <img_entrada_2> <img_saida>
#
# Instruções do Projeto:
# - Escolher uma operação lógica (AND ou OR).
# - Operação escolhida: AND

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

def loadImg(arg):
    return misc.imread("../../../assets/"+arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
img_2 = loadImg(sys.argv[2])
saida = sys.argv[3]+'.tif'

# Faz a operacao logica AND entre as imagens lidas
img_saida = np.logical_and(img_1,img_2)

# Faz o salvamento da imagem de saída após o processamento
misc.imsave(saida, img_saida.astype(np.uint8)) 

# Organiza o plote das imagens
'''
plt.figure()
plt.subplot(221)
plt.imshow(img_1, cmap='gray', interpolation='nearest')
plt.title('img_1')
plt.subplot(222)
plt.imshow(img_2, cmap='gray', interpolation='nearest')
plt.title('img_2')
plt.subplot(223)
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('img_saida')

# Plota as imagens de entrada e saída na tela
plt.show()
'''