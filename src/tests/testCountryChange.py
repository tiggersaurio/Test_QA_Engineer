import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.utils.webDriver import WebDriverSetup
from src.pages.home import HomePage

class TestCountryChange(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverSetup.initialize_driver()
        cls.driver.get("https://nuxqa6.avtest.ink/es/")
        cls.home = HomePage(cls.driver)
        
    #Cambiar país a Canadá
    def test_change_country_to_canada(self):
        country_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_country_button()))
        country_button.click()

        canada_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_countryCa_option()))
        canada_option.click()

        apply_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_apply_button()))
        apply_button.click()

        time.sleep(2)

        #Se valida el cambio de país
        country_text_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.home.get_country_text_button()))
        self.assertEqual(country_text_button.text, 'Canadá\nUSD', "El texto del botón de país no es 'Canada USD'")
     
    #Cambiar país a Chile
    def test_change_country_to_chile(self):
        country_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_country_button()))
        country_button.click()

        chile_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_countryCh_option()))
        chile_option.click()

        apply_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_apply_button()))
        apply_button.click()

        time.sleep(2)

        #Se valida el cambio de país
        country_text_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.home.get_country_text_button()))
        self.assertEqual(country_text_button.text, 'Chile\nUSD', "El texto del botón de país no es 'Chile USD'")
    
    #Cambiar país a España   
    def test_change_country_to_spain(self):
        country_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_country_button()))
        country_button.click()

        spain_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_countryEu_option()))
        spain_option.click()

        apply_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_apply_button()))
        apply_button.click()

        time.sleep(2)

        #Se valida el cambio de país
        country_text_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.home.get_country_text_button()))
        self.assertEqual(country_text_button.text, 'España\n€', "El texto del botón de país no es 'España €'")   

    @classmethod
    def tearDownClass(cls):
        WebDriverSetup.quit_driver(cls.driver)

if __name__ == "__main__":
    unittest.main()