from selenium import webdriver
import time
#
# def login():
#     url = "https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
#     driver.get(url)
#     #  whsOnd zHQkBf
#     time.sleep(5)
#     driver.find_element_by_class_name("whsOnd").send_keys("contactjaidesai2@gmail.com")
#     driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
#
# if __name__ == "__main__":
#     driver = webdriver.Chrome('driver/chromedriver')
#
#     login()
#
#     done = input("Close Window: ")
#
#     if done == "y":
#         driver.close()

# driver = webdriver.Firefox(executable_path='/Users/jaidesai/PycharmProjects/supSel/geckoDriver/geckodriver.exe')

driver = webdriver.Chrome("/Users/jaidesai/PycharmProjects/supSel/driver/chromedriver")
def gmailLogin():
    driver.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
    time.sleep(1)
    driver.find_element_by_class_name("whsOnd").send_keys("contactjaidesai2@gmail.com")
    time.sleep(.5)
    driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
    time.sleep(1)

    driver.find_element_by_class_name("whsOnd").send_keys("password")
    time.sleep(.5)
    driver.find_element_by_class_name("VfPpkd-RLmnJb").click()

# whsOnd zHQkBf
done = input("Done? ")

if done == "y":
    driver.close()
