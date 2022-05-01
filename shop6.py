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
driver.execute_script("window.scrollBy(0, 300);")
book2_btn = driver.find_element_by_css_selector("[data-product_id='180']")
book2_btn.click()
cart = driver.find_element_by_class_name("wpmenucart-contents")
cart.click()
remove_btn = driver.find_element_by_css_selector(".product-remove>[data-product_id='182']")
time.sleep(3)
remove_btn.click()
wait = WebDriverWait(driver, 10)
undo_btn = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-message>a")))
undo_btn.click()
qty = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
qty.clear()
qty.send_keys(3)
update_btn = driver.find_element_by_name("update_cart")
update_btn.click()
quantity = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
quantity_attribute = quantity.get_attribute("value")
assert quantity_attribute == "3"
time.sleep(3)
coupon_btn = driver.find_element_by_name("apply_coupon")
coupon_btn.click()
woocommerce = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error"), "Please enter a coupon code."))
print(woocommerce)
driver.quit()