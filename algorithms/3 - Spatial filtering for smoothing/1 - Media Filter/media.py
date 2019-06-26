# Universidade Federal de Viçosa - Campus Rio Paranaíba
# Sistemas de Informação - Processamento Digital de Imagens
#
# Professor: Joao Mari
# Autores:
#          - MatheusRV (3929)
#          - iguit0 (3902)
#          - ThiagoMunich (3628)
#
# Filtragem espacial para suavização - Filtro da Média
# Como Executar:
#  $ python media.py img_1 saida <mask_size>
#  <mask_size> é um número inteiro. Exemplo: Se mask_size=3 então a máscara possui tamanho 3x3.
#

import sys
import os
import numpy as np
from scipy.ndimage import filters
import matplotlib.pyplot as plt
from scipy import misc
from skimage import color, data, util

def loadImg(arg):
    return misc.imread(arg)

img = loadImg(sys.argv[1])
saida = sys.argv[2] + '_media.tif'
ms = sys.argv[3]
ms = int(ms)
mascara = np.ones([ms, ms], dtype=float)
mascara = mascara / (ms * ms)

img_filtrada = filters.convolve(img, mascara, mode='constant', cval=0)

img_saida = misc.imsave(saida, img_filtrada)
