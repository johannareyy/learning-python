"""
import bib                          #importar bib mas precisa referenciar de onde vem cada funcao

print(bib.produto(2,3))
print(bib.soma(2,3))
"""


#import bib
#import bib as b
from bib import produto, soma       #importar só essas funcoes da bib
#from bib import *                  importar tudo (todas as funcoes) da bib

print(produto(2,3))
print(soma(2,3))
