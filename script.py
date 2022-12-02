from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from datetime import timedelta, datetime
import time

tomorrow_datetime = datetime.now() + timedelta(days=1)
# date_text = tomorrow_datetime.strftime('%m/%d/%Y')

from_input = input("Please enter departure station from (Tsawwassen, Horseshoe Bay, Departure Bay, Duke Point, Langdale or Victoria):")
to_options_dict = {
    "Tsawwassen" : ["Victoria", "Nanaimo"],
    "Horseshoe Bay" : ["Departure Bay", "Langdale"],
    "Departure Bay" : ["Horseshoe Bay"],
    "Duke Point" : ["Tsawwassen"],
    "Langdale" : ["Horseshoe Bay"],
    "Victoria" : ["Tsawwassen"]
}
to_options = to_options_dict[from_input]
to_input = input("Please enter arrival station from " + ", ".join(to_options))
date_input = input("Please enter your desired booking date (MM/DD/YYYY):")

print("You are looking to book " + from_input + " to " + to_input + " on " + date_input)
confirmation = input("C to confirm, X to exit")

if (confirmation == "X"):
    sys.exit("Cancelled script")

driver = webdriver.Chrome(executable_path="chromedriver")
driver.get('https://www.bcferries.com/')
driver.get('https://www.bcferries.com/RouteSelectionPage')


from_field = driver.find_element("xpath", '/html/body/main/div[5]/div[2]/div[3]/form/div[1]/div[5]/div[1]/div/h3')
from_field.click()
from_picker = driver.find_element("xpath", "/html/body/main/div[5]/div[2]/div[3]/form/div[1]/div[5]/div[1]/div/div")
from_selections = from_picker.find_elements(By.CLASS_NAME, "bookable")
from_selection = ""
for e in from_selections:
    if from_input in e.text:
        from_selection = e
from_selection.click()
driver.implicitly_wait(5)


to_field = driver.find_element("xpath", '/html/body/main/div[5]/div[2]/div[3]/form/div[1]/div[5]/div[2]/div/h3')
to_field.click()
to_picker = driver.find_element("xpath", "/html/body/main/div[5]/div[2]/div[3]/form/div[1]/div[5]/div[2]/div/div")
to_selections = to_picker.find_elements(By.CLASS_NAME, "bookable")
to_selection = ""
for e in to_selections:
    if to_input in e.text:
        to_selection = e  
to_selection.click()
driver.implicitly_wait(5)

date_picker = driver.find_element("xpath", '/html/body/main/div[5]/div[2]/div[3]/form/div[1]/div[5]/div[11]/div/ul/li[1]/a')
date_input_box = driver.find_element("xpath", '/html/body/main/div[5]/div[2]/div[3]/form/div[1]/div[5]/div[11]/div/div/div[1]/div/input')
date_picker.click()
date_input_box.send_keys(date_input)
submit_dates = driver.find_element("xpath", '/html/body/main/div[5]/div[2]/div[3]/form/div[1]/div[5]/div[12]/button')  
submit_dates.click()


add_adult = driver.find_element("xpath", '/html/body/main/div[5]/div[4]/form/div[3]/div[1]/div[1]/div/div/div[2]/div[1]/div/span[2]/button')  
add_adult.click()
submit_info = driver.find_element("xpath", '/html/body/main/div[5]/div[4]/form/div[16]/div/div[1]/button')  
submit_info.click()


truck_picker = driver.find_element("xpath", '/html/body/main/div[5]/form/div[1]/div[2]/div/div[2]/div[2]/div[3]')  
truck_picker.click()
driver.implicitly_wait(5)
truck_type = driver.find_element("xpath", '/html/body/main/div[5]/form/div[1]/div[2]/div/div[2]/div[2]/div[4]/div[2]/div[1]/div/label/input')  
truck_type.click()
driver.implicitly_wait(5)
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
                                                    # /html/body/main/div[7]/div[4]/div[2]/div/div[3]/div/div/div/div[3]
        time_table = driver.find_element(By.CLASS_NAME, "table-responsive")
        time_cards = time_table.find_elements(By.CLASS_NAME, "p-card")
        times_list = []

        for e in time_cards:
            ferry_time = e.find_element(By.TAG_NAME, "b")
            times_list.append(ferry_time.text)

        time_input = input(f'Please enter a time from these options: {times_list}')

        selected_time = ""
        select_standard = ""
        for e in time_cards:
            ferry_time = e.find_element(By.TAG_NAME, "b")

            if time_input == ferry_time.text:
                selected_time = e.find_element(By.CLASS_NAME, "view-fare-btn")
                select_standard = e.find_element(By.CLASS_NAME, "js-radio-select")
        
        selected_time.click()
        # select_standard = driver.find_element("xpath", '/html/body/main/div[7]/div[5]/div[2]/div/div[3]/div/div/div/div[3]/div[2]/div[3]/div[2]/ul[1]/li/div[1]/div[2]/div/div/div/label')  
        select_standard.click()

        login_link = driver.find_element("xpath", "/html/body/main/div[5]/div/form/div[1]/div[4]/div/div[1]/div[1]/a")
        login_link.click()
        username_field = driver.find_element("xpath", '/html/body/main/div[5]/div/div/div[1]/div[1]/form/div[1]/input')
        password_field = driver.find_element("xpath", '/html/body/main/div[5]/div/div/div[1]/div[1]/form/div[2]/input')
        submit_login = driver.find_element("xpath", '/html/body/main/div[5]/div/div/div[1]/div[1]/form/div[4]/button')  
        username_field.send_keys('melih.u.bal@gmail.com')
        password_field.send_keys('M@plestory1276')
        password_field.send_keys(Keys.RETURN)

        continue_confirm = driver.find_element("xpath", '/html/body/main/div[5]/div/form/div[1]/div[4]/div/div[1]/input')  
        driver.implicitly_wait(2)
        continue_confirm.click()
        
        choose_card = driver.find_element("xpath", '/html/body/main/div[6]/div[1]/div[2]/form/div[2]/div[6]/div/div/div/label/span')  
        choose_card.click()
        policies = driver.find_element("xpath", '/html/body/main/div[6]/div[1]/div[2]/form/div[4]/div[2]/div/div/label/span')  
        policies.click()
        driver.implicitly_wait(2)
        charges = driver.find_element("xpath", '/html/body/main/div[6]/div[1]/div[2]/form/div[5]/label/span')  
        charges.click()
        driver.implicitly_wait(2)
        pay_now = driver.find_element("xpath", '/html/body/main/div[6]/div[1]/div[3]/div/div[2]/button')  
        pay_now.click()

        print("Ferry Booked")
        break
    except NoSuchElementException as err:
        print(err)
        print("No ferries yet")

        time.sleep(10000)

