from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


# get driver
s = Service('~/Desktop/chromedriver') # path to your driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# log in
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
driver.find_element(By.ID, 'txtPassword').send_keys('admin123' + Keys.ENTER)


# Add title

driver.get('https://opensource-demo.orangehrmlive.com/index.php/admin/viewJobTitleList')
driver.find_element(By.ID, 'btnAdd').click()
driver.find_element(By.ID, 'jobTitle_jobTitle').send_keys('some_job_title')
driver.find_element(By.ID, 'jobTitle_jobDescription').send_keys('some_description')
driver.find_element(By.ID, 'jobTitle_note').send_keys('some_note')
driver.find_element(By.ID, 'btnSave').click()




# Check newly added title is visible on the grid

work_row = None
is_found_1 = False
is_found_2 = False

driver.get('https://opensource-demo.orangehrmlive.com/index.php/admin/viewJobTitleList')
table = driver.find_element(By.ID, 'resultTable').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
for tr in table:
    values = list(map(lambda x: x.text, tr.find_elements(By.TAG_NAME, 'td'))) 
    if values[1] == 'some_job_title' and values[2] == 'some_description':
        print("Find. New job was added")
        is_found_1 = True 
        work_row = tr
        break
    
# Edit Description    
if (is_found_1):
    title_field = work_row.find_elements(By.TAG_NAME, 'td')[1].find_element(By.TAG_NAME, 'a').click()
    driver.find_element(By.ID, 'btnSave').click()
    driver.find_element(By.ID, 'jobTitle_jobDescription').clear()
    driver.find_element(By.ID, 'jobTitle_jobDescription').send_keys('new_some_description')
    driver.find_element(By.ID, 'btnSave').click()
else:
    print("Not find. New job was not added")

#  Check that your changes are visible on the Job Title page
driver.get('https://opensource-demo.orangehrmlive.com/index.php/admin/viewJobTitleList')
table = driver.find_element(By.ID, 'resultTable').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
for tr in table:
    values = list(map(lambda x: x.text, tr.find_elements(By.TAG_NAME, 'td'))) 
    if values[1] == 'some_job_title' and values[2] == 'new_some_description':
        print("Find. New job was edited")
        is_found_2 = True 
        work_row = tr
        break


if (is_found_2):
    work_row.find_elements(By.TAG_NAME, 'td')[0].click()
    driver.find_element(By.ID, 'btnDelete').click()
    driver.find_element(By.ID, 'dialogDeleteBtn').click()
else:
    print("Not find. New job was not edited")


    

driver.close()
