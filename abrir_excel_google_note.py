import pyautogui as escolha
import pyautogui

opcao = pyautogui.confirm('Escolha uma opção', buttons = ['Excel', 'Google', 'Notepad'])


if opcao == 'Excel':
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('Excel')
    pyautogui.press('enter')


elif opcao == 'Notepad':
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('notepad')
    pyautogui.press('enter')
    pyautogui.sleep(2)
    pyautogui.hotkey('win', 'up')


else:
    pyautogui.hotkey('win','r')
    pyautogui.typewrite('https://www.google.com.br/')
    pyautogui.press('enter')
    pyautogui.sleep(2)
    pyautogui.hotkey('win', 'up')