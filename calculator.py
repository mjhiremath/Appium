from appium import webdriver

dersired_caps = {
    "platformName": "Android",
    "deviceName" : "1130537a",
    "appPackage": "com.miui.calculator",
    "appActivity": "com.miui.calculator.cal.CalculatorActivity",
    "newCommandTimeout": 600,
    "automationName":"UiAutomator2"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=dersired_caps)
driver.implicitly_wait(5)

driver.find_element_by_id("android:id/button1").click()

#addition of 2 number

driver.find_element_by_id("com.miui.calculator:id/btn_1_s").click()
driver.find_element_by_id("com.miui.calculator:id/btn_plus_s").click()
driver.find_element_by_id("com.miui.calculator:id/btn_6_s").click()
driver.find_element_by_id("com.miui.calculator:id/btn_equal_s").click()
result = driver.find_element_by_id("com.miui.calculator:id/result").get_attribute("text")
print(result.strip("= "))
context = driver.current_context
print(context)

