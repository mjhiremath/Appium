from appium import webdriver


desired_caps = {
    "platformName": "Android",
    "deviceName": "1130537a",
    "app": "C:\\Users\\mhiremat\\Downloads\\com.flipkart.android.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)

driver.quit()