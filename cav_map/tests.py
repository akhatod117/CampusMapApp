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
        assert "Welcome, Cav !" in driver.page_source
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
        elem = driver.find_element_by_xpath("/html/body/center[2]/a/img")
        elem.click()
    def mapLink(self):
        assert driver.getCurrentUrl()=="https://a01-cav-map.herokuapp.com/map/"
    def destCoord(self):
        inputElement = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/div[2]/div/div/input")
        inputElement.send_keys('New Cabell Hall University of Virginia')
        inputElement.send_keys(Keys.ENTER)
        expDestCoord='New Cabell Hall, 1605 Jefferson Park Ave, Charlottesville, Virginia 22903, United States'
        actDestCoord = inputElement.get_property('value')
        assert expDestCoord==actDestCoord
    def mapButtons(self):
        traffic=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/label[1]")
        traffic.click()
        trafficInfo=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div[1]").get_property('value')
        driving=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/label[2]")
        driving.click()
        drivingInfo=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div[1]').get_property('value')
        assert trafficInfo!=drivingInfo
    def mapButtons2(self):
        walking=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/label[3]")
        walking.click()
        walkingInfo=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div[1]").get_property('value')
        cycling=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/label[4]")
        cycling.click()
        cyclingInfo=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div[1]').get_property('value')
        assert walkingInfo!=cyclingInfo
    def invalidInput1(self):
        inputElement = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/div[2]/div/div/input")
        inputElement.send_keys(Keys.ENTER)
        directions=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div[1]")
        assert directions.isDisplayed()==False
    def invalidInput2(self):
        inputElement = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/div[2]/div/div/input")
        inputElement.send_keys('djfgkdg')
        inputElement.send_keys(Keys.ENTER)
        directions=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div[1]")
        assert directions.isDisplayed()==False
    def tearDown(self):
        driver.quit()

class RouteMakerTests(TestCase):
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
        elem = driver.find_element_by_xpath("/html/body/nav/div/div/ul/li[2]/a")
        elem.click()
    def link(self):
        assert driver.getCurrentUrl()=="https://a01-cav-map.herokuapp.com/routemaker/"
    def oneClass(self):
        inputElement = driver.find_element_by_name("class1")
        inputElement.send_keys('New Cabell Hall')
        generateMap=driver.find_element_by_xpath("/html/body/form/button[3]").click()
        wait.until(EC.presence_of_element_located(By.find_element_by_xpath("/html/body/h1")))
        expDestCoord='-78.50513,38.03254'
        actDestCoord = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/div[2]/div/div/input").get_property('value')
        assert expDestCoord==actDestCoord
    def twoClasses(self):
        class1 = driver.find_element_by_name("class1")
        class1.send_keys('New Cabell Hall')
        addButton=driver.find_element_by_id("addClass")
        addButton.click()
        class2=driver.find_element_by_name("class2")
        class2.send_keys("Old Cabell Hall")
        generateMap=driver.find_element_by_xpath("/html/body/form/button[3]").click()
        wait.until(EC.presence_of_element_located(By.find_element_by_xpath("/html/body/h1")))
        expDestCoord='-78.50463,38.03300'
        actDestCoord = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/div[2]/div/div/input").get_property('value')
        assert expDestCoord==actDestCoord
    def loadSavedRoute(self):
        button=driver.find_element_by_xpath('/html/body/form[1]/button')
        button.click()
        wait.until(EC.presence_of_element_located(By.find_element_by_xpath("/html/body/h1")))
        expDestCoord="-78.51090,38.03166"
        actDestCoord = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/div[2]/div/div/input").get_property('value')
        assert expDestCoord==actDestCoord
    def resetTest(self):
        class1 = driver.find_element_by_name("class1")
        class1.send_keys('New Cabell Hall')
        c1val=class1.get_property("value")
        assert c1val=="New Cabell Hall"
        resetButton=driver.find_element_by_xpath("/html/body/form/button[2]")
        resetButton.click()
        assert c1val==""
    def removeTest(self):
        addButton=driver.find_element_by_id("addClass")
        addButton.click()
        removeButton=driver.find_element_by_id("remClass")
        removeButton.click()
        assert driver.find_element_by_id("class2").isDisplayed()==False
    def tearDown(self):
        driver.quit()

class logisticsTests(TestCase):
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
    def logoutTest(self):
        logoutButton = driver.find_element_by_xpath("/html/body/nav/div/div/ul/li[3]/a")
        logoutButton.click()
        wait.until(EC.presence_of_element_located(By.find_element_by_xpath("/html/body/center[2]/a/img")))
        assert driver.find_element_by_xpath("/html/body/center[2]/a/img").isDisplayed()==True
    def homeButtonTest(self):
        mapButton = driver.find_element_by_xpath("/html/body/center[2]/a/img")
        mapButton.click()
        homeButton=driver.find_element_by_xpath("/html/body/nav/div/div/a")
        homeButton.click()
        assert driver.getCurrentUrl()=="https://a01-cav-map.herokuapp.com"
    def weatherTest(self):
        assert driver.find_element_by_xpath("/html/body/div/div[1]/span[1]").isDisplayed()==True
    def tearDown(self):
        driver.quit()

class CreatePostTests(TestCase):
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
        elem = driver.find_element_by_xpath("/html/body/nav/div/div/ul/li[4]/a")
        elem.click()
    def normalInput(self):
        title=driver.find_element_by_xpath('/html/body/form/div[1]/input')
        title.send_keys('I love CavMap!')
        post=driver.find_element_by_xpath('/html/body/form/div[2]/textarea')
        post.send_keys(':)')
        submit=driver.find_element_by_xpath('/html/body/form/input[2]')
        submit.click()
        forum=driver.find_element_by_xpath('/html/body/nav/div/div/ul/li[3]/a')
        forum.click()
        wait.until('Forums' in driver.page_source)
        assert "I love CavMap!" in driver.page_source
    def noTitleNoPost(self):
        submit=driver.find_element_by_xpath('/html/body/form/input[2]')
        submit.click()
        actualMsg = driver.findElement(By.xpath("//div[@id='statusMsg']/div[@class='alert in fade alert-error']")).getAttribute("innerHTML")
        expMsg="Please fill out this field"
        assert actualMsg.contains(expMsg)
    def noPost(self):
        title=driver.find_element_by_xpath('/html/body/form/div[1]/input')
        title.send_keys('I love CavMap!')
        submit=driver.find_element_by_xpath('/html/body/form/input[2]')
        submit.click()
        actualMsg = driver.findElement(By.xpath("//div[@id='statusMsg']/div[@class='alert in fade alert-error']")).getAttribute("innerHTML")
        expMsg="Please fill out this field"
        assert actualMsg.contains(expMsg)
    def noTitle(self):
        post=driver.find_element_by_xpath('/html/body/form/div[2]/textarea')
        post.send_keys(':)')
        submit=driver.find_element_by_xpath('/html/body/form/input[2]')
        submit.click()
        actualMsg = driver.findElement(By.xpath("//div[@id='statusMsg']/div[@class='alert in fade alert-error']")).getAttribute("innerHTML")
        expMsg="Please fill out this field"
        assert actualMsg.contains(expMsg)
    def forumLink(self):
        link=driver.find_element_by_xpath('/html/body/nav/div/div/ul/li[3]/a')
        link.click()
        assert driver.getCurrentUrl()=="https://a01-cav-map.herokuapp.com/forum/"
    def tearDown(self):
        driver.quit()





