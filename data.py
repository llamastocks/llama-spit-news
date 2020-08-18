#Extracción de estados financieros solicitados
#Fase 1: Actualizar lista de empresas en SMV
import sys
sys.path.append("/home/mauricio/Desktop/prueba/tcperu")
from smv import list_bvl

bvl=list_bvl()
print(len(bvl)-1)
#bvl=Lista de empresas en SMV actualizada

#Fase 2: Extracción de link por empresa