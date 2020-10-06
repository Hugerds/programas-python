import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

PROXY = 'XXX.XX.XXX:XXXX' #Insira proxys aqui.

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={PROXY}')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get('https:myip.com')
time.sleep(100)