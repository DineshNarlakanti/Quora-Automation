# import statements
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains

# Opens Chrome browser
driver = webdriver.Chrome(executable_path="C:\\Users\\Dinesh Kumar\\Downloads\\chromedriver91\\chromedriver.exe")

# Opens Quora
driver.get("https://www.quora.com/")

# Maximizes the window and waits
'''driver.maximize_window( )'''
driver.implicitly_wait(10)

# Enters credentials to login into the account
driver.maximize_window()
driver.find_element(By.XPATH, "//*[@id='email']").send_keys("n.dinesh.kumar123@gmail.com")
password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys("Qwerty123!")
password.send_keys(Keys.ENTER)
driver.refresh()


# Class creation
class Quora:

    # Method creation
    def execute(self, link):
        driver.get(link)
        driver.execute_script("window.scrollBy(0,200)")
        driver.find_element_by_name("BallotBox").click()
        driver.find_element_by_xpath("//div[text()='Suggestions']").click()

        #Clock
        time.sleep(3)
        wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div/div[2]/div/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div/div/div/button"))).click()
        #Queue
        wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/button"))).click()

        for i in range(100):
            try:
                time.sleep(3)
                wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//*[@name='Clock'])[1]"))).click()
                wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/button"))).click()

            except Exception as ex:
                print("Exception Occured, No suggestions in: ", link)
                break


# Object creation
q1 = Quora()

# Method execution
q1.execute('http://www.quora.com/q/infosysnewscareers')
q1.execute('http://www.quora.com/q/hcltechnologies')
q1.execute('http://www.quora.com/q/deloitte')
q1.execute('http://www.quora.com/q/indiansoftwareindustry1')
q1.execute('http://www.quora.com/q/ibmnewscareers')
q1.execute('http://www.quora.com/q/accenture1')
q1.execute('http://www.quora.com/q/allabouttcs')
q1.execute('http://www.quora.com/q/allabouttcs')
q1.execute('http://www.quora.com/q/cognizant1')
q1.execute('http://www.quora.com/q/srmuniversity')
q1.execute('http://www.quora.com/q/techmahindra')
q1.execute('http://www.quora.com/q/amazoncareers')
q1.execute('http://www.quora.com/q/microsoftjobscareers')


'''q1.execute('http://www.quora.com/q/arizonastateuniversity')
q1.execute('http://www.quora.com/q/cryptocurrencytradinginfo')
q1.execute('http://www.quora.com/q/computersciencecomputerscientists')
q1.execute('http://www.quora.com/q/indiansoftwareindustry1')
q1.execute('http://www.quora.com/q/allaboutlpu')
q1.execute('http://www.quora.com/q/vitvellore')
q1.execute('http://www.quora.com/q/overseaseducation1')
q1.execute('http://www.quora.com/q/wiproit')
q1.execute('http://www.quora.com/q/universityofhouston')
q1.execute('http://www.quora.com/q/universityofflorida')
q1.execute('http://www.quora.com/q/northeasternuniversity')'''
