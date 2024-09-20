from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.language_button = 'button.dropdown_trigger.dropdown_trigger--active'
        self.languageEn_option = "//button[contains(@class, 'options-list_item_option') and contains(., 'English')]"
        self.languageEs_option = "//button[contains(@class, 'options-list_item_option') and contains(., 'Español')]"
        self.languageFr_option = "//button[contains(@class, 'options-list_item_option') and contains(., 'Français')]"
        self.languagePt_option = "//button[contains(@class, 'options-list_item_option') and contains(., 'Português')]"
        self.country_button = 'button.point-of-sale-selector_button'
        self.country_text_button = (By.XPATH, '//*[@id="pointOfSaleSelectorId"]/span[2]')
        self.countryCa_option = '//*[@id="pointOfSaleListId"]/li[4]/button/span[1]' 
        self.countryEu_option = '//*[@id="pointOfSaleListId"]/li[10]/button/span[1]' 
        self.countryCh_option = '//*[@id="pointOfSaleListId"]/li[5]/button/span[1]'
        self.apply_button ='button.points-of-sale_footer_action_button'
        self.headerOffers_button = '//*[@id="mainHeaderDiv"]/main-header-container/main-header-layout-custom/header/div[2]/div[2]/primary-nav-custom/nav/ul/li[2]/button'
        self.flyOffers_option = '//*[@id="primary-nav-sub-menu-1"]/div/div/div[2]/div/nav/ul/li[1]/a'
        self.destination_option = '//*[@id="primary-nav-sub-menu-1"]/div/div/div[2]/div/nav/ul/li[2]/a'
        self.newRoutes_option = '//*[@id="primary-nav-sub-menu-1"]/div/div/div[2]/div/nav/ul/li[4]/a'
        self.container = 'ibeSearchJourneyTypeControlId'
        self.oneway_input_radio = 'journeytypeId_1'
        self.origin_button = "button#originBtn.control_field_button"
        self.origin_input = "input.control_field_input"
        self.arrive_input_OW = '//*[@id="searchContentId_OW"]/div[1]/station-control-custom/div/div[1]/div[2]/div[3]/div/input'
        self.arrive_input_RT = '//*[@id="searchContentId_RT"]/div[1]/station-control-custom/div/div[1]/div[2]/div[3]/div/input'
        self.destination_select = "BOG"
        self.pass_select_RT = '//*[@id="searchContentId_RT"]/div[3]/pax-control-custom/div/div/div[2]/div/button'
        self.pass_select_OW = '//*[@id="searchContentId_OW"]/div[3]/pax-control-custom/div/div/div[2]/div/button'
        self.passTeen_button = '//*[@id="paxControlSearchId"]/div/div[2]/div[1]/ul/li[2]/div[2]/ibe-minus-plus/div/button[2]'
        self.passChild_button = '//*[@id="paxControlSearchId"]/div/div[2]/div[1]/ul/li[3]/div[2]/ibe-minus-plus/div/button[2]'
        self.passInfant_button = '//*[@id="paxControlSearchId"]/div/div[2]/div[1]/ul/li[4]/div[2]/ibe-minus-plus/div/button[2]'
        self.search_button = 'searchButton'
        self.cheapFlights_option = '//*[@id="footerNavListId-0"]/li[1]/a'
        self.weAre_option = '//*[@id="footerNavListId-1"]/li[1]/a'
        self.legalInfo_option = '//*[@id="footerNavListId-3"]/li[1]/a'
        
    def get_language_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.language_button)
    
    def get_languageEn_option(self):
        return self.driver.find_element(By.XPATH, self.languageEn_option)
    
    def get_languageEs_option(self):
        return self.driver.find_element(By.XPATH, self.languageEs_option)
    
    def get_languageFr_option(self):
        return self.driver.find_element(By.XPATH, self.languageFr_option)
    
    def get_languagePt_option(self):
        return self.driver.find_element(By.XPATH, self.languagePt_option)
    
    def get_country_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.country_button)
    
    def get_country_text_button(self):
        return self.country_text_button
    
    def get_countryCa_option(self):
        return self.driver.find_element(By.XPATH, self.countryCa_option)
    
    def get_countryEu_option(self):
        return self.driver.find_element(By.XPATH, self.countryEu_option)
    
    def get_countryCh_option(self):
        return self.driver.find_element(By.XPATH, self.countryCh_option)
    
    def get_apply_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.apply_button)
    
    def get_headerOffers_button(self):
        return self.driver.find_element(By.XPATH, self.headerOffers_button)
    
    def get_flyOffers_option(self):
        return self.driver.find_element(By.XPATH, self.flyOffers_option)
    
    def get_destination_option(self):
        return self.driver.find_element(By.XPATH, self.destination_option)
    
    def get_newRoutes_option(self):
        return self.driver.find_element(By.XPATH, self.newRoutes_option)
    
    def get_container(self):
        return self.driver.find_element(By.ID, self.container)
    
    def get_oneway_input_radio(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, self.oneway_input_radio))
        )

    def get_origin_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.origin_button)

    def get_origin_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.origin_input)
    
    def get_arrive_input_RT(self):
        return self.driver.find_element(By.XPATH, self.arrive_input_RT)
    
    def get_arrive_input_OW(self):
        return self.driver.find_element(By.XPATH, self.arrive_input_OW)

    def get_destination_select(self):
        return self.driver.find_element(By.ID, self.destination_select)

    def get_pass_select_RT(self):
        return self.driver.find_element(By.XPATH, self.pass_select_RT)
    
    def get_pass_select_OW(self):
        return self.driver.find_element(By.XPATH, self.pass_select_OW)

    def get_passTeen_button(self):
        return self.driver.find_element(By.XPATH, self.passTeen_button)

    def get_passChild_button(self):
        return self.driver.find_element(By.XPATH, self.passChild_button)

    def get_passInfant_button(self):
        return self.driver.find_element(By.XPATH, self.passInfant_button)
    
    def get_search_button(self):
        return self.driver.find_element(By.ID, self.search_button)
    
    def get_cheapFlights_option(self):
        return self.driver.find_element(By.XPATH, self.cheapFlights_option)
    
    def get_weAre_option(self):
        return self.driver.find_element(By.XPATH, self.weAre_option)
    
    def get_legalInfo_option(self):
        return self.driver.find_element(By.XPATH, self.legalInfo_option)
    
    
    #Metodos
        
    def click_oneway_input_radio(self):
        oneway_radio = self.get_oneway_input_radio()
        self.driver.execute_script("arguments[0].click();", oneway_radio)

    def set_origin(self, origin):
        self.get_origin_button().click()
        self.get_origin_input().send_keys(origin)
        self.get_origin_input().send_keys(Keys.TAB)
        
    def set_arrive_RT(self, arrive):
        self.get_arrive_input_RT().click()
        self.get_arrive_input_RT().send_keys(arrive)
        
    def set_arrive_OW(self, arrive):
        self.get_arrive_input_OW().click()
        self.get_arrive_input_OW().send_keys(arrive)

    def click_destination_select(self):
        self.get_destination_select().click()

    def click_pass_select_RT(self):
        self.get_pass_select_RT().click()
        
    def click_pass_select_OW(self):
        self.get_pass_select_OW().click()

    def click_passTeen_button(self):
        self.get_passTeen_button().click()

    def click_passChild_button(self):
        self.get_passChild_button().click()

    def click_passInfant_button(self):
        self.get_passInfant_button().click()
        
    def click_search_button(self):
        self.get_search_button().click()