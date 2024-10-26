import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import os

def creacion_df(archivo_html):
    archivo = archivo_html
    archivo_ = 'pagina_principal/'+archivo_html

    with open(f'pagina_principal/{archivo}', "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    soup = BeautifulSoup(contenido,'html.parser')

    tabla_precio = soup.find_all('div', {'class': 'Price-sc-12dh9kl-3 geYYII'})
    #tabla_expensas = soup.find_all('div', {'class': 'Expenses-sc-12dh9kl-1 iboaIF'})
    tabla_direccio = soup.find_all('div', {'class': 'LocationAddress-sc-ge2uzh-0 iylBOA postingAddress'})
    tabla_lugar = soup.find_all('h2', {'class': 'LocationLocation-sc-ge2uzh-2 fziprF'})
    tabla_caracteristicas = soup.find_all('h3', {'class': 'PostingMainFeaturesBlock-sc-1uhtbxc-0 cHDgeO'})

    #la siguiente linea de codigo es para verificar que todas las caracteristicas
    #tengan la misma longitud para iterar lo mismo sobre todas
    print(len(tabla_precio),len(tabla_direccio),len(tabla_lugar),len(tabla_caracteristicas))

    lista_b = []

    for i in range(len(tabla_precio)):
        lista_a = []  # Crear una nueva lista en cada iteración
        lista_a.append(tabla_precio[i].text)
        lista_a.append(tabla_direccio[i].text)
        lista_a.append(tabla_lugar[i].text)
    
    # Obtener todas las características para el índice 'i'
        caracteristicas = tabla_caracteristicas[i].find_all('span')
    
    # Iterar sobre las características y agregarlas a la lista
        for j in range(len(caracteristicas)):  # Usar len(caracteristicas) para evitar el fuera de rango
            lista_a.append(caracteristicas[j].text)
    
        lista_b.append(lista_a)

    caracteristicas = ['precio', 'direccion', 'lugar', 'm2 total', 'habientes', 'dormitorios', 'baños', 'cocheras']
    df = pd.DataFrame(lista_b, columns=caracteristicas)

    # se creara el archivo df
    df.to_csv('dataframes/pagina_scrapeada_1.csv', index=False)

    if os.path.exists(archivo_):
        os.remove(archivo_)
        print(f"El archivo {archivo_} fue eliminado.")
    else:
        print(f"El archivo {archivo_} no existe.")


creacion_df('pagina_scrapeada_1.html')

