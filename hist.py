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
#  $ python hist.py <img_entrada>
#
# Instruções do Projeto:
#  - Não gera imagem de saída
#

## TODO: Remover Equalização da função

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