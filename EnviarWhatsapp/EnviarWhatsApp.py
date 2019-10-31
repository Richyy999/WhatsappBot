from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome("../chromedriver.exe")

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = input("Introduce el nombre del contacto o grupo: ")

# Replace the below string with your own message
string = input("Introduce el mensaje: ")

numVeces = int(input("Introduce el número de veces que se repetirá el mensaje: "))

x_arg = '//span[@title = "{}"]'.format(target)

group_title = driver.find_element_by_xpath(x_arg) 
group_title.click()

inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = driver.find_element_by_xpath(inp_xpath)

for i in range(numVeces):
    input_box.send_keys(string)
    input_box.send_keys(Keys.ENTER)
    sleep(1)
    
driver.close()
