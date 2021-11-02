from urllib import request
import json

'''
    Temp settings file for testing phase, will change later on

'''

safeway_list = {}

settings = {}

INTERNAL_VERSION_NUMBER = "1.3.4.4"

def init():

    # CHANGE ALL API URLS TO THE REAL ONES LATER

    # Get safeway list from api
    with request.urlopen("http://hcc-devserver.me.mbgov.ca:8000/form_creator_api/safeway_list/") as url:

        data = json.loads(url.read().decode())

        # Rebuild the list into "NAME" : "VALUE" pairs
        for item in data:
            safeway_list[item["location_name"]] = item["fax_number"]

    # Get the request log url
    with request.urlopen("http://hcc-devserver.me.mbgov.ca:8000/form_creator_api/request_log_url/") as url:

        data = json.loads(url.read().decode())

        settings["request_log_url"] = data["url"]




# Returns the current request log URL
def get_url():
    return settings["request_log_url"]



# Returns internal version number
def get_internal_ver():
    return INTERNAL_VERSION_NUMBER

