# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\Fuad\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.17.1_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(10)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("https://practice.automationtesting.in/")
# time.sleep(5)
#
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
#
# Email = driver.find_element_by_id("reg_email")
# Email.send_keys("ExampleMail@gmail.com")
#
# password = driver.find_element_by_id("reg_password")
# password.send_keys("SuperMegaPass")
#
# register = driver.find_element_by_class_name("woocomerce-FormRow.form-row .woocommerce-Button.button")
# register.click()
#
# driver.quit()







# 22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222



# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\Fuad\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.17.1_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(10)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("https://practice.automationtesting.in/")
# time.sleep(5)
#
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
#
# username = driver.find_element_by_id("username")
# username.send_keys("ExampleMail@gmail.com")
#
# password = driver.find_element_by_id("password")
# password.send_keys("SuperMegaPass")
#
# login = driver.find_element_by_class_name("form-row .woocommerce-Button.button")
# login.click()
#
# logout = driver.find_element_by_class_name("woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout")
#
# assert logout.is_displayed()
#
# driver.quit()
#
