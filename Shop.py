# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\Fuad\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.19.1_0'
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
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
#
# driver.execute_script("window.scrollBy(0, 400);")
#
# book = driver.find_element_by_class_name("post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.taxable.shipping-taxable.purchasable.product-type-simple .woocommerce-LoopProduct-link")
# book.click()
#
# tittle = driver.find_element_by_class_name("product_title.entry-title")
#
# assert tittle.text == "HTML5 Forms"
#
# driver.quit()
#
#
#
# 22222222222222222222222222222222222222222222222222222222222222222222222222
#
#
# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\Fuad\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.19.1_0'
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
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
#
# html_count_1 = driver.find_element_by_class_name("cat-item.cat-item-19 .count")
# assert  html_count_1.text == "(3)"
#
# html_category = driver.find_element_by_link_text("HTML")
# html_category.click()
#
#
# bookCount = driver.find_elements_by_class_name("product.type-product")
# assert len(bookCount) == 3
#
# driver.quit()
#
#
# 3333333333333333333333333333333333333333333333333333333333333333333
#
#
# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\Fuad\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.19.1_0'
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
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
#
# driver.execute_script("window.scrollBy(0, 200);")
#
#
# selector_menu = driver.find_element_by_class_name("woocommerce-ordering .orderby")
# selector_menu_selected = driver.find_element_by_class_name("woocommerce-ordering .orderby [selected=selected]")
# value = selector_menu_selected.get_attribute("value")
#
# assert value == "menu_order"
#
#
# select = Select(selector_menu)
# select.select_by_value("price-desc")
#
# selector_menu_selected = driver.find_element_by_class_name("woocommerce-ordering .orderby [selected=selected]")
# value = selector_menu_selected.get_attribute("value")
#
# assert value == "price-desc"
#
# driver.quit()
#
#
# 44444444444444444444444444444444444444444444444444444444
#
#
#
# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\Fuad\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.19.1_0'
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
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
#
# driver.execute_script("window.scrollBy(0, 200);")
#
# book = driver.find_element_by_class_name("post-169.product.type-product.status-publish.product_cat-android.product_tag-android.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.instock.sale.downloadable.taxable.shipping-taxable.purchasable.product-type-simple .attachment-shop_catalog.size-shop_catalog.wp-post-image")
# book.click()
#
# old_price = driver.find_element_by_css_selector("del span.woocommerce-Price-amount.amount")
# assert old_price.text == "₹600.00"
# new_price = driver.find_element_by_css_selector("ins span.woocommerce-Price-amount.amount")
# assert new_price.text == "₹450.00"
#
# wait = WebDriverWait(driver, 10)
#
# image = driver.find_element_by_class_name("attachment-shop_single.size-shop_single.wp-post-image")
# waiting_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "attachment-shop_single.size-shop_single.wp-post-image")))
# image.click()
#
# close = driver.find_element_by_class_name("pp_close")
# waiting_2 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# close.click()
#
# driver.quit()
#
#
# 555555555555555555555555555555555555555555555555555555555555555555555555555
#
#
# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\Fuad\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.19.1_0'
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
#
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
#
# driver.execute_script("window.scrollBy(0, 800);")
#
# add_to_cart = driver.find_element_by_class_name("post-182 .ajax_add_to_cart")
# add_to_cart.click()
#
# time.sleep(5)
# item_count = driver.find_element_by_class_name("cartcontents")
# assert item_count.text == "1 Item"
# price = driver.find_element_by_class_name("wpmenucart-contents .amount")
# assert price.text == "₹180.00"
#
# cart = driver.find_element_by_class_name("wpmenucart-contents")
# cart.click()
#
# wait = WebDriverWait(driver,10)
# waiting_1 = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-subtotal .amount")))
# waiting_2 = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "order-total .amount")))
#
# driver.quit()
#
#
# 666666666666666666666666666666666666666666666666666666666666666666666666666666666
#
#
# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\Fuad\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.19.1_0'
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
# wait = WebDriverWait(driver, 10)
#
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
#
# driver.execute_script("window.scrollBy(0, 600);")
#
# add_to_cart_1 = driver.find_element_by_class_name("post-182 .ajax_add_to_cart")
# add_to_cart_1.click()
#
# time.sleep(3)
# driver.execute_script("window.scrollBy(0, 500);")
#
# add_to_cart_2 = driver.find_element_by_class_name("post-180 .ajax_add_to_cart")
# add_to_cart_2.click()
#
# time.sleep(3)
#
# cart = driver.find_element_by_class_name("wpmenucart-contents")
# cart.click()
#
#
# time.sleep(3)
#
# delete = driver.find_element_by_css_selector(".product-remove>[data-product_id='182']")
# delete.click()
#
# undo = driver.find_element_by_css_selector("div.woocommerce-message > a")
# undo.click()
#
# increase_count_to_3 = driver.find_element_by_css_selector(".quantity > [name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
# increase_count_to_3.clear()
# increase_count_to_3.send_keys(3)
#
# update = driver.find_element_by_css_selector(".actions [name=update_cart]")
# update.click()
#
#
# increase_count_to_3 = driver.find_element_by_css_selector(".quantity > [name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
# value = increase_count_to_3.get_attribute("value")
# assert value == "3"
#
#
# time.sleep(3)
# coupon = driver.find_element_by_css_selector(".actions [name=apply_coupon]")
# coupon.click()
#
# error = driver.find_element_by_class_name("woocommerce-error")
# error_wait = wait.until(EC.visibility_of_element_located(
#     (By.CLASS_NAME, "woocommerce-error")
# ))
#
# driver.quit()
#
#
# 77777777777777777777777777777777777777777777777777777777777777777777777777777
#
# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'C:\Users\Fuad\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.19.1_0'
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
# wait = WebDriverWait(driver, 10)
#
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
#
# driver.execute_script("window.scrollBy(0, 800);")
#
# add_to_cart = driver.find_element_by_class_name("post-182 .ajax_add_to_cart")
# add_to_cart.click()
#
# time.sleep(3)
#
# cart = driver.find_element_by_class_name("wpmenucartli.wpmenucart-display-standard.menu-item")
# cart.click()
#
# driver.execute_script("window.scrollBy(0, 400);")
#
# checkout_wait = wait.until(EC.element_to_be_clickable(
#     (By.CLASS_NAME,"checkout-button.button.alt.wc-forward")
# ))
#
# checkout = driver.find_element_by_class_name("checkout-button.button.alt.wc-forward")
# checkout.click()
#
# wait_name = wait.until(EC.visibility_of_element_located(
#     (By.ID,"billing_first_name")
# ))
#
# name = driver.find_element_by_id("billing_first_name")
# name.send_keys("Anton")
#
# surname = driver.find_element_by_id("billing_last_name")
# surname.send_keys("Kireev")
#
# Email = driver.find_element_by_id("billing_email")
# Email.send_keys("anton123@gmail.com")
#
# phone = driver.find_element_by_id("billing_phone")
# phone.send_keys("+9913454312")
#
# driver.execute_script("window.scrollBy(0, 300);")
# driver.implicitly_wait(5)
#
# country = driver.find_element_by_id("s2id_billing_country")
# country.click()
#
# country_serch = driver.find_element_by_id("s2id_autogen1_search")
# country_serch.send_keys("Haiti")
#
# driver.implicitly_wait(5)
#
# Haiti = driver.find_element_by_class_name("select2-results .select2-result-label")
# Haiti.click()
#
# adress = driver.find_element_by_id("billing_address_1")
# adress.send_keys("Kitayskaya street 99")
#
# driver.execute_script("window.scrollBy(0, 300);")
#
# driver.implicitly_wait(5)
#
# city = driver.find_element_by_id("billing_city")
# city.send_keys("Almati")
#
# state = driver.find_element_by_id("billing_state")
# state.send_keys("Kinea")
#
# zipcode = driver.find_element_by_id("billing_postcode")
# zipcode.send_keys("338")
#
# driver.execute_script("window.scrollBy(0, 300);")
# driver.implicitly_wait(5)
#
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(3)
# Check_payment = driver.find_element_by_id("payment_method_cheque")
# Check_payment.click()
#
# order = driver.find_element_by_id("place_order")
# order.click()
#
# thanks_wait = wait.until(EC.text_to_be_present_in_element(
#     (By.CLASS_NAME, "woocommerce-thankyou-order-received"), ("Thank you. Your order has been received.")
# ))
#
# metod_wait = wait.until(EC.text_to_be_present_in_element(
#     (By.CLASS_NAME, "method"), ("Check Payments")
# ))
#
# driver.quit()
