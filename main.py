#Importação da Biblioteca

import pyautogui as auto #Para apelidar a biblioteca para um nome mais curto utilizar 'as'.

#Define o tempo de espera para a execução de cada comenado

auto.PAUSE = 0.5

#Abre o menu inicar

auto.press('win') #O comando 'win' é abreviação do menu iniciar na biblioteca pyautogui

#Abrir o chrome

auto.write('chrome')
auto.press('enter')

#Maximizar tela

auto.hotkey('alt','space') #O comando hotkey é utilizado para combinação de teclas, teclas de atalho
auto.press('x')

#Abre o Github

auto.write('github.com')
auto.press('enter')

#Abre o Class Room em uma nova guia

auto.hotkey('ctrl', 't')
auto.write('classroom.google.com')
auto.press('enter')

'''

Para criar um executável desse programa instalar cxFreeze 

'pip install cx_Freeze' #Primeiro passo instalar 
'cxfreeze main.py --target-dir nome-da-pasta' #Determinar a pasta que será criada e onde ficará alocado o executável

'''