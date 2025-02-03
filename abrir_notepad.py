import pyautogui as abrir_arquivo
import pygetwindow as gw


abrir_arquivo.hotkey('win', 'r') #windows + r

abrir_arquivo.sleep(3)
print(abrir_arquivo.position())

abrir_arquivo.typewrite('notepad')
abrir_arquivo.press('enter')
abrir_arquivo.sleep(2)
abrir_arquivo.hotkey('win', 'up')
abrir_arquivo.typewrite('Desenvolver e muito legal')

janela = gw.getActiveWindow()
janela.close()

abrir_arquivo.sleep(2)
abrir_arquivo.press('right')
abrir_arquivo.sleep(1)
abrir_arquivo.press('enter')
