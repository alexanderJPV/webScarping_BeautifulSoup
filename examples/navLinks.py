#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 21:17:26 2020

@author: alexander
"""


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instancia el driver
with webdriver.Chrome() as driver:

    # Abre la URL
    driver.get("https://seleniumhq.github.io")

    # Configura una espera para despues
    wait = WebDriverWait(driver, 100)

    # Almacena el ID de la ventana original
    original_window = driver.current_window_handle

    # Comprueba que no existen otras ventanas abiertas previamente
    assert len(driver.window_handles) == 1

    # Haz clic en el enlace el cual abre una nueva ventana
    driver.find_element(By.LINK_TEXT, "new window").click()

    # Espera a la nueva ventana o pestaña
    wait.until(EC.number_of_windows_to_be(2))

    # # Recorrelas hasta encontrar el controlador de la nueva ventana
    # for window_handle in driver.window_handles:
    #     if window_handle != original_window:
    #         driver.switch_to.window(window_handle)
    #         break

    # # Espera a que la nueva ventana carge su contenido
    # wait.until(EC.title_is("SeleniumHQ Browser Automation"))