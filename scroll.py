import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import InvalidElementStateException

desired_caps = {
    "platformName": "Android",
    "deviceName": "1130537a",
    "app": "C:\\Users\\mhiremat\\Downloads\\com.flipkart.android.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.implicitly_wait(30)

# clock on the close button
#driver.find_element_by_id("com.flipkart.android:id/btn_skip").click()


driver.find_element_by_id("com.flipkart.android:id/select_btn").click()
driver.find_element_by_id("com.google.android.gms:id/cancel").click()
driver.find_element_by_id("com.flipkart.android:id/custom_back_icon").click()

#click on the menu
driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Drawer']").click()
#driver.find_element_by_id("Drawer").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='Electronics']").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='Laptops']").click()
driver.find_element_by_xpath("//android.widget.TextView[@bounds='[720,654][1080,909]']").click()
driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()

'''
Touch class TouchAction(driver)   .press(x=469, y=1903)   .move_to(x=454, y=924)   .release()   .perform()
'''

for i in range(2):
    time.sleep(5)
    touch = TouchAction(driver)
    touch.press(x=469, y=1903).move_to(x=469, y=924).release().perform()




