# Universidade Federal de Viçosa - Campus Rio Paranaíba
# Sistemas de Informação - Processamento Digital de Imagens
#
# Professor: Joao Mari
# Autores:
#          - MatheusRV (3929)
#          - iguit0 (3902)
#          - ThiagoMunich (3628)
#
# Fundamentos de imagens digitais - Operações aritméticas sobre imagens
# Como Executar:
#  $ python aritm.py img_1.tif img_2.tif saida
#
# Instruções do Projeto:
#  - Escolher uma operação aritmética (soma, subtração, multiplicação ou divisão).
#  - Operação escolhida: Subtração

import sys
from scipy import misc
from skimage import data, util, color
import matplotlib.pyplot as plt

def loadImg(arg):
    return misc.imread(arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
img_2 = loadImg(sys.argv[2])
saida = sys.argv[3]+'.tif'

# Faz a subtração entre as imagens lidas
img_saida = img_1 - img_2

# Faz o salvamento da imagem de saída após o processamento
misc.imsave(saida, img_saida)

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