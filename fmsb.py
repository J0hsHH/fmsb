from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class itsb:

    def __init__(self):
     self.driver = webdriver.Firefox()
    def login_it(self):
     sleep(4)
     self.driver.get('https://www.facebook.com/')    #login in with facebook
     sleep(2)
     norge = self.driver.find_element_by_xpath('//*[@id="u_0_h"]')
     norge.click()
     norge1 = self.driver.find_element_by_xpath('//*[@id="u_0_k"]')
     norge1.click()
     sv = self.driver.find_element_by_xpath('//*[@id="email"]')
     sv.click()
     le = self.driver.find_element_by_xpath('//*[@id="email"]')
     sleep(2)
     le.click()
     le.send_keys('YOUR phone or email') # YOUR phone or email (le stands for login email)
     sleep(2)
     lp = self.driver.find_element_by_xpath('//*[@id="pass"]')
     sleep(1)
     lp.click()
     lp.send_keys('YOUR PASSWORD') # YOUR PASSWORD (lp stands for login PASSWORD)
     sleep(1)
     lib = self.driver.find_element_by_xpath('//*[@id="u_0_b"]')
     lib.click()   # it just clicks on the log in button (lib stands for log in box)
     sleep(2)
     cmb = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/span/div')
     cmb.click()   # clicks on the measseger button (cmd stands for chat messenger button)
     sleep(2)

     # select the person you want to spam by defult it's the last person you have message

     sleep(2)
     person = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/a/div[1]/div[2]')
     person.click()
     sleep(4)

     emoji = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/span[2]/div')

     while True:
      #maybe have sleep(3)
      #sleep(3)
      emoji.click()

bot = itsb()
bot.login_it()
