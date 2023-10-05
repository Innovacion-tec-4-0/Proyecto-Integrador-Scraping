import requests
import csv
import json
import os
#-----------------------------------------------------------------------------------
# Configura las credenciales de tu aplicación
client_id = '27327'
client_secret = 'cSMFZIp1UHJZuHwCM)i)CQ(('
base_url = 'https://api.stackexchange.com/2.2'

# Realiza una solicitud para obtener las 10 preguntas más recientes en Stack Overflow
params = {
    'site': 'stackoverflow',
    'order': 'desc',
    'sort': 'creation',
    'pagesize': 10
}

response = requests.get(f'{base_url}/questions', params=params)
data = response.json()

#-----------------------------------------------------------------------------------
# Obtén el directorio actual del script
current_directory = os.path.dirname(__file__)


# Rutas de los archivos CSV y JSON en el mismo directorio que el script
csv_filename = os.path.join(current_directory, 'preguntas_stackoverflow.csv')
json_filename = os.path.join(current_directory, 'preguntas_stackoverflow.json')

# Guardar datos en un archivo CSV
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Escribir encabezados
    csv_writer.writerow(['Título', 'Enlace'])
    # Escribir datos
    for item in data['items']:
        csv_writer.writerow([item['title'], item['link']])

print(f'Datos guardados en {csv_filename}')

# Guardar datos en un archivo JSON
with open(json_filename, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)

print(f'Datos guardados en {json_filename}')

#-----------------------------------------------------------------------------------
# Imprime los títulos de las preguntas
for item in data['items']:
    print(item['title'])