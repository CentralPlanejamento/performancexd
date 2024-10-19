import os
import time
from PIL import ImageGrab
import pyautogui as py
from pywinauto import Desktop
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Robo:
    def __init__(self):
        self.nome_salvar_print = 'alterar'
        self.extensao_salvar_print = '.PNG'
        self.pasta = r"C:\Users\Robô 01\Desktop\streamlib.app"



class NetlifyAutomation:
    def __init__(self):
        profile_path = r"C:\Users\Robô 01\AppData\Local\Google\Chrome\User Data\Profile 3"
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={os.path.dirname(profile_path)}")
        options.add_argument(f"profile-directory={os.path.basename(profile_path)}")
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)

    def aguardar_elemento_visivel(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def aguardar_elemento_clicavel(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def executar_github(self):
        url = "https://github.com/CentralPlanejamento/performancexd"
        self.driver.get(url)
        
        # Localizando e clicando no botão "Add file"
        try:
            elemento = self.aguardar_elemento_clicavel(By.CSS_SELECTOR, "#\\:R5b5ab\\: > span.Box-sc-g0xbh4-0.gUkoLg > span")
            elemento.click()


            # Localizando o link "Upload files" e clicando
            elemento = self.aguardar_elemento_clicavel(By.CSS_SELECTOR, "a[role='menuitem'][href='/CentralPlanejamento/performancexd/upload/main']")
            elemento.click()

            time.sleep(3)
   
            py.click(665 , 516)
            time.sleep(6)
            py.click(570 , 385)
            py.hotkey('ctrl', 'a')
            py.press('enter')
            time.sleep(10)
            
            
            # Localizando e clicando no botão "Commit changes"
            commit_button = self.aguardar_elemento_clicavel(By.XPATH, "//button[@data-edit-text='Commit changes']")
            commit_button.click()

            time.sleep(5)

        except Exception as e:
            print(f"Erro ao executar ações no GitHub: {e}")
            
            
    def fechar_driver(self):
        self.driver.quit()
        print("Navegador fechado.")

if __name__ == "__main__":
    robo = Robo()
    
    try:
        while True:
            print(f'Início loop: {time.strftime("%Y-%m-%d %H:%M:%S")}')
            try:
                # Inicia a automação do GitHub após as tarefas do Robo
                automation = NetlifyAutomation()
                automation.executar_github()  # Chama o método correto
                
                # Fecha o navegador após a execução
                automation.fechar_driver()
                
            except Exception as e:
                print(f"Erro durante a execução do loop do Robo: {e}")

            # Pause para evitar loops rápidos
            time.sleep(5)

    except KeyboardInterrupt:
        print("Execução interrompida pelo usuário.")    
