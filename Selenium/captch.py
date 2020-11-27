from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Firefox(
    executable_path='F:\py practice\web scrapping\geckodriver-v0.26.0-win64\geckodriver.exe')

extension_dir = 'C:\\Users\\nagen\AppData\\Roaming\Mozilla\\Firefox\Profiles\\0dl5q87c.default-release-1584633775795\\extensions\\'
extensions = [
    '{e58d3966-3d76-4cd9-8552-1582fbc800c1}.xpi',
]

for extension in extensions:
    driver.install_addon(extension_dir + extension, temporary=True)

driver.get("https://erp.aktu.ac.in/webpages/oneview/oneview.aspx")
elem_captch = driver.find_element_by_css_selector('#pnlCaptcha')
elem_captch.click()
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
    (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/bframe']")))


# WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
#     (By.CSS_SELECTOR, "#recaptcha-anchor"))).click()
print('----------------------------')
driver.switch_to.default_content()
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
    (By.CSS_SELECTOR, "iframe[title='recaptcha challenge']")))
time.sleep(5)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button#solver-button"))).click()
