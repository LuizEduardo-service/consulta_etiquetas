from time import sleep
from idna import valid_contextj
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as condicaoEsperada
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from tkinter import messagebox


class ConsultaEtiqueta:
    
    def __init__(self,  usuario, senha) -> None:
        self.usuario = usuario
        self.senha = senha
        self.url ='https://viavarejo.custhelp.com/AgentWeb/ '
        

    def start(self):
        self.inicia_browser()
        if self.login_usuario():
            ...
        else:
            return False

        return True


    def inicia_browser(self):
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager().install()) 
            self.wait = WebDriverWait(self.driver,10)
            self.driver.get(self.url)
            sleep(5)
        except:
            messagebox.showerror('Error','Não foi possivel abrir a pagina web.')

    def login_usuario(self):
        
        self._txt_usuario = self.driver.find_element(By.ID,'username')
        self._txt_senha = self.driver.find_element(By.ID,'password')
        self._btn_conectar = self.driver.find_element(By.ID,'loginbutton')

        self._txt_usuario.send_keys(self.usuario)
        sleep(2)
        self._txt_senha.send_keys(self.senha)
        sleep(2)

        self._btn_conectar.click()

        if self.valida_elemento(By.ID, 'wrongcred'):
            self._msg_erro = self.driver.find_element(By.ID,'wrongcred')
            messagebox.showerror('Error',self._msg_erro.text)
            self.driver.quit()
            return False
        
        return True


    def valida_elemento(self,tipo, path):
        try: self.driver.find_element(by=tipo,value=path)
        except NoSuchElementException as e: return False
        return True

if __name__ == '__main__':
    consulta = ConsultaEtiqueta('2903896595', 'liz...1504')
    consulta.start()