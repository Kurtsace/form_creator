# Scraper module for collecting scraped information

# Imports
from selenium import webdriver
from model.client import Client
import traceback
import os


# Get client info
def get_client_info(id):

    # Client instance 
    client = Client(); 

    # For testing purposes supply a hard coded url
    # Later on replace this with a get request to the hcc-server for updated urls
    url = "http://collaboration.mbgov.ca/sites/MHCD/Security_Info/HCC/EIA/Lists/Request%20Log%2010/DispForm.aspx?ID={}".format(
        id)

    # Path of the web driver
    driver_path = "W:/houhcc/Form Creator Resources/Webdriver/chromedriver.exe"

    # Make sure we are able to load the webdriver
    if not os.path.exists(driver_path):
        print("Chromedriver not found")

    # Edit the options
    # Disable extensions and set the window to run headless
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.headless = True

    # Start a driver instance
    try:
        driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

    except :
        traceback.print_exc()
        return client

    # Navigate to the ID page --No auth header needed
    driver.get(url)

    # Scrape the data needed 
    # Get the xpath of the SPFieldText item within the table only 
    field_elements = driver.find_elements_by_xpath("//*[@id='SPFieldText']")

    # Ensure the element list is not empty 
    if not field_elements:
        return client

    # Convert from raw xpath objects to string 
    field_elements = [field.text for field in field_elements]

    # End the driver instance 
    driver.quit()

    # Build a client model object using the scraped data
    # Index is as follows:
    # field_elements[0] = Case number 
    # [1] = first name 
    # [2] = last name
    # [3] = dob
    # [4] = Street address
    # [5] = unit number
    # Note that address can be blank here depending on the type of request 
    address = field_elements[5] + " " + field_elements[4]
    client = Client(field_elements[0], field_elements[1], field_elements[2], field_elements[3], address)

    return client
    