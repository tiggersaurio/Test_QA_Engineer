import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.webDriver import WebDriverSetup
from src.pages.home import HomePage

class TestHeader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverSetup.initialize_driver()
        cls.driver.get("https://nuxqa6.avtest.ink/es/")
        cls.home = HomePage(cls.driver)

    #Ir a Ofertas y vuelos
    def test_change_page_to_flyOffers(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_headerOffers_button()))
        self.home.get_headerOffers_button().click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_flyOffers_option()))
        self.home.get_flyOffers_option().click()

        time.sleep(2)
        
        #Validar idioma
        self.assertIn('/es/ofertas-destinos/ofertas-de-vuelos/', self.driver.current_url)
       
    #Ir a Destinos
    def test_change_page_to_destination(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_headerOffers_button()))
        self.home.get_headerOffers_button().click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_destination_option()))
        self.home.get_destination_option().click()

        time.sleep(2)
        
        #Validar idioma
        self.assertIn('/es/ofertas-destinos/destinos/', self.driver.current_url)
        
    def test_change_page_to_newRoutes(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_headerOffers_button()))
        self.home.get_headerOffers_button().click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_newRoutes_option()))
        self.home.get_newRoutes_option().click()

        time.sleep(2)
        
        #Validar idioma
        self.assertIn('/es/ofertas-destinos/nuevas-rutas/', self.driver.current_url)
        
    @classmethod
    def tearDownClass(cls):
        WebDriverSetup.quit_driver(cls.driver)

if __name__ == "__main__":
    unittest.main()