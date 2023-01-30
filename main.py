from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

CHROME_DRIVER_PATH = 'C:\Development\chromedriver.exe'
LOGIN = "your login here"
PASSWORD = "your password here"
SIMMILAR_ACCOUNT = "therock"
URL = "https://www.instagram.com/"


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(service=Service(path))

    def login(self):
        self.driver.get(url=URL)
        self.driver.maximize_window()
        sleep(2)
        accept_button = self.driver.find_element(By.CLASS_NAME, '_a9_1')
        accept_button.click()
        sleep(2)
        email = self.driver.find_element(By.NAME, "username")
        email.send_keys(LOGIN)
        sleep(1)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        sleep(1)
        log_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        log_button.click()
        sleep(10)

    def find_followers(self):
        self.driver.get(url=URL + SIMMILAR_ACCOUNT)
        sleep(10)
        followers_button = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[3]/a')
        followers_button.click()

        sleep(10)
        modal = self.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        sleep(2)
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, '._aano button')
        print(len(follow_buttons))
        for follow in follow_buttons:
            try:
                follow.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,
                                                         '/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
                cancel_button.click()
                follow.click()
            sleep(2)
        self.driver.quit()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
