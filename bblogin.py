import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib3 as ul3
from pyfiglet import Figlet

gr = Figlet(font= 'graffiti')
print(gr.renderText('zWR417H'))
print("\n 					  [Auto BB-Login Script v1.0]")
print("\n")



def con_chck():
    r = requests.get('https://www.google.com', timeout = 10)
    return True
        


if con_chck() == True:

	print("\n[+]Internet Connection Found...!\n")

	uk = b'\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00c\x00u\x00c\x00h\x00d\x00.\x00b\x00l\x00a\x00c\x00k\x00b\x00o\x00a\x00r\x00d\x00.\x00c\x00o\x00m\x00/\x00'

	browser = webdriver.Chrome('drivers\chromedriver.exe')
	fk = uk
	"""
	If you need to Open Time Table Along with Login then remove this comment 
	browser.get(('file:/// Your Time table pdf File Path'))
	browser.execute_script("window.open('about:blank', 'tab2');")
	browser.switch_to.window("tab2")
	"""
	browser.get((fk.decode('utf-16', 'strict')))
	username = Your Encrypted User Name Here 			# Fill these details Carefully.
	passwd = Your Encrypted Password Here

	cookiy = browser.find_element_by_id('agree_button')
	cookiy.click()

	browser.find_element_by_id('user_id').send_keys(username.decode('utf-16', 'strict'))
	browser.find_element_by_id('password').send_keys(passwd.decode('utf-16', 'strict'))

	signInButton = browser.find_element_by_id('entry-login')
	signInButton.click()

	print("\n\n[!]Don't Close this Command Prompt\n")

	exit()
else:
	print(err)
