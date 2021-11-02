# Imports 
from urllib import request
from pip._vendor.packaging import version
from view.custom_widgets.popup_dialog import popups
from settings.settings import INTERNAL_VERSION_NUMBER

import json


# Get version from API
def get_version():
    
    # Form creator file ver uploded to the server
    file_ver = ''

    # Call devserver API to get list of files 
    with request.urlopen("http://devserver.local:8000/form_creator_api/uploaded_files/Update/") as url:

        # Get file detail from API 
        file_detail = json.loads(url.read().decode())

        # Get form creator ver 
        file_ver = file_detail['version']

    return file_ver



# Check for update 
def update_check():

    # Compare internal ver to whatever is uploaded to the server 
    retrieved_version = get_version()

    if version.parse(retrieved_version) > version.parse(INTERNAL_VERSION_NUMBER):

        # Prompt user for update
        popups.info_popup(text="An update is available. Please update to the latest version of Form Creator", window_title="Update Available")

        #TODO 
        # Open a chrome window to the download page 

# Only run if called directly
if __name__ == "__main__":
    
    update_check()
