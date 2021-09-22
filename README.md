Project name: Half baked screen scraper

How to run:

Dependencies:

- Chrome Web Browser
- Python
- Selenium webdriver

Command to execute:

python scraper.py

What it does:

The programme uses Selenium to make http calls in your local browser to pull data from the Airbnb website and build a portfolio of properties in JSON format

********Technology used**********

It is based on Selenium and Python. The choice behind is that Selenium can scrape data from dynamic websites as this is the case for Airbnb. I have tried JavaScript but had issues with identifying relevant html elements with CSS selector and tried Beautiful Soup library but it only worked for static websites.


*********Constrains************

- Limited time to finish the project.

I only had a couple of hours on Sunday,Monday and Tuesday each day to work on it and trying to navigate between different work and personal commitments. As a result the product is MVP but missing many important features.

- Luck of experiences

This was my first time when I built a web scraper. I had spent a bit of time reading documentation and trying to code at the same time. But that defintely had an impact on my pace.  


********Further considerations********

- Refactoring

The code is working for a very particular set of data, it should be refactor to consist of more generic modules (function) which could be used for larger sets of data. For example paths to specific html elements need further consideration. Maybe it would be advisable to use CSS selector than selectByClassName or XPath.

- Error handling

There is no error handling present. This is mainly because I am not sure if we should be breaking or just logging an error (ie what would be requirements). I am not proficient in Python so will need to look further into sytax for that.

- Tests

No testing is included. Something that should be implemented at first place (good habit) but had no time to do it as was trying to get it to function at least.

- Data rendering

Rendering of JSON on a web page server localy would be good to have either using Javascript or React. I run out of time but it would be interesting to know how to combine Python with React.

- Poor performance

Execution times are really poor. I would imagine there are ways to do it by executing multiple calls simultaneously or using a different framework than Selenium.



It was interesting experience and a lot to talk about when we meet on Friday. 
