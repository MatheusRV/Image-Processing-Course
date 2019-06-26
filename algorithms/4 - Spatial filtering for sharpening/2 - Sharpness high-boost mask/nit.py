# Universidade Federal de Viçosa - Campus Rio Paranaíba
# Sistemas de Informação - Processamento Digital de Imagens
#
# Professor: Joao Mari
# Autores:
#          - MatheusRV (3929)
#          - iguit0 (3902)
#          - ThiagoMunich (3628)
#
# Filtragem espacial para aguçamento - Máscara de nitidez e high-boost
# Como Executar:
#  $ python nit.py <img_entrada> <img_saida>

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
saida = sys.argv[2] + '_nit.tif'

# Mascaras - Laplaciano 4
lap_4 = np.array([[0.,  1., 0.],
                   [1., -4., 1.],
                   [0.,  1., 0.]], dtype=float)

img_lap_4 = filters.convolve(img, lap_4)


# Aguçamento usando o Laplaciano.
# ===============================
# Ajusta a intensidade para evitar pixels < que 0.
img_lap_4_i = im_lap_4 + np.abs(img_lap_4.min())

# Constante
c1 = -1.
# Imagens aguçadas.
img_lap_4_ag = img + c1 * img_lap_4_i

img_saida = misc.imsave(saida, img_lap_4_ag)
