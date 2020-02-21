### this python file complets the task of auto log in to the SMC school websites and adds the class in the class list array.
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("https://smccis.smc.edu/smcweb/f?p=520191216:102::::::")

##Enter Student ID
studentID = driver.find_element_by_id("P102_LOGIN_ID")
studentID.clear()
studentID.send_keys("yourStudentID")

##Enter Student Password
studentPassWord = driver.find_element_by_id("P102_PASSWORD")
studentPassWord.clear()
studentPassWord.send_keys("YourStudentPassword")

##press login
logInBotton = driver.find_element_by_id("P102_LOGIN")
logInBotton.send_keys(Keys.RETURN)

##press Enrollment Services
Enrollment_Services = driver.find_element_by_id("bgdEnroll")
Enrollment_Services.send_keys(Keys.RETURN)

##Choose Semaster 
semasterList = driver.find_element_by_id("P1_SEMCODE")
semasterList.send_keys(Keys.RETURN)
for option in semasterList.find_elements_by_tag_name('option'):
    if option.text == 'Spring 2020':
        option.click() 
        break

##add classes
while True:
    classSectionList = ['2724','4097','3195','2719','3196','3197','3198','4380','2721','2722','2723','4259','2728','2727']
    for index in range(len(classSectionList)):
        aClass = classSectionList[index]
        addClass = driver.find_element_by_link_text('Add a Class')
        addClass.send_keys(Keys.RETURN)
        addSectionNum = driver.find_element_by_id("P301_ADDSCTNUM")
        addSectionNum.clear()
        addSectionNum.send_keys(aClass)
        addTheClass = driver.find_element_by_id("B19745901389643700077")
        addTheClass.send_keys(Keys.RETURN)
        time.sleep(2)
        continueAdd = driver.find_element_by_id("B19746872779480575340")
        continueAdd.send_keys(Keys.RETURN)
        print("added a class",aClass)
    assert "No results found." not in driver.page_source
    time.sleep(10)


