import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.webDriver import WebDriverSetup
from src.pages.home import homePage

class TestOneway(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverSetup.initialize_driver()
        cls.driver.get("https://nuxqa6.avtest.ink/es/")
        cls.home = homePage(cls.driver)
    
    def test_bookingOneway(self):
        #Cambiar idioma a Inglés
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_language_button()))
        self.home.get_language_button().click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_languageEn_option()))
        self.home.get_languageEn_option().click()
        
        #Cambiar país
        country_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_country_button()))
        country_button.click()

        canada_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_countryCa_option()))
        canada_option.click()

        apply_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_apply_button()))
        apply_button.click()
        
        #Llenar form
        container = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.home.get_container()))
        oneway_input_radio = container.find_element(EC.element_to_be_clickable(self.home.get_oneway_input_radio()))
        oneway_input_radio.click()
        
        origin_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_origin_button()))
        origin_button.click()
        origin_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_origin_input()))
        origin_input.send_keys("Vancouver")
        origin_input.send_keys(Keys.ENTER)
        
        arrive_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_arrive_input()))
        arrive_input.send_keys("Bogota")
        arrive_input.send_keys(Keys.ENTER)

        
        time.sleep(5)
    
    @classmethod
    def tearDownClass(cls):
        WebDriverSetup.quit_driver(cls.driver)

if __name__ == "__main__":
    unittest.main()
