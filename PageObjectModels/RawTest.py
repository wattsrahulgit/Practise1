from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:\\Code\PythonTestingSelenium\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
driver.implicitly_wait(10)
driver.maximize_window()
action = ActionChains(driver)

driver.find_element_by_link_text("Computers").click()
driver.find_element_by_link_text("Desktops").click()
driver.find_element_by_css_selector("#products-orderby").click()
dropdown = driver.find_elements_by_css_selector("[id='products-orderby'] option")

dropdown[3].click()

bottom_of_page = driver.find_element_by_css_selector("[class='column customer-service']")
action.move_to_element(bottom_of_page).perform()

driver.find_element_by_link_text("Build your own expensive computer").click()
assert driver.find_element_by_css_selector("[class='free-shipping']").is_displayed()

driver.find_element_by_css_selector("#small-searchterms").send_keys(Keys.PAGE_DOWN)

radioButtons = driver.find_elements_by_css_selector("input[type='radio']")
radioButtons[2].click()
radioButtons[5].click()
radioButtons[7].click()

checkBox = driver.find_elements_by_css_selector("input[type='checkbox']")
checkBox[2].click()

driver.find_element_by_css_selector("#addtocart_74_EnteredQuantity").clear()
driver.find_element_by_css_selector("#addtocart_74_EnteredQuantity").send_keys("4")
driver.find_element_by_xpath("//input[@class='button-1 add-to-cart-button']").click()
time.sleep(3)
driver.execute_script("window.scrollTo(0, 0)")
driver.find_element_by_css_selector(".cart-qty").click()

applyCoupan = driver.find_element_by_css_selector("[name='applydiscountcouponcode']")
driver.execute_script('arguments[0].scrollIntoView(true);', applyCoupan)

country = Select(driver.find_element_by_id("CountryId"))
country.select_by_value("2")

state = Select(driver.find_element_by_id("StateProvinceId"))
state.select_by_visible_text("British Columbia")

driver.find_element_by_name("estimateshipping").click()

commonButtons = driver.find_element_by_css_selector(".common-buttons")
commonButtons.location_once_scrolled_into_view

driver.find_element_by_id("termsofservice").click()
driver.find_element_by_id("checkout").click()
