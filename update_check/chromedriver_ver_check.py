# Imports
from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException

from view.custom_widgets.popup_dialog import popups

import subprocess
import os
import time
import traceback
import tempfile
import zipfile

# Internal driver path
INTERNAL_DRIVER_PATH = os.path.abspath(os.path.join(os.getcwd(), "chromedriver/chromedriver.exe"))
INTERNAL_DRIVER_FOLDER_PATH = os.path.abspath(os.path.join(INTERNAL_DRIVER_PATH, os.pardir)) + '\\'

# Backup driver path
BACKUP_DRIVER_PATH = "W:/houhcc/Form Creator Resources/Webdriver/chromedriver.exe"

# Compares the current Chrome Browser version with the current chromedriver version


def version_check():

    # Make sure internal driver exists
    # If no path, download the latest driver release
    if not os.path.exists(INTERNAL_DRIVER_PATH):
        print("Chrome driver not found. Attempting driver install")

        # Get current driver compatible for current browser
        get_current_browser_driver()

        # Leave function
        return

    try:

        # Create options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.headless = True

        # Get current chrome driver and browser version
        driver = webdriver.Chrome(executable_path=INTERNAL_DRIVER_PATH)
        browser_ver = driver.capabilities['browserVersion']
        driver_ver = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]

        # Get only the first int value before the .
        browser_ver_int = int(browser_ver.split('.')[0])
        driver_ver_int = int(driver_ver.split('.')[0])

        # If driver out of date
        if browser_ver_int > driver_ver_int:

            # Get cleaned browser version string
            # Parse the full string for only the first 3 decimals
            # i.e 72.0.123.34344 -> 72.0.123
            # refer to documentation https://chromedriver.chromium.org/downloads/version-selection
            desired_ver = browser_ver.split(".")
            desired_ver = desired_ver[:-1]
            desired_ver = '.'.join(desired_ver)

            # Get the latest build of this version
            get_driver(desired_ver)

        # If the driver ver > browser ver it would instead go into the except block
        # right after driver initialization above

    # Driver version > browser version or Driver version is way out of date
    except SessionNotCreatedException as e:

        # Get driver version and browser version
        msg = str(e).split('\n')
        driver_ver = msg[0].split(' ')[-1]
        driver_ver_int = int(driver_ver)

        # Get browser path and version via a shell
        # Could probably brute force a parse on the message string to get the version already
        browser_path = msg[1].split('path ')[-1].replace("\\", '\\\\')
        browser_ver = subprocess.check_output(
            r'wmic datafile where name="{path}" get Version /value'.format(
                path=browser_path),
            shell=True
        )
        browser_ver = browser_ver.decode('utf-8').strip().split('=')[-1]
        browser_ver_int = int(browser_ver.split('.')[0])

        # If browser out of date
        if driver_ver_int > browser_ver_int:
            print("Browser out of date")

            # Prompt for browser update
            popups.error_popup(
                text="Error", detailed_text="Chrome is out of date. Please update chrome to the newest version.")

        # If driver is way out of date
        elif browser_ver_int > driver_ver_int:
            print("Driver too old")

            # download and update to the newest driver compatible
            # Use backup driver via the network drive to update the users driver
            get_current_browser_driver()


# Update the current chrome driver
def get_driver(desired_ver, use_backup_driver=False):

    # Check if we are using the internal driver or the backup driver
    desired_driver_path = BACKUP_DRIVER_PATH if use_backup_driver else INTERNAL_DRIVER_PATH

    # Download zip file
    try:

        # Create settings
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.headless = True

        # Create temp folder to download zip file in
        TEMP_FOLDER_DIR = tempfile.TemporaryDirectory(dir=INTERNAL_DRIVER_FOLDER_PATH)

        # Set download settings
        chrome_options.add_experimental_option('prefs',
            {
                   "download.default_directory": r"{}".format(TEMP_FOLDER_DIR.name + "\\"),
                   "download.prompt_for_download": False,
                   "download.directory_upgrade": False,
                   "safebrowsing.enabled": False,
                   "safebrowsing_for_trusted_sources_enabled": False,
            }
        )

        # Instantiate driver
        driver = webdriver.Chrome(
            executable_path=desired_driver_path, options=chrome_options)

        # Get latest release of this build
        latest_release_ver = get_latest_release(desired_ver, driver)

        # Generate the link to navigate to
        driver_release_url = "https://chromedriver.storage.googleapis.com/{ver}/chromedriver_win32.zip".format(ver=latest_release_ver)

        # Download desired driver
        driver.get(driver_release_url)

        # Sleep
        time.sleep(3)

        # Quit driver instance
        driver.quit()

        # Downloaded zip file path
        ZIPFILE_PATH = os.path.join(INTERNAL_DRIVER_FOLDER_PATH, TEMP_FOLDER_DIR.name + "/chromedriver_win32.zip")

        # Unzip file
        with zipfile.ZipFile(ZIPFILE_PATH, 'r') as zip_file:
            zip_file.extractall(INTERNAL_DRIVER_FOLDER_PATH)

        # Clean up temp dir
        TEMP_FOLDER_DIR.cleanup()

    except:
        traceback.print_exc()

        popups.error_popup(text="Error", detailed_text="Unable to begin update process. Contact an administrator.")
   


# Navigate to the url to get the latest ver using the desired driver
def get_latest_release(desired_ver, driver):

    # Get the latest release value
    try:

        # Latest release URL
        LATEST_RELEASE_URL = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{ver}".format(ver=desired_ver)

        # Navigate to latest release
        driver.get(LATEST_RELEASE_URL)
        latest_release_ver = driver.find_element_by_tag_name('pre').text

        return latest_release_ver

    except:
        traceback.print_exc()

        popups.error_popup(text="Critical Error", detailed_text="Unable to retrieve latest Chromedriver release. Contact an administrator.")



# Get a driver that matches current browser ver 
def get_current_browser_driver():

    # Get current chrome version
    output = subprocess.check_output(
        r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version /value',
        shell=True
    )
    version = output.decode('utf-8').strip().split("=")[-1]

    # Make sure chrome is installed 
    if "." in version:

        # Download latest chromedriver build
        desired_ver = version.split(".")
        desired_ver = desired_ver[:-1]
        desired_ver = '.'.join(desired_ver)

        # Get driver 
        get_driver(desired_ver, use_backup_driver=True)
        
    else:
        print("Please install chrome")
        popups.error_popup(text="Error", detailed_text="Chrome is needed to run this application. Please install Chrome.")



# Only run if called directly
if __name__ == "__main__":
    version_check()
