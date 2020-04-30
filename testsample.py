from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('C:\SeleniumWebDrivers\chromedriver.exe')
wait = WebDriverWait(driver, 5)

username_correct = "eugen"
password_correct = "nasec"

username_bad = "nguyen"
password_bad = "cesan"


def login_to_dashboard(username, password):

    driver.get("https://auta.sde.cz/login")

    username_input = driver.find_element_by_xpath("//*[@id=\"mat-input-0\"]")
    username_input.send_keys(username)

    password_input = driver.find_element_by_xpath("//*[@id=\"mat-input-1\"]")
    password_input.send_keys(password)

    login_btn = driver.find_element_by_xpath("/html/body/app-root/app-login-layout/div[2]/app-login/mat-card/form/button[2]")
    login_btn.click()
    print("Attempting to log in")

    try:
        wait.until(EC.url_contains("/dashboard/"))
        print(driver.current_url)
        print("Login successful")
    except:
        error = driver.find_element_by_class_name("error-label")
        print("Login failed")
        print(error.text)
        driver.quit()


def get_not_communicating_car_info():
    
    listed_available_cars = driver.find_elements_by_tag_name("app-car-row")
    try:
        
        for car in listed_available_cars:
            error_icon = car.find_element_by_class_name("error-icon")
            register_number = car.find_element_by_class_name("car-headline").text
            car_description = car.find_element_by_class_name("car-description").text
            car_position = car.find_element_by_class_name("position").text
        
            if error_icon:
                print("Vozidlo nekomunikuje")
                print(car_description)
                print(register_number)
                print(car_position)                

    except:
        print("Stale Error")


def logout():    
    
    logout_btn = driver.find_element_by_xpath("/html/body/app-root/app-site-layout/mat-sidenav-container/mat-sidenav/div/mat-action-list/div[2]/button[2]")
    logout_btn.click()
    try:
        wait.until(EC.url_contains("/login"))
        print("Logout successful")
    except:
        print("Logout failed")


login_to_dashboard(username_correct, password_correct)
get_not_communicating_car_info()
logout()
