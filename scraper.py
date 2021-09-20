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

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(executable_path='/Users/emilzacharczuk/Downloads/chromedriver')
driver.get("https://www.airbnb.co.uk/rooms/33090114")
driver.implicitly_wait(20)
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

submitButton = driver.find_element_by_xpath("(//button[contains(text(),'OK')])").click()
submit = driver.find_element_by_link_text("Show all 15 amenities").click()
kitchen = driver.find_element_by_xpath("(//div[contains(text(),'Kitchen')])")
# wifi = driver.find_element_by_xpath("(//div[contains(text(),'Wifi')])")
wifi = driver.find_element_by_id("pdp_v3_internet_office_4_33090114-0-row-title")
tv = driver.find_element_by_xpath("(//div[contains(text(),'TV')])")
patio = driver.find_element_by_xpath("(//div[contains(text(),'Patio or balcony')])")
hairdryer = driver.find_element_by_xpath("(//div[contains(text(),'Hair dryer')])")
bedlinen = driver.find_element_by_xpath("(//div[contains(text(),'Bed linen')])")
heating = driver.find_element_by_xpath("(//div[contains(text(),'Heating')])")
smoke_alarm = driver.find_element_by_xpath("(//div[contains(text(),'Smoke alarm')])")
carbon_monox_alarm = driver.find_element_by_xpath("(//div[contains(text(),'Carbon monoxide alarm')])")


# //*[@id="site-content"]/div/div[1]/div[2]/div[7]/div/div/div/div[2]/section/div[3]/div[1]/div/div[1]
# //*[@id="site-content"]/div/div[1]/div[2]
print(kitchen.text)
print(wifi.text)
print(tv.text)
print(patio.text)
print(hairdryer.text)
print(bedlinen.text)
# This is just a sample, I would also use booleans instead of text
property_details['amenieties'] = {
    'kitchen': kitchen.text,
    'wifi': wifi.text,
	'tv': tv.text,
	'patio': patio.text,
	'hairdryer': hairdryer.text,
    'bedlinen': bedlinen.text,
    'safety': [smoke_alarm.text, carbon_monox_alarm.text]
}

print(property_details)

driver.quit()


# //*[@id="site-content"]/div/div[1]/div[2]/div[2]/div/div/div/div/section/div[1]/span/h1
# /html/body/div[5]/div/div/div[1]/div/main/div/div/div/div/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/section/div[1]/span/h1
# /html/body/div[5]/div/div/div[1]/div/main/div/div/div/div/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/section/div[1]/span/h1
#site-content > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > div > div > div:nth-child(2) > section > div > div > div:nth-child(2) > span:nth-child(4)
# "(//span[contains(text(),’odamax’)])[1]"
