import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Pytest:

    def test_MobNumberOfCred_005(self):
        driver= webdriver.Chrome()
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
### Find all index no. from value in list
        # for i in Contact_Number_List:
        #     print(f"Index no is:, {Contact_Number_List.index(i)} Value is:, {Contact_Number_List(i)}")
