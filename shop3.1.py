from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
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
sort_order = driver.find_element_by_class_name("orderby")
sort_order_selected = sort_order.get_attribute("value")
print("value of sort order select: ", sort_order_selected)
if sort_order_selected is not None:
    print("Сортировка по умолчанию")
else:
    print("Ошибка сортировки")
element = driver.find_element_by_class_name("orderby")
select = Select(element)
select.select_by_value("price-desc")
sort_order = driver.find_element_by_class_name("orderby")
sort_order_selected = sort_order.get_attribute("value")
print("value of sort order select: ", sort_order_selected)
if sort_order_selected is not None:
    print("Сортировка цены по убыванию")
else:
    print("Ошибка сортировки")
    driver.quit()