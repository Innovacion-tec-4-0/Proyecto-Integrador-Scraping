import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import csv

# Obtener la ruta del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

URL = "https://stackoverflow.com/questions"


# Leer HTML de la página
response = urlopen(URL)
html = response.read()

# Analizar HTML con BeautifulSoup
soup = BeautifulSoup(html, features="lxml")

# Encontrar preguntas en etiquetas 'h3' con la clase 's-post-summary--content-title'
qlist = soup.find_all("h3", class_="s-post-summary--content-title")

titles = []
data_for_json = []

for q in qlist:
    title = q.text.strip()  # Eliminar espacios en blanco alrededor del título
    titles.append(title)
    data_for_json.append({"title": title})
    print (q.text)
    
# Ruta completa para guardar los archivos en la misma ubicación del script
json_file_path = os.path.join(script_dir, "stack_overflow_titles.json")
csv_file_path = os.path.join(script_dir, "stack_overflow_titles.csv")

# Guardar los datos en un archivo JSON
with open(json_file_path, "w") as json_file:
    json.dump(data_for_json, json_file, indent=4)

# Guardar los datos en un archivo CSV
with open(csv_file_path, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Title"])  # Escribir la cabecera del CSV
    for title in titles:
        writer.writerow([title])

print(f"Archivos guardados en: {script_dir}")
