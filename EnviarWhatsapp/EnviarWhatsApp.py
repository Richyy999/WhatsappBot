from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

# se debe tener instalado selenium
# si no, introduce esto en la terminal: pip install selenium

# to chromedriver in your computer
driver = webdriver.Chrome("../chromedriver.exe")

# abrir whstsapp web
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Nombre del contacto o grupo
target = input("Introduce el nombre del contacto o grupo: ")

# para seleccionar el contacto o grupo
x_arg = '//span[@title = "{}"]'.format(target)

group_title = driver.find_element_by_xpath(x_arg) 
group_title.click()

# mensaje a enviar
string = input("Introduce el mensaje: ")

# seleccionar el campo de texto
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = driver.find_element_by_xpath(inp_xpath)

# número de veces que se envía le mensaje
numVeces = int(input("Introduce el número de veces que se repetirá el mensaje: "))

for i in range(numVeces):
    # introduce el mensaje en el campo de texto
    input_box.send_keys(string)
    # pulsa enter y envía el mensaje
    input_box.send_keys(Keys.ENTER)
    # esperar antes de enviar el siguiente mensaje
    sleep(1)
    
driver.close()
