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

	browser = webdriver.Chrome()
	fk = uk
	browser.get(('file:///C:/Users/Prince/Downloads/rptStudentTimeTable.pdf'))
	browser.execute_script("window.open('about:blank', 'tab2');")
	browser.switch_to.window("tab2")
	browser.get((fk.decode('utf-16', 'strict')))
	username = b'\xff\xfe2\x000\x00B\x00C\x00S\x004\x009\x005\x003\x00'
	passwd = b'\xff\xfeP\x00r\x00i\x00n\x00c\x00e\x00U\x00i\x00m\x00s\x00@\x008\x009\x000\x007\x00'

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