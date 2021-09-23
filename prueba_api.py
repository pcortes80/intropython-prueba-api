# API key
# RFi8nBGz3YPhwLfqZ1CAsx0FrIaYuIpMUm2xlsM6

# Prueba - API
# Patricio Cortés
# G18
# 22-09-2021

# importa librerias necesarias
import requests
import json

# crea funcion que llama una url con una determinada accion
# funcion creada en Desafio - API
def llamar_api(url, accion):
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': 'RFi8nBGz3YPhwLfqZ1CAsx0FrIaYuIpMUm2xlsM6'
        }
    payload = {}
    # obtiene respuesta del servidor
    respuesta = requests.request(accion, url, data=payload, headers = headers)
    print("Acción: {}\nCódigo: {}".format(accion,respuesta))
    return json.loads(respuesta.text)

# *** Requerimiento 1 ***
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?"
print("Requerimiento 1:")

# llama a la funcion definida con solo 25 resultados
response = llamar_api(url, "GET")

# define una lista de solo 25 resultados
lista_25_fotos = response["latest_photos"][0:25]
#print(lista_25_fotos)

# *** Requerimiento 2 ***

# iteramos la lista de 25 resultados
lista_url = []
for i in lista_25_fotos:
    # print(i["img_src"])
    lista_url.append(i["img_src"])
print("Lista de url de las 25 fotos encontradas = ",lista_url)
print("La lista tiene un largo de {} url.".format(len(lista_25_fotos)))

# *** Requerimiento 3 ***

# define la funcion
def build_web_page(list_url):
    html = "<html><head></head><body><ul>\n"
    for i in list_url:
        html += "<li><img src=\"{}\"></li>\n".format(i)
    html += "</ul></body></head></html>"
    
    with open("output.html", "w") as f:
        f.write(html)

# llama a la funcion builds_web_page
build_web_page(lista_url)

# Fin del Programa