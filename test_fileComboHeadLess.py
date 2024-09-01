import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
HeadLess_Option =webdriver.ChromeOptions()
HeadLess_Option.add_argument("headLess")
class Test_Pytest:
    def Test_OrangeHRM_006(self):
        driver= webdriver.Chrome(options= HeadLess_Option)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(4)
        ##enter username
        # driver.find_element(By.NAME,"username").send_keys("Admin")
        driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        #Enter pswd
        # driver.find_element(By.NAME,"").send_keys("admin123")
        driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
        time.sleep(3)
        #click on login
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        # LOgout
        ## Click to dropdown
        driver.find_element(By.XPATH,"//span[@class='oxd-userdropdown-tab']").click()
        time.sleep(2)
        #Click on Logout
        driver.find_element(By.XPATH,"//a[normalize-space()='Logout']")
        time.sleep(2)
        ##### You can explore TestCaseStudio--- selectorhubs--- just add in your browser.

    def test_Amazon_GetRandom_Items_007(self):
        driver = webdriver.Chrome(options= HeadLess_Option)
        driver.get("https://www.amazon.in/")
        driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("women kurties")
        driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
        l = len(driver.find_elements(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div'))
        print(l)
        RandomNum = random.randint(1, l + 1)
        driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[' + str(
            RandomNum) + "]").click()
        time.sleep(4)
        print("Page Title is", driver.title)
        print("selected Item No is: ", RandomNum)

    def test_CredKart_LOGinSucessful_008(self):
        driver = webdriver.Chrome(options= HeadLess_Option)
        driver.get("https://automation.credence.in/shop")
        driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        driver.find_element(By.ID, "email").send_keys("Credence11@credence.in")
        driver.find_element(By.ID, "password").send_keys("Credence@123")
        # untick, tick check BOX
        driver.find_element(By.XPATH, "//input[@name='remember']").is_selected()
        time.sleep(2)
        # driver.find_element(By.XPATH,"//input[@name='remember']").is_enabled()
        time.sleep(2)
        # Click on Login Button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # check Logout option
        driver.find_element(By.XPATH, '//*[@id="navbar"]/ul[2]/li[3]/a').click()
        time.sleep(1)
        # Click on Login
        driver.find_element(By.XPATH, '//*[@id="navbar"]/ul[2]/li[3]/ul/li/a').click()
        time.sleep(2)

    def test_MobNumberOfCred_009(self):
        driver= webdriver.Chrome(options= HeadLess_Option)
        driver.get("https://credence.in")
        driver.find_element(By.XPATH,"//img[@src='/website/images/enquiry.png']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//h4[normalize-space()='Select Number']").click()
        l = len(driver.find_elements(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a"))
        print("l is:;;", l)
        ##### 1:25:00 index option inspect
        Contact_Number_List =[]
        for r in range(1, l+1):
            Contact_Number = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a[" +str(r)+ "]").text
            print("no. is: ", Contact_Number)
            Contact_Number_List.append(Contact_Number)
        print(Contact_Number_List)   ## ['+91 8237916162', '+91 7391053250', '+91 9579064658']
#### Check if this value present in list or not
        if "+91 7391053250" in Contact_Number_List:
            print("It is present")
            assert True
        else:
            print("it is Absent")
            assert False
### Find index no. from value in list
        ChkMobileNo= "+91 7391053250"
        if ChkMobileNo in Contact_Number_List:
            print("It is present and it's Index no is:", Contact_Number_List.index(ChkMobileNo))
            assert True
        else:
            assert False





