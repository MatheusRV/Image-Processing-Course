# Universidade Federal de Viçosa - Campus Rio Paranaíba
# Sistemas de Informação - Processamento Digital de Imagens
#
# Professor: Joao Mari
# Autores:
#          - MatheusRV (3929)
#          - iguit0 (3902)
#          - ThiagoMunich (3628)
#
# Segmentação – Limiarização - Efeito da suavização na limiarização
# Como Executar:
#  $ python lim_s.py img_1.tif saida <mask_size>
#
# Instruções do Projeto:
#  - Utilizar o filtro da média.
#  - Utilizar o método de Otsu.
#

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc 
from skimage import img_as_float, filters
from scipy.ndimage import filters as fil

def loadImg(arg):
    return misc.imread(arg)

# Lê a imagem a partir de um arquivo
img_1 = loadImg(sys.argv[1])
saida = sys.argv[2]+'.tif'
mask_size = int(sys.argv[3])

# Converte os pixels em float, com valores entre 0 e 1
img_1 = img_as_float(img_1)

# Aplica o filtro da média
ave_masc = np.ones([mask_size, mask_size], dtype = float)
ave_masc = ave_masc / (mask_size * mask_size)
img_media = fil.correlate(img_1, ave_masc)

# Limiar de Otsu
l_otsu = filters.threshold_otsu(img_media)

# Segmenta a imagem por limiarização
img_saida = img_media < l_otsu

# Faz o salvamento das imagens de saída após o processamento
misc.imsave(saida, img_saida.astype(np.uint8))

'''
# Organiza o plote das imagens
plt.figure() 
plt.subplot(221); 
plt.imshow(img_1, cmap='gray', interpolation='nearest'); 
plt.title('img_entrada')
plt.subplot(222); 
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('img_saida')

# Plota as imagens de entrada e saída na tela
plt.show()
'''