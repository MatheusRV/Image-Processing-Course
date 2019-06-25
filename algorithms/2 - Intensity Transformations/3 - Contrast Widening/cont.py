# Universidade Federal de Viçosa - Campus Rio Paranaíba
# Sistemas de Informação - Processamento Digital de Imagens
#
# Professor: Joao Mari
# Autores:
#          - MatheusRV (3929)
#          - iguit0 (3902)
#          - ThiagoMunich (3628)
#
# Transformações de intensidade - Alargamento de contraste
# Como Executar:
#  $ python cont.py img_1.tif saida
#

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from skimage import exposure

def loadImg(arg):
    return misc.imread(arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
saida = sys.argv[2]+'.tif'

# Define os limites do intervalo
v_min, v_max = np.percentile(img_1, (20, 80))

# Aplica a função para esticar os níveis de intensidade
img_saida = exposure.rescale_intensity(img_1, in_range = (v_min, v_max))

# Faz o salvamento da imagem de saída após o processamento
misc.imsave(saida, img_saida)

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
# Carrega uma imagem de baixo contraste a partir do módulo skimage.data.
im = data.moon()
# Converte o tipo de dados da imagem para float [0..1]
im = img_as_float(im)
# Imprime algumas informações sobre a imagem.
print(im.shape, im.min(), im.max(), im.mean(), im.std())

# Alargamento de contraste 1.
im_ac1 = exposure.rescale_intensity(im)
# Alargamento de contraste 2
im_ac2 = exposure.rescale_intensity(im, (0.2,0.6), (0.0,1.0))
# Equalização de histograma
im_eq = exposure.equalize_hist(im)

# Mostra as imagens na tela.
plt.figure()
plt.title('Processamento de histograma')
plt.axis('off')
plt.subplot(2,4,1)
plt.imshow(im,     cmap='gray')
plt.title('Imagem original')
plt.subplot(2,4,2)
plt.imshow(im_ac1, cmap='gray')
plt.title('Alarg. de constraste 1')
plt.subplot(2,4,3)
plt.imshow(im_ac2, cmap='gray')
plt.title('Alarg. de constraste 2')
plt.subplot(2,4,4)
plt.imshow(im_eq,  cmap='gray')
plt.title('Equalizacao de histograma')
plt.subplot(2,4,5)
plt.hist(im.flatten(),     256, range=(0, 1.), normed=True)
plt.title('Histograma')
plt.subplot(2,4,6)
plt.hist(im_ac1.flatten(), 256, range=(0, 1.), normed=True)
plt.title('Histograma')
plt.subplot(2,4,7)
plt.hist(im_ac2.flatten(), 256, range=(0, 1.), normed=True)
plt.title('Histograma')
plt.subplot(2,4,8)
plt.hist(im_eq.flatten(),  256, range=(0, 1.), normed=True)
plt.title('Histograma')
 
plt.show()
'''