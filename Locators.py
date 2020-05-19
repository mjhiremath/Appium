from appium import webdriver
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

#Enter the data in search field
search_bar = driver.find_element_by_xpath('//android.widget.LinearLayout[@content-desc="Search on flipkart"]/android.widget.TextView').click()
driver.find_element_by_id('com.flipkart.android:id/search_autoCompleteTextView').send_keys("Iphone")
#search_bar.send_keys("Iphone")

#driver.set_value(search_bar,"Iphone")
#driver.press_keycode(84)

driver.execute_script('mobile:performEditorAction',{'action':'search'})

#Locate an element using class
try:
    location_not_now = driver.find_element_by_class_name('android.widget.Button')
    driver.set_value(location_not_now,"NOT NOW")
except InvalidElementStateException:
    driver.find_element_by_id('com.flipkart.android:id/not_now_button').click()
