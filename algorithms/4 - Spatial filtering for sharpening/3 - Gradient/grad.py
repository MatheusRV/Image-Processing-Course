# Universidade Federal de Viçosa - Campus Rio Paranaíba
# Sistemas de Informação - Processamento Digital de Imagens
#
# Professor: Joao Mari
# Autores:
#          - MatheusRV (3929)
#          - iguit0 (3902)
#          - ThiagoMunich (3628)
#
# Filtragem espacial para aguçamento - Gradiente
# Como Executar:
#  $ python grad.py <img_entrada> <img_saida>
# Utilizar o gradiente de Sobel

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
saida = sys.argv[2] + '_grad.tif'

sob_h = np.array([[-1., -2., -1.],
                  [ 0.,  0.,  0.],
                  [ 1.,  2.,  1.]], dtype=float)


# Gradiente de Sobel.
img_sob_h  = filters.convolve(img, sob_h)

img_saida = misc.imsave(saida, img_sob_h)
