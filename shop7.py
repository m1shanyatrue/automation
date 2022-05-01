from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
path_to_extension = r'C:\Users\U\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.46.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
time.sleep(10)
window_adblock = driver.window_handles[1]
driver.switch_to.window(window_adblock)
driver.close()
window = driver.window_handles[0]
driver.switch_to.window(window)
driver.maximize_window()
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://practice.automationtesting.in/")
shop_btn = driver.find_element_by_id("menu-item-40")
shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
book1_btn = driver.find_element_by_css_selector("[data-product_id='182']")
book1_btn.click()
time.sleep(3)
wait = WebDriverWait(driver, 10)
cart = driver.find_element_by_class_name("wpmenucart-contents")
cart.click()
check_btn = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
check_btn.click()
firstname = wait.until(
    EC.presence_of_element_located((By.ID, "billing_first_name")))
firstname.send_keys("Admin")
lastname = driver.find_element_by_id("billing_last_name")
lastname.send_keys("Admin1")
email = driver.find_element_by_id("billing_email")
email.send_keys("admin@email.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("1234567890")
country_btn = driver.find_element_by_id("s2id_billing_country")
country_btn.click()
country_search = driver.find_element_by_id("s2id_autogen1_search")
country_search.send_keys("Russ")
country_select = driver.find_element_by_class_name("select2-result-label")
country_select.click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("address")
city = driver.find_element_by_id("billing_city")
city.send_keys("City")
state = driver.find_element_by_id("billing_state")
state.send_keys("State")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("Postcode")
driver.execute_script("window.scrollBy(0, 600);")
payment_btn = driver.find_element_by_id("payment_method_cheque")
payment_btn.click()
time.sleep(3)
place_btn = driver.find_element_by_id("place_order")
place_btn.click()
head_text = wait.until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
payment_text = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr:nth-child(3)>td"), "Check Payments"))
driver.quit()