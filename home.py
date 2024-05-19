# 1111111111111111111111111111111111111111111111111111111111111111111

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
# driver.execute_script("window.scrollBy(0, 600);")
#
# book = driver.find_element_by_id("text-22-sub_row_1-0-2-0-0")
# book.click()
#
# driver.execute_script("window.scrollBy(0, 600);")
#
# reviews = driver.find_element_by_class_name("reviews_tab")
# reviews.click()
#
# stars_5 = driver.find_element_by_class_name("star-5")
# stars_5.click()
#
# comment = driver.find_element_by_id("comment")
# comment.send_keys("Nice book!")
#
# name = driver.find_element_by_id("author")
# name.send_keys("Fuad")
#
# email = driver.find_element_by_id("email")
# email.send_keys("example@gmail.com")
#
# submit = driver.find_element_by_id("submit")
# submit.click()
#
# driver.quit()



