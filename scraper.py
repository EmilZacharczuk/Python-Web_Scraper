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
another = driver.find_element_by_xpath("(//span[contains(text(),'bedrooms') or contains(text(),'bedroom')])")
ammenities = name = driver.find_element_by_class_name('iikjzje i10xc1ab dir dir-ltr')

# another2 = driver.find_element_by_xpath("html/body/div[5]/div/div/div[1]/div/main/div/div/div/div/div[1]/main/div/div[1]/div[2]/div[3]/div/div/div/div[2]/section/div/div/div[2]/span[4]")
print(name.text)
print(type.text)
print(another.text)
print(ammenities.text)

driver.quit()


# //*[@id="site-content"]/div/div[1]/div[2]/div[2]/div/div/div/div/section/div[1]/span/h1
# /html/body/div[5]/div/div/div[1]/div/main/div/div/div/div/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/section/div[1]/span/h1
# /html/body/div[5]/div/div/div[1]/div/main/div/div/div/div/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/section/div[1]/span/h1
#site-content > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > div > div > div:nth-child(2) > section > div > div > div:nth-child(2) > span:nth-child(4)
# "(//span[contains(text(),’odamax’)])[1]"
