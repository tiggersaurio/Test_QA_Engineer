from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Passengers:
    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            'adult': {
                'gender': '//*[@id="IdPaxGender_7E7E303030312D30312D30317E353334423438324433313244343535383534"]',
                'gender_select': '//*[@id="IdPaxGender_7E7E303030312D30312D30317E353334423438324433313244343535383534-1"]',
                'first_name': '//*[@id="IdFirstName7E7E303030312D30312D30317E353334423438324433313244343535383534"]',
                'last_name': '//*[@id="IdLastName7E7E303030312D30312D30317E353334423438324433313244343535383534"]',
                'day': '//*[@id="dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_"]',
                'month': '//*[@id="dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_"]',
                'year': '//*[@id="dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_"]',
                'nationality': '//*[@id="IdDocNationality_7E7E303030312D30312D30317E353334423438324433313244343535383534"]',
                'day_select': '//*[@id="dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_-2"]',
                'month_select': '//*[@id="dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_-1"]',
                'year_select': '//*[@id="dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_-11"]',
                'nationality_select': '//*[@id="IdDocNationality_7E7E303030312D30312D30317E353334423438324433313244343535383534-4"]',
            },
            'infant': {
                'gender': '//*[@id="IdPaxGender_7E7E303030312D30312D30317E353334423438324433343244343535383534"]',
                'gender_select': '//*[@id="IdPaxGender_7E7E303030312D30312D30317E353334423438324433343244343535383534-1"]',
                'first_name': '//*[@id="IdFirstName7E7E303030312D30312D30317E353334423438324433343244343535383534"]',
                'last_name': '//*[@id="IdLastName7E7E303030312D30312D30317E353334423438324433343244343535383534"]',
                'day': '//*[@id="dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433343244343535383534_"]',
                'month': '//*[@id="dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433343244343535383534_"]',
                'year': '//*[@id="dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433343244343535383534_"]',
                'nationality': '//*[@id="IdDocNationality_7E7E303030312D30312D30317E353334423438324433343244343535383534"]',
                'day_select': '//*[@id="dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433343244343535383534_-2"]',
                'month_select': '//*[@id="dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433343244343535383534_-1"]',
                'year_select': '//*[@id="dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433343244343535383534_-1"]',
                'nationality_select': '//*[@id="IdDocNationality_7E7E303030312D30312D30317E353334423438324433343244343535383534-4"]',
            },
            'teen': {
                'gender': '//*[@id="IdPaxGender_7E7E303030312D30312D30317E353334423438324433323244343535383534"]',
                'gender_select': '//*[@id="IdPaxGender_7E7E303030312D30312D30317E353334423438324433323244343535383534-1"]',
                'first_name': '//*[@id="IdFirstName7E7E303030312D30312D30317E353334423438324433323244343535383534"]',
                'last_name': '//*[@id="IdLastName7E7E303030312D30312D30317E353334423438324433323244343535383534"]',
                'day': '//*[@id="dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_"]',
                'month': '//*[@id="dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_"]',
                'year': '//*[@id="dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_"]',
                'nationality': '//*[@id="IdDocNationality_7E7E303030312D30312D30317E353334423438324433323244343535383534"]',
                'day_select': '//*[@id="dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_-2"]',
                'month_select': '//*[@id="dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_-1"]',
                'year_select': '//*[@id="dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_-2"]',
                'nationality_select': '//*[@id="IdDocNationality_7E7E303030312D30312D30317E353334423438324433323244343535383534-4"]',
            },
            'child': {
                'gender': '//*[@id="IdPaxGender_7E7E303030312D30312D30317E353334423438324433333244343535383534"]',
                'gender_select': '//*[@id="IdPaxGender_7E7E303030312D30312D30317E353334423438324433333244343535383534-1"]',
                'first_name': '//*[@id="IdFirstName7E7E303030312D30312D30317E353334423438324433333244343535383534"]',
                'last_name': '//*[@id="IdLastName7E7E303030312D30312D30317E353334423438324433333244343535383534"]',
                'day': '//*[@id="dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433333244343535383534_"]',
                'month': '//*[@id="dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433333244343535383534_"]',
                'year': '//*[@id="dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433333244343535383534_"]',
                'nationality': '//*[@id="IdDocNationality_7E7E303030312D30312D30317E353334423438324433333244343535383534"]',
                'day_select': '//*[@id="dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433333244343535383534_-2"]',
                'month_select': '//*[@id="dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433333244343535383534_-1"]',
                'year_select': '//*[@id="dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433333244343535383534_-3"]',
                'nationality_select': '//*[@id="IdDocNationality_7E7E303030312D30312D30317E353334423438324433333244343535383534-4"]',
            },
            'contact': {
                'prefix': '//*[@id="phone_prefixPhoneId"]',
                'prefix_select': '//*[@id="phone_prefixPhoneId-1"]',
                'phone': '//*[@id="phone_phoneNumberId"]',
                'email': '//*[@id="email"]',
            },
            'tyc': '//*[@id="sendNewsLetter"]',
            'continue': 'maincontent',
        }

    def get_element(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def get_passenger_element(self, passenger_type, element_type):
        return self.get_element(self.locators[passenger_type][element_type])

    def get_contact_element(self, element_type):
        return self.get_element(self.locators['contact'][element_type])

    def get_tyc_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.locators['tyc']))
        )

    def click_tyc_button(self):
        tyc_button = self.get_tyc_button()
        self.driver.execute_script("arguments[0].click();", tyc_button)

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, self.locators['continue']))
        )

    def click_continue_button(self):
        continue_button = self.get_continue_button()
        self.driver.execute_script("arguments[0].click();", continue_button)