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

    def capturar_imagem(self, left, top, right, bottom, nome_arquivo):
        try:
            imagem = ImageGrab.grab(bbox=(left, top, right, bottom))
            caminho_saida = os.path.join(self.pasta, nome_arquivo + self.extensao_salvar_print)
            imagem.save(caminho_saida)  
            print(f"Imagem salva: {caminho_saida}")
        except Exception as e:
            print(f"Erro ao capturar imagem: {e}")

    def encontrar_e_ativar_aba(self, titulo_aba):
        app = Desktop(backend="uia")
        while True:
            try:
                abas = app.windows()
                abas_filtradas = [aba for aba in abas if titulo_aba.lower() in aba.window_text().lower()]
                if abas_filtradas:
                    aba = abas_filtradas[0]
                    aba.set_focus()
                    aba.maximize()
                    print(f"Aba encontrada e ativada: {aba.window_text()}")
                    return
                else:
                    print(f"Tentando encontrar a aba '{titulo_aba}'...")
                    time.sleep(2)
            except Exception as e:
                print(f"Erro ao tentar encontrar a aba: {e}")
                time.sleep(2)

    def tracking(self):
        self.encontrar_e_ativar_aba("Tracking_Deposito")
        left, top, right, bottom = 45, 120, 580, 650
        self.capturar_imagem(left, top, right, bottom, 'Tracking')

        aba_tracking1 = (122, 687)
        py.click(aba_tracking1)
        py.click(687, 217)
        time.sleep(150)
        py.hotkey('ctrl', 'b')
        time.sleep(4)

        self.encontrar_e_ativar_aba("BI_V2_produtividade")

    def db_Performance(self):
        try:
            py.click(485, 80)
            time.sleep(40)
            py.click(873, 515)
            time.sleep(1)

            abas = {
                'Produtividade': (198 , 684),
                'Recebimento': (340 , 678),
                'Consolidacao': (447 , 676),
                'Inbound': (548 , 674),
                'Greenzone': (638 , 677),
                'Outbound': (729 , 684)
            }

            for nome, coordenadas in abas.items():
                self.nome_salvar_print = nome
                py.click(coordenadas)
                time.sleep(3)
                py.moveTo(0, 370)
                time.sleep(2)
                self.capturar_imagem(25, 120, 1185, 650, nome)
                print(f'"Print {nome}" finalizado.')
        except Exception as e:
            print(f"Erro ao capturar desempenho do banco: {e}")


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

        time.sleep(8)
        
        # Localizando e clicando no botão "Add file"
        try:
            elemento = self.aguardar_elemento_clicavel(By.CSS_SELECTOR, "#\\:R5b5ab\\: > span.Box-sc-g0xbh4-0.gUkoLg > span")
            elemento.click()

            time.sleep(4)
            
            # Localizando o link "Upload files" e clicando
            elemento = self.aguardar_elemento_clicavel(By.CSS_SELECTOR, "a[role='menuitem'][href='/CentralPlanejamento/performancexd/upload/main']")
            elemento.click()

            time.sleep(3)
            
            py.click(665 , 516)
            time.sleep(4)
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
                # Descomente as funções que deseja executar
                robo.tracking()
                robo.db_Performance()
                
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
