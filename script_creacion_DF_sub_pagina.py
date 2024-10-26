import pandas as pd
from bs4 import BeautifulSoup
import os

def creacio_df_sub_pagina():

    ruta = 'sub_paginas/'

    archivos_html = [archivo for archivo in os.listdir(ruta) 
                    if os.path.isfile(os.path.join(ruta, archivo)) and archivo.endswith('.html')]

    caracteristicas = ['direccion',
                       'm2_total',
                       'm2_cubiertos',
                       'ambientes',
                       'banos',
                       'cocheras',
                       'dormitorios',
                       'toilettes',
                       'antiguedad',
                       'orientacion',
                       'luminosidad']

    df = pd.DataFrame(columns=caracteristicas)

    for i in archivos_html:
        archivo = ruta + i

        with open(archivo, "r", encoding="utf-8") as file:
            contenido = file.read()
            soup = BeautifulSoup(contenido, 'html.parser')

            # Inicializar el diccionario de propiedades para este archivo
            propiedades = {
                'direccion': None,
                'm2_total': None, 
                'm2_cubiertos': None, 
                'ambientes': None, 
                'banos': None, 
                'cocheras': None, 
                'dormitorios': None, 
                'toilettes': None, 
                'antiguedad': None, 
                'orientacion': None, 
                'luminosidad': None
            }

            # Obtener la dirección
            direccion_div = soup.find('div', {'class': 'section-location-property section-location-property-classified'})
            if direccion_div:
                direccion_h4 = direccion_div.find('h4')
                if direccion_h4:
                    propiedades['direccion'] = direccion_h4.text.strip()

            for li in soup.find_all("li", class_="icon-feature"):
                icon = li.find("i")["class"][0]  # Obtener la clase del ícono
                
                # Extraer texto relevante de cada `li`
                text = li.get_text(strip=True)
                
                # Condicionales según la clase del ícono para asignar al diccionario
                if icon == "icon-stotal":
                    try:
                        propiedades["m2_total"] = int(text.split()[0])
                    except ValueError:
                        propiedades["m2_total"] = None
                elif icon == "icon-scubierta":
                    try:
                        propiedades["m2_cubiertos"] = int(text.split()[0])
                    except ValueError:
                        propiedades["m2_cubiertos"] = None
                elif icon == "icon-ambiente":
                    try:
                        propiedades["ambientes"] = int(text.split()[0])
                    except ValueError:
                        propiedades["ambientes"] = None
                elif icon == "icon-bano":
                    try:
                        propiedades["banos"] = int(text.split()[0])
                    except ValueError:
                        propiedades["banos"] = None
                elif icon == "icon-cochera":
                    try:
                        propiedades["cocheras"] = int(text.split()[0])
                    except ValueError:
                        propiedades["cocheras"] = None
                elif icon == "icon-dormitorio":
                    try:
                        propiedades["dormitorios"] = int(text.split()[0])
                    except ValueError:
                        propiedades["dormitorios"] = None
                elif icon == "icon-toilete":
                    try:
                        propiedades["toilettes"] = int(text.split()[0])
                    except ValueError:
                        propiedades["toilettes"] = None
                elif icon == "icon-antiguedad":
                    try:
                        propiedades["antiguedad"] = int(text.split()[0])
                    except ValueError:
                        propiedades["antiguedad"] = None
                elif icon == "icon-orientacion":
                    propiedades["orientacion"] = text
                elif icon == "icon-luminosidad":
                    propiedades["luminosidad"] = text

        # Eliminar el archivo después de procesarlo
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"El archivo {archivo} fue eliminado.")
        else:
            print(f"El archivo {archivo} no existe.")

        # Agregar las propiedades extraídas al DataFrame
        df = pd.concat([df, pd.DataFrame([propiedades])], ignore_index=True)

    df.to_csv('dataframes/sub_paginas_screapedas.csv', index=False)

# Llamar a la función
creacio_df_sub_pagina()
