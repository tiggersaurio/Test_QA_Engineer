from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SelectFlights:
    def __init__(self,driver):
        self.driver = driver
        self.selectPrice_button = '//journey-control-custom/div/div/div[1]/div[2]/button'
        self.selectBasic_button ='//journey-control-custom/div/div/div[2]/div/div/div/div[1]/fare-control/div/div[3]/button'
        self.continue_button ='//*[@id="maincontent"]/div/div[2]/div/div/button-container/div/div/button'
        
    def get_selectPrice_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.selectPrice_button))
        )
    
    def get_selectBasic_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.selectBasic_button))
        )
    
    def get_continue_button(self):
        return self.driver.find_element(By.XPATH, self.continue_button)
    
    #Metodos
    def click_selectPrice_button(self):
        selectPrice_button = self.get_selectPrice_button()
        self.driver.execute_script("arguments[0].click();", selectPrice_button)
                
    def click_selectBasic_button(self):
        selectBasic_button = self.get_selectBasic_button()
        self.driver.execute_script("arguments[0].click();", selectBasic_button)