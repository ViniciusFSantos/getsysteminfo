import subprocess
import platform, os, psutil, sys
from traceback import print_tb
import time
import math
from pathlib import Path



info_geral = []

os.system('color a')
print('\n================================== SysGetInfo ============================================\n')

titulo = '================================== SysGetInfo ============================================\n'
info_geral.append(titulo)

sistema_operacional = 'Sistema Operacional =', platform.system(), platform.version(), platform.win32_edition()
print('\nSistema Operacional =', platform.system(), platform.version(), platform.win32_edition())   
info_geral.append(sistema_operacional)     
                                                                                           
#---------------------------
uname_list =[]   
uname = platform.uname()

for dado in uname:
    uname_list.append(dado)

nomepc = 'Nome do computador =', uname_list[1]
print('Nome do computador =', uname_list[1]) 
info_geral.append(nomepc)  

#---------------------------

calc_memoria_fisica = psutil.virtual_memory().total / (1024.0 **3)
resultado = 'Memória RAM = {:.0f}gb'.format(round(calc_memoria_fisica))
print('Memória RAM = {:.0f}gb'.format(round(calc_memoria_fisica)))
info_geral.append(resultado)  

#---------------------------

print('--------------------- Análise de armazenamento secundário --------------------\n')
subprocess.run('wmic diskdrive get model, size, serialnumber')
print('------------------------------------------------------------------------------\n')

#--------------------------

armazenamento = subprocess.run('wmic diskdrive get model, size, serialnumber', capture_output=True, text=True)
armazenamento_list = []

text1 = '--------------------- Análise de armazenamento secundário --------------------'
info_geral.append('\n')
info_geral.append(text1)
info_geral.append(armazenamento.stdout)  
text2 = '------------------------------------------------------------------------------'
info_geral.append(text2)


end = '\n=========================================================================================='
info_geral.append(end)

print('\n==========================================================================================\n')
#------------- END GetSysInfo--------------------


#---------- Cria arquivo txt----------------------

filepath = 'D:\\' + f'{nomepc[1]}.txt'   #troque aqui para o diretorio desejado
try:
    with open(filepath, 'w') as arquivo:
        for valor in info_geral:
            arquivo.write(str(valor)+'\n')
    print('Arquivo .txt salvo com sucesso!')
except:
    print('Algo deu errado ao salvar o arquivo .txt contate o desenvolvedor')

time.sleep(600)