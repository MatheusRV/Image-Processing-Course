
# Universidade Federal de Viçosa - Campus Rio Paranaíba
# Sistemas de Informação - SIN392 Processamento Digital de Imagens
#
# Professor: Joao Mari
# Autores:
#          - MatheusRV (3929)
#          - iguit0 (3902)
#          - ThiagoMunich (3628)
#
# Segmentação – Limiarização - Limiarização utilizando o método de Otsu 
# Como Executar:
#  $ python otsu.py img_1.tif saida
#

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from skimage import img_as_float, filters

def loadImg(arg):
    return misc.imread(arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
saida = sys.argv[2]+'.tif'

# Converte os pixels em float, com valores entre 0 e 1
img_1 = img_as_float(img_1.astype(np.uint8))

# Limiar de Otsu
l_otsu = filters.threshold_otsu(img_1)

img_saida = img_1 < l_otsu

# Faz o salvamento das imagens de saída após o processamento
misc.imsave(saida, img_saida.astype(np.uint8))

'''
# Organiza o plote das imagens
plt.figure() 
plt.subplot(221); 
plt.imshow(img_1, cmap='gray', interpolation='nearest'); 
plt.title('img_entrada')
plt.subplot(222); 
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('img_saida')

# Plota as imagens de entrada e saída na tela
plt.show()
'''
