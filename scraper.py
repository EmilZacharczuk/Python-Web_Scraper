# Please write some code that scrapes property name, property type (e.g Apartment), number of bedrooms, bathrooms and list of the amenities for the following 3 properties:
#
# https://www.airbnb.co.uk/rooms/33571268
#
# https://www.airbnb.co.uk/rooms/33090114
#
# https://www.airbnb.co.uk/rooms/50633275
#
# This can be implemented in any language you prefer (although it would be nice if done in Python or JavaScript/TypeScript/NodeJS as that's what we use most at TravelNest). Please put your project into a code repository and share it with us.
#

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")


driver = webdriver.Chrome(executable_path='/Users/emilzacharczuk/Downloads/chromedriver')

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_class_name(className):
    try:
        driver.find_element_by_class_name(className)
    except NoSuchElementException:
        return False
    return True

properties_array = []

property_ids_array = ["33090114", "50633275"]
def propert_portfolio_builder(property_ids_array):
    properties_array_portfolio = []
    domainURL = 'https://www.airbnb.co.uk/rooms/'
    for property_id in property_ids_array:
        print (domainURL + property_id)
        driver.get(domainURL + property_id)
        driver.implicitly_wait(10)
        if check_exists_by_class_name('_fecoyn4'):
            name = driver.find_element_by_class_name('_fecoyn4')
            type = driver.find_element_by_class_name('_1qsawv5')
            bedroom = driver.find_element_by_xpath("(//span[contains(text(),'bedrooms') or contains(text(),'bedroom')])")
            bathroom = driver.find_element_by_xpath("(//span[contains(text(),'bathrooms') or contains(text(),'bathroom')])")

            # build main level object
            property_details = {
            	'name': name.text,
            	'type': type.text,
            	'bedroom': bedroom.text,
                'bathroom': bathroom.text
                }

            print(name.text)
            print(type.text)
            print(bedroom.text)
            print(bathroom.text)
            # submitButton = driver.find_element_by_xpath("(//button[contains(text(),'OK')])")
            if check_exists_by_xpath("(//button[contains(text(),'OK')])"):
                submitButton = driver.find_element_by_xpath("(//button[contains(text(),'OK')])").click()
            submit = driver.find_element_by_partial_link_text("amenities").click()
            property_details["amenities"] ={}
            kitchen = driver.find_element_by_xpath("(//*[contains(text(),'Kitchen') or contains(text(),'Kitchen and dining')])")
            property_details["amenities"]["kitchen"] = True
            # wifi = driver.find_element_by_xpath("(//div[contains(text(),'Wifi')])")
            wifi = driver.find_element_by_id("pdp_v3_internet_office_4_"+ property_id +"-0-row-title")
            property_details["amenities"]["wifi"] = True
            if check_exists_by_xpath("(//div[contains(text(),'TV')])"):
                tv = driver.find_element_by_xpath("(//div[contains(text(),'TV')])")
                property_details["amenities"]["tv"] = True
            if check_exists_by_xpath("(//div[contains(text(),'Patio or balcony')])"):
                patio = driver.find_element_by_xpath("(//div[contains(text(),'Patio or balcony')])")
                property_details["amenities"]["patioOrBalcony"] = True
            if check_exists_by_xpath("(//div[contains(text(),'Hair dryer')])"):
                hairdryer = driver.find_element_by_xpath("(//div[contains(text(),'Hair dryer')])")
                property_details["amenities"]["hairDryer"] = True
            if check_exists_by_xpath("(//div[contains(text(),'Bed linen')])"):
                bedlinen = driver.find_element_by_xpath("(//div[contains(text(),'Bed linen')])")
                property_details["amenities"]["bedLinen"] = True
            if check_exists_by_xpath("(//div[contains(text(),'Heating')])"):
                heating = driver.find_element_by_xpath("(//div[contains(text(),'Heating')])")
                property_details["amenities"]["heating"] = True
            if check_exists_by_xpath("(//div[contains(text(),'Smoke alarm')])"):
                smoke_alarm = driver.find_element_by_xpath("(//div[contains(text(),'Smoke alarm')])")
                property_details["amenities"]["smokeAlarm"] = True
            if check_exists_by_xpath("(//div[contains(text(),'Carbon monoxide alarm')])"):
                carbon_monox_alarm = driver.find_element_by_xpath("(//div[contains(text(),'Carbon monoxide alarm')])")
                property_details["amenities"]["carbonMonoxideAlarm"] = True


            properties_array.append(property_details)
            print(properties_array)
        else:
            print ("Property doesn't exists")

    driver.quit()
    return  properties_array

propert_portfolio_builder(property_ids_array)
# //*[@id="site-content"]/div/div[1]/div[2]/div[2]/div/div/div/div/section/div[1]/span/h1
# /html/body/div[5]/div/div/div[1]/div/main/div/div/div/div/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/section/div[1]/span/h1
# /html/body/div[5]/div/div/div[1]/div/main/div/div/div/div/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/section/div[1]/span/h1
#site-content > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > div > div > div:nth-child(2) > section > div > div > div:nth-child(2) > span:nth-child(4)
# "(//span[contains(text(),’odamax’)])[1]"
