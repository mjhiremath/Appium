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

#take screeshot and save with filename

activity = driver.current_activity
ts = time.strftime("%Y_%m_%d_%H%M%S")
file_name = activity+"_"+ts
time.sleep(4)

driver.save_screenshot("C:\\Users\\mhiremat\\PycharmProjects\\appium\\Screenshots\\"+file_name+".png")