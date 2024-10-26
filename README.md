# Web Scraping Zona Prop
V 0.5

## Objetivo

Estos scripts están creados con la finalidad de hacer dataframes con información inmobiliaria de la zona de La Matanza, GBA. Mi objetivo, después de crear el dataset, es hacer un análisis sobre el mercado inmobiliario en dicha zona.

Este script toma de ZonaProp algunos datos como:

 - La dirección (que será una especie de ID para enlazar varias tablas, como se muestra en el ejemplo de Power BI).
 - La zona.
 -  Los m² de la propiedad.
 - Los m² cubiertos.
 - Cantidad de habitaciones.
 - Cocheras.
 - Baños.
 - Toilette.
 - Entre otros.

## El orden de ejecución sería el siguiente:

script_solicitud ↓

script_creacion_DF ↓

script_creacion_DF_sub_pagina

De esta manera se obtienen dos dataframes con la información general que dan en la página después de darle a "buscar" dentro de ZonaProp. Además, se obtienen algunas características más de forma individual en cada oferta.

** Observaciones**
 - Solo se probó con una página (*).
 - Cuando se manipulan los archivos con la librería OS, no se verifica si los archivos ya existen para crear nuevos en consecuencia (*).
 - Falta documentación dentro del código (*).
 - No se recolectó información sobre los departamentos en las pruebas unitarias y en la primera prueba.
 - No se recolectó información sobre las expensas.
  
## Ideas
 - aplicar un algoritmo de  regresion lineal con toda la informacion que se recolecte
 - aplicar un algoritmo de KNN
 - Conectarme a la API del BCRA con el fin de extraer el precio del dólar y representar el valor de las viviendas en pesos argentinos, además de que se actualice automáticamente al aumentar el precio del dólar.
 - Intentar encontrar un mapa vectorizado de La Matanza y agregarlo a Power BI para que el análisis sea más profundo.
 - Encontrar información como:
 - Avenidas importantes.
 - Rutas.
 - Shoppings.
 - Autopistas.
 - cercanía a zonas céntricas.
 - Contabilizar la cantidad de fábricas.
 - Universidades.
 - Escuelas.
 - Habitantes por km².
 - Accesibilidad a los servicios básicos.
 - Cercanía a transportes públicos.
 - Para ver si todo esto afecta al precio final de las viviendas.
