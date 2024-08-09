from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

ruta_html = os.path.abspath('../app/index.html')

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get(f'file:///{ruta_html}')

# Test 1, mostrar nombre

def test_ingresar_nombre():
    nombre_input = driver.find_element(By.ID, 'nombre')
    nombre_input.send_keys('Eduardo')

    boton_enviar = driver.find_element(By.ID, 'btnEnviar')
    boton_enviar.click()

    time.sleep(2)

    alert = driver.switch_to.alert
    assert 'Hola, Eduardo' in alert.text
    alert.accept()
    
    print("Caso 1 exitoso: El nombre se muestra correctamente en la ventana emergente.")

    # Test 2, campo vacío

def test_nombre_vacio():
    nombre_input = driver.find_element(By.ID, 'nombre')
    nombre_input.clear()

    boton_enviar = driver.find_element(By.ID, 'btnEnviar')
    boton_enviar.click()

    time.sleep(2)

    mensaje_error = driver.find_element(By.ID, 'mensajeError')
    assert 'Por favor, ingrese su nombre' in mensaje_error.text
    
    print("Caso 2 exitoso: El mensaje de error aparece cuando el campo esta vacio.")

# Ejecutar las pruebas
test_ingresar_nombre()
test_nombre_vacio()
# Cerrar el navegador
driver.quit()

