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
account_btn = driver.find_element_by_id("menu-item-50")
account_btn.click()
name = driver.find_element_by_id("username")
name.send_keys("pochta@yandex.com")
password = driver.find_element_by_id("password")
password.send_keys("sa1np3t3rburg77")
log_btn = driver.find_element_by_css_selector("[value='Login']")
log_btn.click()
shop_btn = driver.find_element_by_id("menu-item-40")
shop_btn.click()
android_btn = driver.find_element_by_class_name("post-169")
android_btn.click()
old = driver.find_element_by_css_selector(".price>del")
old_text = old.text
assert "₹600.00" in old_text
new = driver.find_element_by_css_selector(".price>ins")
new_text = new.text
assert "₹450.00" in new_text
wait = WebDriverWait(driver, 10)
img = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[itemprop='image']")))
img.click()
exit = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
time.sleep(2)
exit.click()
driver.quit()