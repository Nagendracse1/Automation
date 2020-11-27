from selenium import webdriver

browser = webdriver.Firefox(
    executable_path='F:\py practice\web scrapping\geckodriver-v0.26.0-win64\geckodriver.exe')


extension_dir = 'C:\\Users\\nagen\AppData\\Roaming\Mozilla\\Firefox\Profiles\\0dl5q87c.default-release-1584633775795\\extensions\\'
extensions = [
    '{e58d3966-3d76-4cd9-8552-1582fbc800c1}.xpi',
]

for extension in extensions:
    browser.install_addon(extension_dir + extension, temporary=True)

browser.get('https://erp.aktu.ac.in/webpages/oneview/oneview.aspx')

for i in range(1709710070,1709710071):
    elem_fill = browser.find_element_by_css_selector('#txtRollNo')
    elem_fill.send_keys('1709710070')
    elem_captch = browser.find_element_by_css_selector(
        '#pnlCaptcha')
    elem_captch.click()
    elem_buster = browser.find_element_by_css_selector('#solver-button')
