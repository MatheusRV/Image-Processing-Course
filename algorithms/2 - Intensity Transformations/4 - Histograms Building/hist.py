# Universidade Federal de Viçosa - Campus Rio Paranaíba
# Sistemas de Informação - Processamento Digital de Imagens
#
# Professor: Joao Mari
# Autores:
#          - MatheusRV (3929)
#          - iguit0 (3902)
#          - ThiagoMunich (3628)
#
# Transformações de intensidade -  Construção de histogramas
# Como Executar:
#  $ python hist.py img_1.tif
#
# Instruções do Projeto:
#  - OBS: Não gera imagem de saída!
#

import sys
import matplotlib.pyplot as plt
from scipy import misc 

def loadImg(arg):
    return misc.imread(arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
saida = 'histograma.tif'

# Transforma os níveis de intensidade numa imagem de uma dimensão
histograma = img_1.flatten()	

'''
# Organiza o plote das imagens
plt.figure()
plt.subplot(221)
plt.hist(histograma, bins=256, range=(0,255))
plt.title('histograma')
plt.savefig(saida)
plt.subplot(222)
plt.imshow(img_1, cmap='gray', interpolation='nearest')
plt.title('img_entrada')

# Plota as imagens de entrada e saída na tela
plt.show()
'''


'''
from scipy import misc 
import matplotlib.pyplot as plt
from skimage import img_as_float

# Carrega a imagem a partir do arquivo.
im = misc.imread('ascent.tif')

# Histograma da imagem (uint-8)
plt.figure()
plt.subplot(2,3,1)
plt.imshow(im, cmap='gray')
plt.colorbar()
plt.title('Imagem original - dtype=''uint8''.')
plt.subplot(2,3,2)
plt.hist(im.flatten(), bins=256, range=(0,255))
plt.title('Histograma nao normalizado.')
plt.subplot(2,3,3)
plt.hist(im.flatten(), bins=256, range=(0,255), normed=True)
plt.title('Histograma normalizado.')
# Converte a imagem de uint-8 [0..255] para float [0..1].

im = img_as_float(im)
# Histograma da imagem (float)
plt.subplot(2,3,4)
plt.imshow(im, cmap='gray')
plt.colorbar()
plt.title('Imagem original - dtype=''float''.')
plt.subplot(2,3,5)
plt.hist(im.flatten(), bins=256, range=(0,1))
plt.title('Histograma nao normalizado.')
plt.subplot(2,3,6)
plt.hist(im.flatten(), bins=256, range=(0,1), normed=True)
plt.title('Histograma normalizado.')

# Mostra as figuras na tela
plt.show()
'''