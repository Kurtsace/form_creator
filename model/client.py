
# Client module
# Stores client info from parsed Request Log item

# Set client  variables
client_info = {
    'case_number': '',
    'first_name': '',
    'last_name': '',
    'dob': '',
    'full_name': '',
    'address': '',
    'gender': '',
}


# Set fields
def setFields(case_number_='', first_name_='', last_name_='', dob_='', full_name_='', address_='', gender_=''):
    # Set client  variables
    client_info['case_number'] = case_number_
    client_info['first_name'] = first_name_.title().strip()
    client_info['last_name'] = last_name_.title().strip()
    client_info['dob'] = dob_
    client_info['full_name'] = first_name_ + " " + last_name_
    client_info['address'] = address_
    client_info['gender'] = gender_


# Print method
def toString():
    return "Case Num: {} | Name: {} | DOB: {} | Address: {}".format(client_info['case_number'], client_info['full_name'], client_info['dob'], client_info['address'])
