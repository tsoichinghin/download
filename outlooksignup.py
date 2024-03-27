from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random
import os
import csv
import requests

def get_current_ip():
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
        else:
            print("Failed to retrieve IP:", response.status_code)
    except Exception as e:
        print("Error occurred while retrieving IP:", str(e))

def countdown(seconds):
    for i in range(seconds, -1, -1):
        if i > 0:
            print(f"\rTime remaining: {i} seconds", end="", flush=True)
        else:
            print("\rTime remaining: 0 seconds", end="", flush=True)
        time.sleep(1)
    print("\n")

def random_email():
    min_length = 10
    max_length = 15

    length = random.randint(min_length, max_length)

    lowercase_characters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    characters = lowercase_characters + uppercase_characters
    username = ''
    for _ in range(length):
        random_index = random.randint(0, len(characters) - 1)
        username += characters[random_index]
    result = username + '@outlook.com'
    return result

def random_pw():
    min_length = 10
    max_length = 15

    length = random.randint(min_length, max_length)

    lowercase_characters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeric_characters = '1234567890'

    characters = lowercase_characters + uppercase_characters + numeric_characters
    result = ''
    for _ in range(length):
        random_index = random.randint(0, len(characters) - 1)
        result += characters[random_index]

    if any(c in result for c in lowercase_characters) and \
       any(c in result for c in uppercase_characters) and \
       any(c in result for c in numeric_characters):
        return result
    else:
        return random_pw()

def random_name():
    min_length = 4
    max_length = 6

    length = random.randint(min_length, max_length)

    lowercase_characters = 'abcdefghijklmnopqrstuvwxyz'

    characters = lowercase_characters
    result = ''
    for _ in range(length):
        random_index = random.randint(0, len(characters) - 1)
        result += characters[random_index]
    return result

def signup_live_email():
    while True:
        try:
            #current_working_directory = os.getcwd()
            #capsolver_extension_path = current_working_directory + "/capsolver_extension_firefox"
            #os.environ['SSL_CERT_FILE'] = '/dev/null'

            chrome_options = webdriver.ChromeOptions()
            chrome_profile = "/home/tch/.config/google-chrome/Profile\\ 1"
            chrome_options.add_argument(f"user-data-dir={chrome_profile}")

            #chrome_options.add_argument('--load-extension=/Users/tsoichinghin/Library/Application\ Support/Google/Chrome/Profile\ 23/Extensions')
            #profile_path = '/Users/tsoichinghin/Library/Application Support/Firefox/Profiles/kyhno26y.default'
            #profile = webdriver.FirefoxProfile(profile_directory=profile_path)

            proxy_options = {
                'proxy':{
                    'http':'http://user-lu4456881-region-hk:Qdi5pZ@as.rhyq9ffx.lunaproxy.net:12233'
                }
            }

            #chrome_options.add_extension("--load-extentions={0}".format(capsolver_extension_path))

            driver = webdriver.Chrome(seleniumwire_options = proxy_options, options = chrome_options)
            #driver.install_addon(capsolver_extension_path, temporary=True)
            driver.set_page_load_timeout(60)

            try:
                driver.get("https://signup.live.com/signup")
                print("Page load succeed.")
            except Exception as a:
                print("Page load timeout:", a)
                raise
            
            countdown(60)

            email = random_email()
            print("email:", email)

            try:
                driver.find_element(By, "MemberName").send_keys(email)
                print("Type email okay.")
            except Exception as b:
                print("Type email fail:", b)
                raise

            try:
                firstnextstep = driver.find_element(By.ID, "iSignupAction")
                firstnextstep.click()
                print("Click first next step okay")
            except Exception as c:
                print("Click first next step fail:", c)
                raise

            countdown(5)

            pw = random_pw()
            print("pw:", pw)

            try:
                driver.find_element(By.ID, "PasswordInput").send_keys(pw)
                print("Type password okay")
            except Exception as d:
                print("Type password fail:", d)
                raise

            try:
                secondnextstep = driver.find_element(By.ID, "iSignupAction")
                secondnextstep.click()
                print("Click second next step okay")
            except Exception as e:
                print("Click second next step fail:", e)
                raise

            countdown(5)

            lastname = random_name()
            print("last name:", lastname)

            try:
                driver.find_element(By.ID, "LastName").send_keys(lastname)
                print("Type lastname okay")
            except Exception as f:
                print("Type lastname fail:", f)
                raise

            firstname = random_name()
            print("first name:", firstname)

            try:
                driver.find_element(By.ID, "FirstName").send_keys(firstname)
                print("Type firstname okay")
            except Exception as g:
                print("Type firstname fail:", g)
                raise

            try:
                thirdnextstep = driver.find_element(By.ID, "iSignupAction")
                thirdnextstep.click()
                print("Click third next step okay")
            except Exception as h:
                print("Click third next step fail:", h)
                raise

            countdown(5)

            Birthyear = random.randint(1980, 2010)
            print("Birthyear:", Birthyear)

            try:
                driver.find_element(By.ID, "BirthYear").send_keys(Birthyear)
                print("Type year okay")
            except Exception as i:
                print("Type year fail:", i)
                raise

            Birthmonth = random.randint(1, 12)
            print("Birthmonth:", Birthmonth)

            try:
                select_month_element = driver.find_element(By.ID, "BirthMonth")
                select_month = Select(select_month_element)
                select_month.select_by_index(Birthmonth)
                print("Type month okay")
            except Exception as j:
                print("Type month fail:", j)
                raise

            Birthday = random.randint(1, 28)
            print("Birthday:", Birthday)

            try:
                select_day_element = driver.find_element(By.ID, "BirthDay")
                select_day = Select(select_day_element)
                select_day.select_by_index(Birthday)
                print("Type day okay")
            except Exception as k:
                print("Type day fail:", k)
                raise

            try:
                forthnextstep = driver.find_element(By.ID, "iSignupAction")
                forthnextstep.click()
                print("Click forth next step okay")
            except Exception as l:
                print("Click forth next step fail:", l)
                raise

            countdown(180)
            
            decline_button = driver.find_element(By.ID, "declineButton")
            sticky_footer = driver.find_element(By.ID, "StickyFooter")
            main_content_landing = driver.find_element(By.ID, "main-content-landing-react")

            if decline_button or sticky_footer or main_content_landing:
                driver.quit()
                break
            else:
                driver.quit()

        except Exception as ex:
            print("Driver quit. Email signup fail:", ex)
            driver.quit()
    
    return email, pw

def main():
    while True:
        try:
            num_iterations = int(input("Please enter how many accounts you want to create:"))
            for i in range(num_iterations):
                print(f"Round:{i+1}")
                email, pw = signup_live_email()
                csv_file = os.path.join("ac.csv")
                mode = "a" if os.path.exists(csv_file) else "w"
                with open(csv_file, mode, newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow([email, pw])       
            break 
        except ValueError:
            print("Input error: Please enter a correct number.")
            return

main()
