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
book_btn = driver.find_element_by_css_selector("[data-product_id='182']")
book_btn.click()
time.sleep(2)
price = driver.find_element_by_class_name("wpmenucart-contents")
price_text = price.text
assert "1 Item" in price_text
assert "₹180.00" in price_text
cart = driver.find_element_by_class_name("wpmenucart-contents")
cart.click()
wait = WebDriverWait(driver, 10)
subtotal = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal']"), "₹180.00"))
total = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Total']:nth-child(2)"), "₹189.00"))
driver.quit()