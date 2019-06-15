# Universidade Federal de Viçosa - Campus Rio Paranaíba
# Sistemas de Informação - Processamento Digital de Imagens
#
# Professor: Joao Mari
# Autores:
#          - MatheusRV (3929)
#          - iguit0 (matriculaIgorNum)
#
# Fundamentos de imagens digitais - Operações aritméticas sobre imagens
# Como Executar:
#  $ python aritm.py <img_entrada_1> <img_entrada_2> <img_saida>
#
# Instruções do Projeto:
#  - Escolher uma operação aritmética (soma, subtração, multiplicação ou divisão).
#

## TODO: Implementar a operação aritmética soma
## TODO: Decidir se vale a pena implementar uma divisão

import numpy as np
from scipy import misc, ndimage
import matplotlib.pyplot as plt

## Multiplicação

# Lê a imagem a partir de um arquivo
im = misc.imread('ascent.tif')
 
# Obtem a forma do arranjo. 
num_l, num_c = im.shape
# Constrói a mascara. 
mascara = np.zeros([num_l, num_c], dtype=float)
mascara[200:300, 350:450] = 1
# Mascaramento usando multiplicação. 
im_rdi = im * mascara

# Plota as imagens em uma figura.
plt.figure() # Cria uma nova figura 
# Divide a área de plotagem: 1 linha e 3 colunas.
plt.subplot(1,3,1) # A área ativa é a 1.
plt.imshow(im, cmap='gray')
plt.axis('off')
plt.title('Imagem original')
plt.subplot(1,3,2) # Agora a área ativa é a 2.
plt.imshow(mascara, cmap='gray')
plt.title('Imagem mascara (binaria)')
plt.subplot(1,3,3) # A área ativa é a 3.
plt.imshow(im_rdi, cmap='gray')
plt.title('RdI isolada por mascaramento')
plt.show()

## Subtração

# Lê as imagens a partir de arquivos
im_l = misc.imread('../data/dip_3ed/ch03/angiography_live_image.tif')
im_m = misc.imread('../data/dip_3ed/ch03/angiography_mask_image.tif')

# Subtrai imagem máscara da imagem ativa.
im_sub = im_l.astype(np.float) - im_m.astype(np.float)

# Plota as imagens em uma figura.
# Cria uma nova figura 
plt.figure() 
# Divide a área de plotagem: 1 linha e 3 colunas.
plt.subplot(1,3,1) # A área ativa é a 1.
plt.imshow(im_l, cmap='gray')
plt.axis('off')
plt.title('Imagem ativa - antes do contraste')
plt.subplot(1,3,2) # Agora a área ativa é a 2.
plt.imshow(im_m, cmap='gray')
plt.title('Imagem mascara - apos do contraste')
plt.subplot(1,3,3) # A área ativa é a 3.
plt.imshow(im_sub, cmap='gray')
plt.title('Resultado da subtracao')
plt.show()



# Grava a imagem 'im' em arquivo com nome 'ascent.tif'
misc.imsave('ascent.tif', im)



# Mostra as figuras na tela
plt.show()