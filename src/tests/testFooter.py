import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.webDriver import WebDriverSetup
from src.pages.home import homePage

class TestFooter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverSetup.initialize_driver()
        cls.driver.get("https://nuxqa6.avtest.ink/es/")
        cls.home = homePage(cls.driver)

    #Ir a Vuelos baratos
    def test_change_page_to_cheapFlights(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_cheapFlights_option()))
        self.home.get_cheapFlights_option().click()

        time.sleep(2)
        
        self.assertIn('/es/ofertas-destinos/ofertas-de-vuelos/', self.driver.current_url)
    
    def test_change_page_to_weAre(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_weAre_option()))
        self.home.get_weAre_option().click()

        time.sleep(2)
        
        self.assertIn('/es/sobre-nosotros/somos-avianca/', self.driver.current_url)
        
    def test_change_page_to_legalInfo(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_legalInfo_option()))
        self.home.get_legalInfo_option().click()

        time.sleep(2)
        
        self.assertIn('/es/informacion-legal/informacion-legal/', self.driver.current_url)
        
    @classmethod
    def tearDownClass(cls):
        WebDriverSetup.quit_driver(cls.driver)

if __name__ == "__main__":
    unittest.main()