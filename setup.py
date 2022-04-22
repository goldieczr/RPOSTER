import json
import pwinput
import pyfiglet
from time import sleep
from os import system, name
from selenium import webdriver, common
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

client_version = "1.0"
bot_name = "RPOSTER"

system(f'title {bot_name} {client_version}')

def setup():
    #Waits for the credentials of the account to be inputted, then opens browser
    USERNAME = input("[>] Username: ")
    PASSWORD = pwinput.pwinput(prompt="[>] Password: ", mask='*')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_position(-10000, 0)
    driver.set_window_size(800, 800)
    #Uses the credentials to log in
    driver.get(f'https://www.reddit.com/login')
    driver.find_element(By.ID,'loginUsername').send_keys(USERNAME)
    driver.find_element(By.ID,'loginPassword').send_keys(PASSWORD)
    driver.find_element(By.XPATH,'/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button').click()
    print(f"[!] Submitting credentials, please wait")
    sleep(5)
    try:
        #Error handling: invalid username or password
        error = driver.find_element(By.XPATH,'/html/body/div/main/div[1]/div/div[2]/form/fieldset[1]/div').text
        print(f"[!] {error}, retrying\n")
        driver.quit()
        setup()
    except common.exceptions.NoSuchElementException:
        #Saves the session cookie inside cookie.json
        print("[!] Successfully logged in, saving session cookie")
        cookie = driver.get_cookie("reddit_session")
        with open("cookie.json", "w") as f:
            json.dump(cookie, f)
        print("[!] Session cookie saved into text file, DO NOT SHARE IT")
    print("[!] Setup.py will exit in 5 seconds")
    sleep(5)

print(pyfiglet.figlet_format(f"{bot_name} {client_version}", font="slant"))
print ("[!] Setup initialized, input your Reddit login credentials")
setup()