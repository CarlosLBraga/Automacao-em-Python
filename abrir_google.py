import pyautogui as abrir_google


abrir_google.sleep(2)
print(abrir_google.position())

abrir_google.moveTo(x=611, y=754)
abrir_google.doubleClick(x=611, y=754)

abrir_google.sleep(2)


abrir_google.hotkey("win", "up")

abrir_google.sleep(1)
abrir_google.typewrite('https://www.google.com/')
abrir_google.sleep(1)
abrir_google.press('enter')


abrir_google.sleep(1)
abrir_google.typewrite('g1')
abrir_google.press('enter')

abrir_google.sleep(3)
abrir_google.click(x=384, y=305)

abrir_google.sleep(2)
abrir_google.hscroll(-300)

for i in range (8):
    abrir_google.sleep(3)
    abrir_google.hscroll(-500)
