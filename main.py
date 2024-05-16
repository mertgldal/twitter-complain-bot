import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 150
TWITTER_EMAIL = os.getenv('twitter_id')
TWITTER_PASSWORD = os.getenv('twitter_password')


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go_button = self.driver.find_element(By.CLASS_NAME, value='start-text')
        go_button.click()
        time.sleep(45)
        try:
            self.down = self.driver.find_element(
                By.XPATH,
                value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]'
                      '/div[1]/div[1]/div/div[2]/span'
            ).text
            self.up = self.driver.find_element(
                By.XPATH,
                value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]'
                      '/div[1]/div[2]/div/div[2]/span'
            ).text
        except NoSuchElementException:
            print('No such element in Speedtest page.')

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(5)
        try:
            email = self.driver.find_element(
                By.XPATH,
                value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/'
                      'div[5]/label/div/div[2]/div/input'
            )
            email.send_keys(TWITTER_EMAIL)
            email.send_keys(Keys.ENTER)
            time.sleep(2)
            password = self.driver.find_element(
                By.XPATH,
                value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/'
                      'div[3]/div/label/div/div[2]/div[1]/input'
            )
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)
            time.sleep(10)
            if float(self.up) < PROMISED_UP or float(self.down) < PROMISED_DOWN:
                message = (f'Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for'
                           f' {PROMISED_DOWN}down/{PROMISED_UP}? Hanınyaaaa?!?!!?')
                post_text = self.driver.find_element(
                    By.XPATH,
                    value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/'
                          'div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/'
                          'div/div[2]/div/div/div/div'
                )
                post_text.send_keys(message)
                post_button = self.driver.find_element(
                    By.XPATH,
                    value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/'
                          'div/div/div[2]/div[2]/div[2]/div/div/div/div[3]'
                )
                post_button.click()
        except NoSuchElementException:
            print('No such element in twitter page.')


IS = InternetSpeedTwitterBot()
IS.get_internet_speed()
IS.tweet_at_provider()
