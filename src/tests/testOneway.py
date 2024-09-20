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
    
    def wait_and_click(self, element):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element)).click()

    def wait_and_send_keys(self, element, keys):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element)).send_keys(keys)

    #Info para datos de pasajeros
    def fill_passenger_info(self, passenger_type, first_name, last_name):
        self.wait_and_click(self.passengers.get_passenger_element(passenger_type, 'gender'))
        self.wait_and_click(self.passengers.get_passenger_element(passenger_type, 'gender_select'))
        self.wait_and_send_keys(self.passengers.get_passenger_element(passenger_type, 'first_name'), first_name)
        self.wait_and_send_keys(self.passengers.get_passenger_element(passenger_type, 'last_name'), last_name)
        self.wait_and_click(self.passengers.get_passenger_element(passenger_type, 'day'))
        self.wait_and_click(self.passengers.get_passenger_element(passenger_type, 'day_select'))
        self.wait_and_click(self.passengers.get_passenger_element(passenger_type, 'month'))
        self.wait_and_click(self.passengers.get_passenger_element(passenger_type, 'month_select'))
        self.wait_and_click(self.passengers.get_passenger_element(passenger_type, 'year'))
        self.wait_and_click(self.passengers.get_passenger_element(passenger_type, 'year_select'))
        self.wait_and_click(self.passengers.get_passenger_element(passenger_type, 'nationality'))
        self.wait_and_click(self.passengers.get_passenger_element(passenger_type, 'nationality_select'))

    def test_bookingOneway(self):
        # Cambiar idioma
        self.wait_and_click(self.home.get_language_button())
        self.wait_and_click(self.home.get_languageEn_option())
        
        # Cambiar país
        self.wait_and_click(self.home.get_country_button())
        self.wait_and_click(self.home.get_countryCa_option())
        self.wait_and_click(self.home.get_apply_button())
        
        time.sleep(1)
        
        self.home.click_oneway_input_radio()
        
        # Llenar datos
        self.wait_and_click(self.home.get_origin_button())
        self.wait_and_send_keys(self.home.get_origin_input(), "Vancouver" + Keys.ENTER)
        time.sleep(2)
        self.wait_and_send_keys(self.home.get_arrive_input_OW(), "Barranquilla" + Keys.ENTER)
        
        # Selección de pasajeros
        self.wait_and_click(self.home.get_pass_select_OW())
        self.wait_and_click(self.home.get_passTeen_button())
        self.wait_and_click(self.home.get_passChild_button())
        self.wait_and_click(self.home.get_passInfant_button())

        self.wait_and_click(self.home.get_search_button())
        
        time.sleep(5)
        
        # Seleccionar vuelo
        self.selectFlights.click_selectPrice_button()
        self.selectFlights.click_selectBasic_button()
                
        time.sleep(5)
        
        self.wait_and_click(self.selectFlights.get_continue_button())
        
        time.sleep(5)

        # Llenar información de pasajeros
        self.fill_passenger_info('adult', "Pan", "Naranjo")
        self.fill_passenger_info('infant', "Coco", "Grajales")
        self.fill_passenger_info('teen', "Shakira", "Pineda")
        self.fill_passenger_info('child', "Chayanne", "Emilio")
        
        # Información de contacto
        self.wait_and_click(self.passengers.get_contact_element('prefix'))
        self.wait_and_click(self.passengers.get_contact_element('prefix_select'))
        self.wait_and_send_keys(self.passengers.get_contact_element('phone'), "3013114116")
        self.wait_and_send_keys(self.passengers.get_contact_element('email'), "daniela@test.com")
        
        self.passengers.click_tyc_button()
        self.passengers.click_continue_button()
        
        time.sleep(2)
    
    @classmethod
    def tearDownClass(cls):
        WebDriverSetup.quit_driver(cls.driver)

if __name__ == "__main__":
    unittest.main()