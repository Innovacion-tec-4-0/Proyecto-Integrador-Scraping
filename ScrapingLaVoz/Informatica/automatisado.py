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
chromedriver_path = 'C:\SCRAPI\chromedriver.exe'

#ruta al controlador de Chrome en una variable de entorno
os.environ["webdriver.chrome.driver"] = chromedriver_path

# Inicializar el controlador de Chrome
driver = webdriver.Chrome()
# Abre la página con la lista de títulos
driver.get(url_lista)

# Encuentra los elementos que contienen los títulos
titulos = driver.find_elements(By.XPATH, "//h2[@class='article-title']")

# Imprimir los primeros 4 títulos de la lista
for i in range(4):
    try:
        titulo = titulos[i]
        print(titulo.text)
        titulo.click()
        driver.implicitly_wait(5)
        page_content = driver.page_source
        
    # Analiza el contenido con BeautifulSoup
        soup = BeautifulSoup(page_content, "html.parser")
    
    # Extrae el título
        article_title = soup.find("h1", {"class": "false h1 boldbold mb1 col-12 lg-col-9 md-col-8"}).text.strip()
    
    # Extrae el contenido (puede variar según la estructura de la página)
        article_content = soup.find("div", {"class": "story-content px2"}).text.strip()
    
    # Extrae la fecha de publicación (puede variar según la estructura de la página)
        article_date = soup.find("p", {"class": "date primary-color"}).text.strip()
    
    # Imprime los resultados
        print("Título:", article_title)
        print("Contenido:", article_content)
        print("Fecha de Publicación:", article_date)
        print()
        print()
        driver.back()

    except StaleElementReferenceException:
        driver.refresh()
        titulo = driver.find_elements(By.XPATH, "//h2[@class='article-title']")[i]
        titulo.click()



# Cierra el navegador al final
driver.quit()