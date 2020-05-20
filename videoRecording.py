import base64
import os
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

driver.start_recording_screen()
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

raw_video = driver.stop_recording_screen()

file_name = driver.current_activity+"_"+time.strftime("%Y_%m_%d_%H%M%S")
'''
do the video recording
construct file name
'''

file_path = os.path.join("C:\\Users\\mhiremat\\PycharmProjects\\appium\\Screenshots\\"+file_name+".mp4")

with open(file_path,"wb") as vd:
    vd.write(base64.b64decode(raw_video))



