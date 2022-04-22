import json
import random
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

def startup():
    #Opens post.txt and saves your title & link
    a = open("post.txt", "r")
    global title
    global link
    title = a.readline().strip()
    link = a.readline().strip()
    print(f"[!] Title: '{title}'")
    print(f"[!] Link: '{link}'")
    runbot()

def runbot():
    #Starts up the browser without showing
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(800, 800)
    driver.set_window_position(-10000, 0)
    driver.get(f'https://www.reddit.com/')
    #Loads the session cookie
    with open("cookie.json") as f:
        cookie = json.load(f)
    driver.add_cookie(cookie)
    print(f"[!] Loaded the session cookie")
    #Opens the list of subreddits and starts iterating through lines
    a = open("subreddits.txt", "r")
    for subreddit in a:
        driver.get(f'https://www.reddit.com/r/{subreddit}/submit')
        sleep(3)
        #Clicks on 'LINK' button
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[1]/div/button[3]").click()
        #Pastes title
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/div/textarea").send_keys(title)
        #Pastes link
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[2]/textarea").send_keys(link)
        #Submits post
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[2]/div/div[1]/button").click()
        #Waits 3 seconds, then displays the URL of the post
        sleep(3)
        post_url = driver.current_url
        print(f"[!] Successfully posted, URL: {post_url}")
        #Random delay between 20 and 40 seconds
        delay = random.randint(20, 40)
        print (f"[!] Waiting {delay} before submitting to the next subreddit")
        sleep(delay)

print(pyfiglet.figlet_format(f"{bot_name} {client_version}", font="slant"))
print(f"[!] {bot_name} is starting.")
startup()