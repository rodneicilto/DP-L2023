from selenium import webdriver
from selenium.webdriver.common.by import By

import time

vulnerability = input ('Insert your Vulnerability topic: ')

browser = webdriver.Chrome()
issue_link = f'https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query={vulnerability}&search_type=all&isCpeNameSearch=false'
browser.get(issue_link)
browser.find_element('xpath', '/html/body/main/div/div/div[2]/div/div[2]/table/tbody/tr[1]/th/strong/a').click()


#variables to get information related to spreadsheet creation
vuln_researched = vulnerability
vuln_id = browser.find_element('xpath', '/html/body/main/div/div/div[2]/div[2]/table/tbody/tr/td/div/div[2]/div/a').text
vuln_description = browser.find_element('xpath', '/html/body/main/div/div/div[2]/div[2]/table/tbody/tr/td/div/div[1]/p').text
#vuln_severity = browser.find_element(By.ID, 'Cvss3NistCalculatorAnchor').text
try:
    vuln_severity = browser.find_element(By.ID, 'Cvss3NistCalculatorAnchor').text
    #vuln_severity = browser.find_element('xpath', '//*[@id="Cvss3NistCalculatorAnchor"]').text

except:

    vuln_severity = browser.find_element(By.ID, 'Cvss3NistCalculatorAnchorNA').text
    #vuln_severity = browser.find_element('xpath', '//*[@id="Cvss3NistCalculatorAnchorNA"]').text

#vuln_reference = browser.find_element('xpath', '/html/body/main/div/div/div[2]/div[2]/table/tbody/tr/td/div/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[1]/a').text
vuln_reference = browser.find_element(By.CLASS_NAME, 'external').text
#vuln_affected = browser.find_element('xpath', '/html/body/main/div/div/div[2]/div[2]/table/tbody/tr/td/div/div[1]/div[2]/div[3]/div/div[2]/div/table/tbody/tr[1]/td[1]/b').text
try:

    vuln_affected = browser.find_element(By.TAG_NAME, 'b').text

except:
    vuln_affected = ('No Software was informed related to this issue')
    
vuln_date = browser.find_element('xpath', '/html/body/main/div/div/div[2]/div[2]/table/tbody/tr/td/div/div[2]/div/span[1]').text
vuln_link = f'https://nvd.nist.gov/vuln/detail/{vuln_id}'

print('Data Returned......')
print('Software/Sistem: ', vulnerability)
print('CVE: ', vuln_id)
print('Current Description: ', vuln_description)
print('Severity: ', vuln_severity)
print('References: ', vuln_reference)
print('Affected Software: ', vuln_affected)
print('NVD Date: ', vuln_date)
print('Link to Issue: ', vuln_link)

time.sleep(10)

browser.quit()