from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from getUser import username, password
import time

class Instagram():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
    
    def kullaniciGiris(self):
        self.driver.get('https://www.instagram.com/accounts/login')
        time.sleep(2)

        self.driver.find_element(By.NAME,"username").send_keys(self.username)
        self.driver.find_element(By.NAME,"password").send_keys(self.password)
        self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(10)

        self.driver.find_element(By.CSS_SELECTOR,'div[role=button]').click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'._a9-z').find_element(By.CSS_SELECTOR,'._a9--._a9_1').click()
        time.sleep(2)

    def takipcileriAl(self):
        self.driver.get(f'https://www.instagram.com/{self.username}/')
        time.sleep(4)
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(3)
        
        fallowerList = self.driver.find_element(By.CSS_SELECTOR,'div[role=dialog]')
        userCount = len(fallowerList.find_elements(By.CSS_SELECTOR,'.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3'))

        while True:
            fallowerList.click()
        
            scrollCount = 4
            for i in range(scrollCount):
                self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
                time.sleep(10)

                newCount = len(fallowerList.find_elements(By.CSS_SELECTOR,'.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3'))
                if userCount != newCount:
                    userCount = newCount
                else:
                    break
        
            users = fallowerList.find_elements(By.CSS_SELECTOR,'.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3')
            for user in users:
                fallowerName = user.find_element(By.CSS_SELECTOR,'._ap3a._aaco._aacw._aacx._aad7._aade').text
                print(fallowerName)



instagram = Instagram(username, password)
instagram.kullaniciGiris()
instagram.takipcileriAl()
