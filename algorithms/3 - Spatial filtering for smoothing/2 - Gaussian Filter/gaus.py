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
# $ python gauss.py <img_entrada> <img_saida> <stdev>
# <stdev> é o desvio padrão da Gaussiana.

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
saida = sys.argv[2] + '_gauss.tif'
std = sys.argv[3]
std = float(std)

img_gauss = filters.gaussian_filter(img, sigma=std)


img_saida = misc.imsave(saida, img_gauss)
