import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.webDriver import WebDriverSetup
from src.pages.home import HomePage

class TestLanguageChange(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverSetup.initialize_driver()
        cls.driver.get("https://nuxqa6.avtest.ink/es/")
        cls.home = HomePage(cls.driver)

    #Cambiar idioma a Inglés
    def test_change_language_to_english(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_language_button()))
        self.home.get_language_button().click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_languageEn_option()))
        self.home.get_languageEn_option().click()

        time.sleep(2)
        
        self.assertIn('/en/', self.driver.current_url)
       
    #Cambiar idioma a Español
    def test_change_language_to_spanish(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_language_button()))
        self.home.get_language_button().click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_languageEs_option()))
        self.home.get_languageEs_option().click()

        time.sleep(2)

        self.assertIn('/es/', self.driver.current_url)
        
    #Cambiar idioma a Francés   
    def test_change_language_to_french(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_language_button()))
        self.home.get_language_button().click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_languageFr_option()))
        self.home.get_languageFr_option().click()

        time.sleep(2)

        self.assertIn('/fr/', self.driver.current_url)
    
    #Cambiar idioma a Portugues    
    def test_change_language_to_portuguese(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_language_button()))
        self.home.get_language_button().click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.home.get_languagePt_option()))
        self.home.get_languagePt_option().click()

        time.sleep(2)

        self.assertIn('/pt/', self.driver.current_url)
        
    @classmethod
    def tearDownClass(cls):
        WebDriverSetup.quit_driver(cls.driver)

if __name__ == "__main__":
    unittest.main()