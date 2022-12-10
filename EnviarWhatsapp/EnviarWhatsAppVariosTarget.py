from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

# se debe tener instalado selenium
# si no, introduce esto en la terminal: pip install selenium

# to chromedriver in your computer
driver = webdriver.Chrome("chromedriver.exe")

# abrir whstsapp web
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 25)

# Nombre del contacto o grupo
target = ["Chechu", "Maria Cate", "Alicia"]
# contacto = ""
# while contacto != "fin":
#     contacto = input("Introduce el nombre del contacto o grupo: ")
#     if contacto != "fin":
#         target.append(contacto)

# mensaje a enviar
# string = input("Introduce el mensaje: ")

mensaje = "¡¡¡¡Feliz Año Nuevo!!!!"

#número de veces que se va a repetir el mensaje
# numVeces = int(input("Introduce el número de veces que se repetir el mensaje: "))
numVeces = 1

input("Pulsa enter")

# para seleccionar el contacto o grupo
for i in target:
    x_arg = '//span[@title = "{}"]'.format(i)
    group_title = driver.find_element_by_xpath(x_arg) 
    group_title.click()
    for i in range(numVeces):
        # seleccionar el campo de texto
        inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div'
        input_box = driver.find_element_by_xpath(inp_xpath)
        # introduce el mensaje en el campo de texto
        input_box.send_keys(mensaje)
        # pulsa enter y envía el mensaje
        sleep(2)
        input_box.send_keys(Keys.ENTER)
        # esperar antes de enviar el siguiente mensaje
        sleep(2)
    
driver.close()
