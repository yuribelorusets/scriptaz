from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from datetime import timedelta, datetime
import time

tomorrow_datetime = datetime.now() + timedelta(days=1)


driver = webdriver.Chrome(executable_path="/mnt/c/users/admin/downloads/chromedriver")

from_input = input("Please enter departure station:")
to_input = input("Please enter arrival station:")

print("You are looking to book " + from_input + " to " + to_input)
confirmation = input("C to confirm, X to exit")

if (confirmation == "X"):
 sys.exit("Cancelled script")

driver.get('https://www.bcferries.com/login')

username_field = driver.find_element("xpath", '/html/body/main/div[5]/div/div/div[1]/div[1]/form/div[1]/input')
password_field = driver.find_element("xpath", '/html/body/main/div[5]/div/div/div[1]/div[1]/form/div[2]/input')
submit_login = driver.find_element("xpath", '/html/body/main/div[5]/div/div/div[1]/div[1]/form/div[4]/button')  
username_field.send_keys('melih.u.bal@gmail.com')
password_field.send_keys('M@plestory1276')
password_field.send_keys(Keys.RETURN)

driver.get('https://www.bcferries.com/RouteSelectionPage')

from_field = driver.find_element("xpath", '/html/body/main/div[5]/div[2]/div[3]/form/div[1]/div[5]/div[1]/div/h3')
tswawassen = driver.find_element("xpath", '/html/body/main/div[5]/div[2]/div[3]/form/div[1]/div[5]/div[1]/div/div/div/ul[1]/li[1]/a')

date_picker = driver.find_element("xpath", '/html/body/main/div[5]/div[2]/div[3]/form/div[1]/div[5]/div[11]/div/ul/li[1]/a')
date_input = driver.find_element("xpath", '/html/body/main/div[5]/div[2]/div[3]/form/div[1]/div[5]/div[11]/div/div/div[1]/div/input')
date_text = tomorrow_datetime.strftime('%m/%d/%Y')

from_field.click()
tswawassen.click()
driver.implicitly_wait(5)
date_picker.click()
date_input.send_keys(date_text)
driver.implicitly_wait(5)
to_field = driver.find_element("xpath", '/html/body/main/div[5]/div[2]/div[3]/form/div[1]/div[5]/div[2]/div/h3')
nanaimo = driver.find_element("xpath", '/html/body/main/div[5]/div[2]/div[3]/form/div[1]/div[5]/div[2]/div/div/div/ul[1]/li[2]/a')
to_field.click()
nanaimo.click()
submit_dates = driver.find_element("xpath", '/html/body/main/div[5]/div[2]/div[3]/form/div[1]/div[5]/div[12]/button')  
submit_dates.click()


add_adult = driver.find_element("xpath", '/html/body/main/div[5]/div[4]/form/div[3]/div[1]/div[1]/div/div/div[2]/div[1]/div/span[2]/button')  
add_adult.click()
submit_info = driver.find_element("xpath", '/html/body/main/div[5]/div[4]/form/div[15]/div/div[1]/button')  
submit_info.click()


truck_picker = driver.find_element("xpath", '/html/body/main/div[5]/form/div[1]/div[2]/div/div[2]/div[2]/div[3]')  
truck_picker.click()
truck_type = driver.find_element("xpath", '/html/body/main/div[5]/form/div[1]/div[2]/div/div[2]/div[2]/div[4]/div[2]/div[1]/div/label/input')  
truck_type.click()
truck_width_radio = driver.find_element("xpath", '/html/body/main/div[5]/form/div[1]/div[2]/div/div[2]/div[2]/div[4]/div[3]/div[1]/div/div[1]/div/label/input')  
truck_width_radio.click()
truck_length = driver.find_element("xpath", '/html/body/main/div[5]/form/div[1]/div[2]/div/div[2]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div[1]/input')  
truck_length.send_keys('31')
truck_height = driver.find_element("xpath", '/html/body/main/div[5]/form/div[1]/div[2]/div/div[2]/div[2]/div[4]/div[3]/div[2]/div[1]/div[3]/div/div[1]/div[1]/input')  
truck_height.send_keys('12')
submit_truck = driver.find_element("xpath", '/html/body/main/div[5]/form/div[3]/div/div/button')  
submit_truck.click()

while (True) :
    try:
        driver.refresh()
        driver.implicitly_wait(3)
        # time_select = driver.find_element("xpath", '/html/body/main/div[7]/div[5]/div[2]/div/div[3]/div/div/div/div[3]/div[3]/div[2]/div/div/div[3]/button[1]')  
        # time_select.click()
        # select_standard = driver.find_element("xpath", '/html/body/main/div[7]/div[5]/div[2]/div/div[3]/div/div/div/div[3]/div[3]/div[3]/div[2]/ul[1]/li/div[1]/div[2]/div/div/div/label')  
        # select_standard.click()
        time_select = driver.find_element("xpath", '/html/body/main/div[7]/div[5]/div[2]/div/div[3]/div/div/div/div[3]/div[2]/div[2]/div/div/div[3]/button[1]')  
        time_select.click()
        select_standard = driver.find_element("xpath", '/html/body/main/div[7]/div[5]/div[2]/div/div[3]/div/div/div/div[3]/div[2]/div[3]/div[2]/ul[1]/li/div[1]/div[2]/div/div/div/label')  
        select_standard.click()

        continue_confirm = driver.find_element("xpath", '/html/body/main/div[5]/div/form/div[1]/div[2]/div[2]/div[1]/input')  
        continue_confirm.click()
        
        choose_card = driver.find_element("xpath", '/html/body/main/div[6]/div[1]/div[2]/form/div[2]/div[6]/div/div/div/label/span')  
        choose_card.click()
        policies = driver.find_element("xpath", '/html/body/main/div[6]/div[1]/div[2]/form/div[4]/div[2]/div/div/label/span')  
        policies.click()
        driver.implicitly_wait(2)
        charges = driver.find_element("xpath", '/html/body/main/div[6]/div[1]/div[2]/form/div[5]/label/span')  
        charges.click()
        pay_now = driver.find_element("xpath", '/html/body/main/div[6]/div[1]/div[3]/div/div[2]/button')  
        pay_now.click()

        print("Ferry Booked")
        break
    except NoSuchElementException:
        print("No ferries yet")

        time.sleep(10)

