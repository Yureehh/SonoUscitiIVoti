from selenium import webdriver
from bs4 import BeautifulSoup
import Email
import time
import os
from dotenv import load_dotenv


#This is needed if i want to use Brave but is to bugfix
# browser_path = "C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\chromedriver.exe"
# brave_path = "C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\\brave.exe"

# option = webdriver.ChromeOptions()
# option.binary_location = brave_path
# # option.add_argument("--incognito") OPTIONAL
# # option.add_argument("--headless") OPTIONAL

# # Create new Instance of Chrome
# browser = webdriver.Chrome(executable_path=browser_path, options=option)
load_dotenv()
esame_old = None
esame = None
mymail = os.environ.get('Email_Uni')
password =  os.environ.get('Unicorni')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--headless')       #il browser non appare
chrome_options.add_argument('--disable-gpu')    #toglie un errore strano
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging']) #toglie un altro errore strano

while True:

    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://studenti.unibo.it/sol/welcome.htm")

    #Primo link verso studenti online
    prelogin_button = browser.find_element_by_xpath('//a[@href="'+"studenti/home.htm"+'"]')
    # Click login
    prelogin_button.click()

    #Link credenziali
    credenziali_button = browser.find_element_by_class_name("largeTextNoWrap")
    # Click login
    credenziali_button.click()

    # Select the id box
    id_box = browser.find_element_by_name('UserName')
    # Send id information
    id_box.send_keys(mymail)
    # Find password box
    pass_box = browser.find_element_by_name('Password')
    # Send password
    pass_box.send_keys(password)
    time.sleep(1)
    # Find login button
    login_button = browser.find_element_by_id('submitButton')
    # Click login
    login_button.click()

    # Find and click on almaesami
    courses_button = browser.find_element_by_xpath('//a[@href="'+"https://almaesami.unibo.it/almaesami/studenti/home.htm"+'"]')
    courses_button.click()

    #Link credenziali 2
    credenziali_button2 = browser.find_element_by_class_name("largeTextNoWrap")
    # Click login 2
    credenziali_button2.click()

    #Ora siam dentro alla pagina di almaesami, devo ricavare calcolo
    page_source = browser.page_source
    soup = BeautifulSoup(page_source, "lxml")

    # Cerca l'esame in questione
    esame_old = esame
    esame = soup.find_all('a', href="/almaesami/studenti/attivitaFormativaPiano-list.htm?execution=e1s1&_eventId=prenota&idx=8")

    print(esame_old)
    print(esame,"\n")
    if esame_old != esame and esame_old != None:
        print("email inviata")
        Email.send_mail()
        break

    print("Niente voti")
    time.sleep(300)
    browser.quit()