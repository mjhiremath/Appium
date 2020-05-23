import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import InvalidElementStateException

desired_caps = {
    "platformName": "Android",
    "deviceName": "1130537a",
    "app": "C:\\Users\\mhiremat\\Downloads\\Contacts_v3.23.1.310566111_apkpure.com.apk",
    "appPackage": "com.google.android.contacts",
    "appActivity": "com.android.contacts.activities.PeopleActivity",
    "newCommandTimeout": 600
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.implicitly_wait(30)

#allow permission
for i in range(2):
    driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
    time.sleep(3)

#driver.find_element_by_id("android:id/list").click()
#driver.find_element_by_xpath("//android.widget.ListView[@bounds='[0,234][1080,2131]']").click()
time.sleep(5)
#tap on the create button
touch = TouchAction(driver)
touch.tap(x=926, y=2073).perform()
time.sleep(5)
file_name = driver.current_activity+"_"+time.strftime("%H%M%S")

#taking screenshot
driver.save_screenshot("C:\\Users\\mhiremat\\PycharmProjects\\appium\\Screenshots\\"+file_name+".png")

touch.press(x=952, y=1660).wait(3).move_to(x=958, y=1259).wait(3).release().perform()

#click on the more field button
touch.tap(x=247, y=2122).perform()

time.sleep(2)
touch.press(x=984, y=1923).move_to(x=974, y=1352).release().perform()
time.sleep(2)
touch.press(x=999, y=1514).move_to(x=989, y=1030).release().perform()

#click on the phone drop-down
driver.find_element_by_xpath("(//android.widget.ImageButton[@content-desc='Show drop-down menu'])[1]").click()

