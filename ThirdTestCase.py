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

#click on the menu
driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Drawer']").click()
#driver.find_element_by_id("Drawer").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='Electronics']").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='Laptops']").click()
driver.find_element_by_xpath("//android.widget.TextView[@bounds='[720,654][1080,909]']").click()
driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()

#get the price
price = driver.find_element_by_xpath("//android.widget.TextView[@bounds='[311,622][463,674]']").get_attribute("text")
print("the price of the laptop is ",price)
assert price == '₹49,990' , "price is not matched"







