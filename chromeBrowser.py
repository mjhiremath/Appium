from appium import webdriver


desired_caps = {
    "platformName":"Android",
    "deviceName":"1130537a",
    'automationName': 'UIAutomator2',
    'browserName': 'Chrome'
}


webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
