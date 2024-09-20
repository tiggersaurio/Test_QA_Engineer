import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.webDriver import WebDriverSetup
from src.pages.home import HomePage
from src.pages.selectFlights import SelectFlights
from src.pages.passengers import Passengers

class TestOneway(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverSetup.initialize_driver()
        cls.driver.get("https://nuxqa6.avtest.ink/es/")
        cls.home = HomePage(cls.driver)
        cls.selectFlights = SelectFlights(cls.driver)
        cls.passengers = Passengers(cls.driver)
    
    def test_bookingRoundtripHome(self):
        #Cambiar idioma
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
        
        #Llenar datos
        origin_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_origin_button()))
        origin_button.click()
        origin_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_origin_input()))
        origin_input.send_keys("Vancouver")
        origin_input.send_keys(Keys.ENTER)
        
        arrive_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_arrive_input_RT()))
        arrive_input.send_keys("Barranquilla")
        arrive_input.send_keys(Keys.ENTER)

        #Seleccionar pasajeros
        pass_select = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_pass_select_RT()))
        pass_select.click()

        passTeen_button = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.home.get_passTeen_button()))
        passTeen_button.click()

        passChild_button = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.home.get_passChild_button()))
        passChild_button.click()

        passInfant_button = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.home.get_passInfant_button()))
        passInfant_button.click()

        #buscar
        search_button = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.home.get_search_button()))
        search_button.click()
        
        time.sleep(10)      
    
    
    @classmethod
    def tearDownClass(cls):
        WebDriverSetup.quit_driver(cls.driver)

if __name__ == "__main__":
    unittest.main()
