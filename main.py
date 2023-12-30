import time
import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

EMAIL = os.environ.get('login')
PASS = os.environ.get('pass')

PROMISED_DOWN = 8
PROMISED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url='https://www.reg.ru/web-tools/speedtest')
        self.driver.find_element(By.XPATH, value='//*[@id="content"]/div/article[1]/div/button[1]').click()
        time.sleep(60)
        self.down = self.driver.find_element(By.ID, value='downloadValue').text
        self.up = self.driver.find_element(By.ID, value='uploadValue').text

    def tweet_at_provider(self):
        self.driver.get(url='https://twitter.com/home?lang=en')
        time.sleep(5)
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/'
                                                 'main/div/div/div[1]/div/div/div[3]/div[5]/a').click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/'
                                                 'div[2]/div[2]/div/div/div/div[5]/label/div/'
                                                 'div[2]/div/input').send_keys(EMAIL, Keys.ENTER)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/'
                                                 'div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/'
                                                 'div[1]/input').send_keys(PASS, Keys.ENTER)
        time.sleep(10)
        post_text = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                             'div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                             'div[1]/div/div/div/div/div/div/div/div/div/div/label/'
                                                             'div[1]/div/div/div/div/div/div[2]/div')
        post_text.send_keys(f'Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when i pay'
                            f' for {PROMISED_DOWN}down/{PROMISED_UP}up?')
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/'
                                                 'div[3]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                 'div[2]/div[2]/div/div/div/div[3]').click()


ist_bot = InternetSpeedTwitterBot()
ist_bot.get_internet_speed()
ist_bot.tweet_at_provider()
