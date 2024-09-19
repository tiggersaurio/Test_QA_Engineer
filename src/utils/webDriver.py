from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverSetup:
    @staticmethod
    def initialize_driver():
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        return driver

    @staticmethod
    def quit_driver(driver):
        if driver:
            driver.quit()
    
    
    
#cls.driver.get("https://nuxqa6.avtest.ink/es/")
