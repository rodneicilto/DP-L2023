from selenium import webdriver
import pandas as pd

import time

vulnerability = input ('Insert your Vulnerability topic: ')

browser = webdriver.Chrome()
link = f'https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query={vulnerability}&search_type=all&isCpeNameSearch=false'
browser.get(link)
cve_head = browser.find_element('xpath', '/html/body/main/div/div/div[2]/div/div[2]/table/tbody/tr[1]/th/strong/a').text
cve_details = browser.find_element('xpath', '/html/body/main/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/p').text
print('Data Returned......')
print('Software/Sistem: ', vulnerability)
print('CVE: ', cve_head)
print('Current Description: ', cve_details)
time.sleep(10)

browser.quit()