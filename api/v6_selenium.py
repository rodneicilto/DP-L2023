import os
import time
import pandas as pd
from send_email import send
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

if os.path.exists("Vulnerability.xls"):
   os.remove("Vulnerability.xls")
   table = pd.DataFrame({'Software/System': [], 'CVE': [], 'Current Description': [], 'Severity': [], 'References': [], 'Afected Software': [], 'NVD Date': [], 'Link to Issue': [] })
   spreadsheet_writer = pd.ExcelWriter('Vulnerability.xls', engine='xlsxwriter')
   table.to_excel(spreadsheet_writer, index=False)
   spreadsheet_writer.close()
else:
    table = pd.DataFrame({'Software/System': [], 'CVE': [], 'Current Description': [], 'Severity': [], 'References': [], 'Afected Software': [], 'NVD Date': [], 'Link to Issue': [] })
    spreadsheet_writer = pd.ExcelWriter('Vulnerability.xls', engine='xlsxwriter')
    table.to_excel(spreadsheet_writer, index=False)
    spreadsheet_writer.close()
  
#vulnerability = input ('Insert your Vulnerability topic: ')
vulnerability = 'Android'
#initial_date = input ('Put the initial date to search (MM/DD/YYYY)')
initial_date = '03/01/2023'
#final_date = input ('Put the final date to search (MM/DD/YYYY)')
final_date = '05/27/2023'

try:
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    browser = webdriver.Chrome(options=op)
    #browser.maximize_window()
    #browser.minimize_window()

    browser.get('https://nvd.nist.gov/vuln/search')
    link = browser.find_element(By.ID, 'Keywords').send_keys(vulnerability)
    search_type = browser.find_element(By.ID, 'SearchTypeAdvanced').click()
    start_date_range = browser.find_element(By.ID, 'published-start-date').send_keys(initial_date)
    end_date_range = browser.find_element(By.ID, 'published-end-date').send_keys(final_date)
    browser.find_element('xpath', '//*[@id="vuln-search-submit"]').click()

    for i in range(1,11):
        i_as_string = str(i)
        browser.find_element('xpath', '/html/body/main/div/div/div[2]/div/div[2]/table/tbody/tr['+i_as_string+']/th/strong/a').click()
        vuln_researched = vulnerability
        vuln_id = browser.find_element('xpath', '/html/body/main/div/div/div[2]/div[2]/table/tbody/tr/td/div/div[2]/div/a').text
        vuln_description = browser.find_element('xpath', '/html/body/main/div/div/div[2]/div[2]/table/tbody/tr/td/div/div[1]/p').text

        try:
            vuln_severity = browser.find_element(By.ID, 'Cvss3NistCalculatorAnchor').text

        except:

            vuln_severity = browser.find_element(By.ID, 'Cvss3NistCalculatorAnchorNA').text

        vuln_reference = browser.find_element(By.CLASS_NAME, 'external').text

        try:

            vuln_affected = browser.find_element(By.TAG_NAME, 'b').text

        except:
            vuln_affected = ('No Software was informed related to this issue')
    
        vuln_date = browser.find_element('xpath', '/html/body/main/div/div/div[2]/div[2]/table/tbody/tr/td/div/div[2]/div/span[1]').text
        vuln_link = f'https://nvd.nist.gov/vuln/detail/{vuln_id}'

        print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
        print('')
        print('Data Returned......')
        print('Software/Sistem: ', vulnerability)
        print('CVE: ', vuln_id)
        print('Current Description: ', vuln_description)
        print('Severity: ', vuln_severity)
        print('References: ', vuln_reference)
        print('Affected Software: ', vuln_affected)
        print('NVD Date: ', vuln_date)
        print('Link to Issue: ', vuln_link)
        print('')
        print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

        table = pd.DataFrame({'Software/System': [vulnerability], 'CVE': [vuln_id], 'Current Description': [vuln_description], 'Severity': [vuln_severity], 'References': [vuln_reference], 'Afected Software': [vuln_affected], 'NVD Date': [vuln_date], 'Link to Issue': [vuln_link] })
        reader = pd.read_excel('Vulnerability.xls')
        writer = pd.ExcelWriter('Vulnerability.xls', engine='openpyxl', mode='a', if_sheet_exists="overlay")
        table.to_excel(writer, index=False, header=False, startrow=len(reader) + 1)
        writer.close()

        browser.back()

    time.sleep(10)

    browser.quit()
    send()

except:
    print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
    print('')
    print('No Data was Found with parameters provided')
    print('Topic NOT Found: ', vulnerability)
    print('')
    print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
    send()
