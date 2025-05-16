from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicializa o navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Abrir o plano de login e senha
driver.get('https://app.stage.rentzapp.com.br/auth/login')

##
#campo_email = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
#campo_email.send_keys("seu_email@teste.com")


#preenche login com email ou username
campo_email = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
campo_email.send_keys("imob.grupomatriarca@gmail.com")

#preenche password
campo_senha = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
campo_senha.send_keys("XHJrIuI=")
                                                
#Clica no botton de login
driver.find_element(By.ID, "submit").click()

#tempo de carregamento para retorno
time.sleep(3)

#fecha navegador
