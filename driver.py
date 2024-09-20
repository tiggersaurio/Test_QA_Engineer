from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Usar ChromeDriverManager para descargar y usar automáticamente el ChromeDriver correcto
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Abrir la página web
driver.get("https://nuxqa6.avtest.ink/es/")

# Esperar y hacer clic en el botón de idioma
language_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.dropdown_trigger.dropdown_trigger--active')))
language_button.click()

# Esperar y hacer clic en la opción de idioma deseada (por ejemplo, inglés)
languageEn_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'options-list_item_option') and contains(., 'English')]")))
languageEn_option.click()

# Esperar y hacer clic en el botón país
country_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.point-of-sale-selector_button')))
country_button.click()

# Esperar y hacer clic en el país deseado
country_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pointOfSaleListId"]/li[5]/button/span[1]')))
country_option.click()



# Aplicar
apply_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.points-of-sale_footer_action_button')))
apply_button.click()


# Seleccionar "solo ida"
# Esperar a que el contenedor de los radio buttons esté presente
container = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//journey-type-control-custom")))    
oneway_radio = container.find_element(By.XPATH, ".//input[@type='radio' and (@value='oneway' or @id='journeytypeId_1')]")
driver.execute_script("arguments[0].click();", oneway_radio)

# Ingresar destino de origen 
origin_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#originBtn.control_field_button")))
origin_button.click()
origin_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.control_field_input")))
origin_input.send_keys("Vancouver")
origin_input.send_keys(Keys.TAB)

time.sleep(4)

#ingrear destino
destination_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "BOG")))
destination_select.click()

#Seleccionar pasajeros
pass_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchContentId_OW"]/div[3]/pax-control-custom/div/div/div[2]/div/button')))
pass_select.click()

passTeen_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="paxControlSearchId"]/div/div[2]/div[1]/ul/li[2]/div[2]/ibe-minus-plus/div/button[2]')))
passTeen_button.click()

passChild_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="paxControlSearchId"]/div/div[2]/div[1]/ul/li[3]/div[2]/ibe-minus-plus/div/button[2]')))
passChild_button.click()

passInfant_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="paxControlSearchId"]/div/div[2]/div[1]/ul/li[4]/div[2]/ibe-minus-plus/div/button[2]')))
passInfant_button.click()

#buscar
search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
search_button.click()


# Mantener el navegador abierto
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Cerrando el navegador...")
    driver.quit()