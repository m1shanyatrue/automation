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
driver.execute_script("window.scrollBy(0, 900);")
read_btn = driver.find_element_by_css_selector("[data-product_id='160']")
read_btn.click()
driver.execute_script("window.scrollBy(0, 400);")
reviews_btn = driver.find_element_by_css_selector("[href='#tab-reviews']")
reviews_btn.click()
driver.execute_script("window.scrollBy(0, 600);")
star_btn = driver.find_element_by_css_selector(".star-5")
star_btn.click()
comm = driver.find_element_by_id("comment")
comm.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Admin")
email = driver.find_element_by_id("email")
email.send_keys("admin@admin.com")
submit_btn = driver.find_element_by_id("submit")
submit_btn.click()
time.sleep(5)
driver.quit()