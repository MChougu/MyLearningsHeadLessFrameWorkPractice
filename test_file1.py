from selenium import webdriver
class Test_Pytest:
    def test_sum_001(self):
        a=3
        b=4
        sum= a+b
        print(sum)

    def test_sum_002(self):
        a=3
        b=5
        sum= a+b
        print(sum)
        if sum == 8:   # try 6
            assert True ####=== to exception
        else:
            assert False

    def test_sum_003(self):
        a=3
        b=6
        sum= a+b
        print(sum)

    def test_URLofCred_004(self):
        driver= webdriver.Chrome()
        driver.get("https://automation.credence.in/shop")
        if driver.title =="Credence":    # try crdnces
            print("you are at Right Place")
        else:
            print("you are at WRONG Place")
