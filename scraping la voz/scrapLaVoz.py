import os
import json
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import StaleElementReferenceException
import time

# Obtiene la ubicación actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))

# URL de la página con la lista de títulos
url_lista = "https://www.lavoz.com.ar/busqueda/ciudadanos/"

# Ruta al controlador de Chrome (ajusta la ruta según tu sistema)
chromedriver_path = "C:\Programacion\scrapy\chromedriver.exe"

# Ruta a los archivos JSON y CSV
json_file_name = os.path.join(current_dir, "article_data.json")
csv_file_name = os.path.join(current_dir, "article_data.csv")

# Inicializa el controlador de Chrome
os.environ["webdriver.chrome.driver"] = chromedriver_path
driver = webdriver.Chrome()

# Abre la página con la lista de títulos
driver.get(url_lista)

# Encuentra los elementos que contienen los títulos
titulos = driver.find_elements(By.XPATH, "//h2[@class='article-title']//a")

# Abre los archivos JSON y CSV antes del bucle
with open(json_file_name, "w", encoding="utf-8") as json_file, open(csv_file_name, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)

    # Escribe una fila de encabezado en el archivo CSV
    csv_writer.writerow(["Título", "Contenido", "Fecha de Publicación"])

    # Itera a través de los títulos
    for i in range(len(titulos)):
        try:
            titulo = titulos[i]
            print(titulo.text)
            titulo.click()
            time.sleep(2)
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

            # Crear un diccionario con los datos
            article_data = {
                "Título": article_title,
                "Contenido": article_content,
                "Fecha de Publicación": article_date
            }

            # Guardar los datos en un archivo JSON
            json.dump(article_data, json_file, ensure_ascii=False, indent=4)
            json_file.write('\n')  # Agrega un salto de línea

            # Guardar los datos en un archivo CSV
            csv_writer.writerow([article_title, article_content, article_date])

            driver.back()

        except StaleElementReferenceException:
            driver.refresh()
            titulos = driver.find_elements(By.XPATH, "//h2[@class='article-title']//a")

# Cierra el navegador al final
driver.quit()