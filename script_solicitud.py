from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import script_tiempo


def solicitud(urls):

    chrome_options = Options()
    service = Service('C:\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    a = 0

    for i in urls:
        a = a + 1 
        driver.get(i)
        script_tiempo.tiempo_espera()

        try:
            aceptar_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Acepto']"))
            )
            aceptar_btn.click()
            print("Se aceptaron las cookies automáticamente.")

        except Exception as e:
            print("No se encontró el botón de cookies o algo falló:", e)

        html = driver.page_source

        with open(f'pagina_principal/pagina_scrapeada_{a}.html', 'w', encoding='utf-8') as file:
            file.write(html)

        print(f"HTML guardado correctamente en 'pagina_scrapeada_{i}.html'")

    listado_publicaciones = driver.find_elements(By.CSS_SELECTOR, '[data-qa*="posting PROPERTY"]')

    url_posting = []

    for i in listado_publicaciones:

        url_posting.append(i.get_attribute('data-to-posting'))

    b = 0

    for j in url_posting:

        b = b + 1

        url_ = 'https://www.zonaprop.com.ar' + j

        chrome_options = Options()
        service = Service('C:\chromedriver-win64\chromedriver-win64\chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=chrome_options)

        script_tiempo.tiempo_espera()

        driver.get(url_)

        script_tiempo.tiempo_espera()

        try:
            aceptar_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Acepto']"))
                )
            script_tiempo.tiempo_espera()
            aceptar_btn.click()
            print("Se aceptaron las cookies automáticamente.")

        except Exception as e:
            print("No se encontró el botón de cookies o algo falló:", e)

        html__ = driver.page_source

        with open(f'sub_paginas/sub_pagina_scrapeada_{b}.html', 'w', encoding='utf-8') as file:
                file.write(html__)

        print(f"HTML guardado correctamente en 'sub_pagina_scrapeada{b}.html'")

    driver.quit()
    









lista = ['https://www.zonaprop.com.ar/inmuebles-venta-san-justo-la-matanza.html']

solicitud(lista)