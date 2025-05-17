from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_for_cart_button(browser):
    browser.get(link)
    add_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-lg")))
