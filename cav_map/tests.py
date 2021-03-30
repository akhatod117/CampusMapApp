from django.test import TestCase 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create your tests here.

class loginTests(TestCase):
    def loginTest1(self):
        driver = webdriver.Firefox()
        driver.get("https://a01-cav-map.herokuapp.com/")
        elem = driver.find_element_by_xpath("/html/body/center[2]/a/img")
        elem.click()
        assert driver.getCurrentUrl() == "https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?client_id=823802312794-pkhha8pm0cii1md47pk5ig8mprkjfina.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fa01-cav-map.herokuapp.com%2Faccounts%2Fgoogle%2Flogin%2Fcallback%2F&scope=profile%20email&response_type=code&state=qsaRulWvceZB&access_type=online&flowName=GeneralOAuthFlow"
        driver.quit()
    def loginTest2(self):
        driver = webdriver.Firefox()
        driver.get("https://a01-cav-map.herokuapp.com/")
        elem = driver.find_element_by_xpath("/html/body/center[2]/a/img")
        elem.click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(By.name("identifier")))
        driver.findElement(By.name("identifier")).sendKeys("cav.mapp@gmail.com")
        driver.findElement(By.name("identifier")).sendKeys(Keys.RETURN)
        wait.until(EC.presence_of_element_located(By.name("password")))
        driver.findElement(By.name("password")).sendKeys("Spring2021")
        driver.findElement(By.name("password")).sendKeys(Keys.RETURN)
        assert "Welcome, cav !" in driver.page_source
        driver.quit()

class mapTests(TestCase):
    def setUp(self):
        driver = webdriver.Firefox()
        driver.get("https://a01-cav-map.herokuapp.com/")
        elem = driver.find_element_by_xpath("/html/body/center[2]/a/img")
        elem.click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(By.name("identifier")))
        driver.findElement(By.name("identifier")).sendKeys("cav.mapp@gmail.com")
        driver.findElement(By.name("identifier")).sendKeys(Keys.RETURN)
        wait.until(EC.presence_of_element_located(By.name("password")))
        driver.findElement(By.name("password")).sendKeys("Spring2021")
        driver.findElement(By.name("password")).sendKeys(Keys.RETURN)
    def mapLink(self):
        elem = driver.find_element_by_xpath("/html/body/center[2]/a/img")
        elem.click()
        assert driver.getCurrentUrl()=="https://a01-cav-map.herokuapp.com/map/"
    def tearDown(self):
        driver.quit()




