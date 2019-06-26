# Universidade Federal de Viçosa - Campus Rio Paranaíba
# Sistemas de Informação - Processamento Digital de Imagens
#
# Professor: Joao Mari
# Autores:
#          - MatheusRV (3929)
#          - iguit0 (3902)
#          - ThiagoMunich (3628)
#
# Transformações de intensidade - Equalização de histograma
# Como Executar:
#  $ python eq.py img_1.tif saida
#

import sys
import matplotlib.pyplot as plt
from scipy import misc 
from skimage import exposure

def loadImg(arg):
    return misc.imread(arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
saida = sys.argv[2]+'.tif'

# Aplica a equalização do histograma e retorna a imagem
img_saida = exposure.equalize_hist(img_1)

# Faz o salvamento da imagem de saída após o processamento
misc.imsave(saida, img_saida)
'''
# Organiza o plote das imagens
plt.figure()
plt.subplot(221)
plt.imshow(img_1, cmap='gray', interpolation='nearest')
plt.title('img_entrada')
plt.subplot(222)
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('img_saida')

# Plota as imagens de entrada e saída na tela
plt.show()
'''