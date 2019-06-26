# Universidade Federal de Viçosa - Campus Rio Paranaíba
# Sistemas de Informação - Processamento Digital de Imagens
#
# Professor: Joao Mari
# Autores:
#          - MatheusRV (3929)
#          - iguit0 (3902)
#          - ThiagoMunich (3628)
#
# Filtragem espacial para suavização - Filtro de máximo e mínimo
# Como Executar:
# $ python maxmin.py <img_entrada> <img_saida_min> <imgsaida_max> <mask_size>
# <mask_size> é um número inteiro. Exemplo: Se mask_size=3 então a máscara possui tamanho 3x3.
# Gera duas imagens de saída.

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
saida1 = sys.argv[2] + '_max.tif'
saida2 = sys.argv[3] + '_min.tif'
ms = sys.argv[4]
ms = int(ms)

img_filtro_max = filters.maximum_filter(img, size=ms)
img_filtro_min = filters.minimum_filter(img, size=ms)

img_saida1 = misc.imsave(saida1, img_filtro_max)
img_saida2 = misc.imsave(saida2, img_filtro_min)

