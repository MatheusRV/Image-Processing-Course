# Universidade Federal de Viçosa - Campus Rio Paranaíba
# Sistemas de Informação - Processamento Digital de Imagens
#
# Professor: Joao Mari
# Autores:
#          - MatheusRV (3929)
#          - iguit0 (3902)
#          - ThiagoMunich (3628)
#
# Filtragem espacial para aguçamento - Laplaciano
# Como Executar:
#  $ python lap.py <img_entrada> <img_saida>
# Utilizar máscara laplaciana com centro -4

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

saida = sys.argv[2] + '_lap.tif'

# Mascaras - Laplaciano 4
lap_4 = np.array([[ 0.,  1., 0.],
                   [ 1., -4., 1.],
                   [ 0.,  1., 0.]], dtype=float) 

img_lap_4  = filters.convolve(img, lap_4)

img_saida = misc.imsave(saida, img_lap_4)
