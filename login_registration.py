from selenium import webdriver
import time
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
reg_email = driver.find_element_by_id("reg_email")
reg_email.send_keys("pochta@yandex.com")
reg_password = driver.find_element_by_id("reg_password")
time.sleep(5)
reg_password.send_keys("sa1np3t3rburg77")
reg_btn = driver.find_element_by_css_selector("[value='Register']")
reg_btn.click()
time.sleep(5)
driver.quit()