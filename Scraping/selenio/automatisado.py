from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# URL de la página con la lista de títulos
url_lista = "https://www.lavoz.com.ar/busqueda/informatica/"

# Ruta al controlador de Chrome
chromedriver_path = 'D:\ispc\selenium\chromedriver.exe'

#ruta al controlador de Chrome en una variable de entorno
os.environ["webdriver.chrome.driver"] = chromedriver_path

# Inicializar el controlador de Chrome
driver = webdriver.Chrome()
# Abre la página con la lista de títulos
driver.get(url_lista)

# Encuentra los elementos que contienen los títulos
titulos = driver.find_elements(By.XPATH, "//h2[@class='article-title']")

# Itera a través de los títulos y haz clic en cada uno
for titulo in titulos:
        try:
            
    # Intenta hacer clic en el elemento
            #print(titulo.text)
            titulo.click()
            driver.implicitly_wait(5)
            driver.back()
        except StaleElementReferenceException:
    # El elemento se ha vuelto rancio, realiza alguna acción como recargar la página
            driver.refresh()
    # Intenta nuevamente hacer clic en el elemento
            titulo = driver.find_element(By.XPATH, "//h2[@class='article-title']")
            titulo.click()

# Cierra el navegador al final
driver.quit()