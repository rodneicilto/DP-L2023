import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

browser = Chrome()

browser.get('https://nvd.nist.gov/vuln/detail/CVE-2023-27382')

try:
    name = browser.find_element(By.ID, 'Cvss3NistCalculatorAnchor').text
    id_name = browser.find_element('xpath', '//*[@id="Cvss3NistCalculatorAnchor"]').text

except:

    name = browser.find_element(By.ID, 'Cvss3NistCalculatorAnchorNA').text
    id_name = browser.find_element('xpath', '//*[@id="Cvss3NistCalculatorAnchorNA"]').text

print(name)
print(id_name)


df = pd.DataFrame({'Variable Name': [name], 'Variable ID': [id_name]})
spreadsheet_writer = pd.ExcelWriter('SampleTable.xls', engine='xlsxwriter')
df.to_excel(spreadsheet_writer, sheet_name='Vulnerability', index=False)
spreadsheet_writer.close()

"""
//*[@id="Cvss3NistCalculatorAnchorNA"]
//*[@id="Cvss3NistCalculatorAnchorNA"]
//*[@id="Cvss3NistCalculatorAnchorNA"]
//*[@id="Cvss3NistCalculatorAnchor"]

#config-div-1 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > b:nth-child(1)
.vulnerable > td:nth-child(1) > b:nth-child(1)
"""