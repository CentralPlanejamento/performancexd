import time, pyautogui as py, winsound



time.sleep(1)
print('')
print('')
print('Posição')
print(f"{py.position().x} , {py.position().y}, ")
print('')
print('')
py.leftClick(py.position())
