
# Client module
# Stores client info from parsed Request Log item

# Set client  variables
case_number = ''
first_name = ''
last_name = ''
dob = ''
full_name = ''
address = ''
gender = ''

# Set fields 
def setFields(case_number_='', first_name_='', last_name_='', dob_='', full_name_='', address_='', gender_=''):
    # Set client  variables
    case_number = case_number_
    first_name = first_name_.title().strip()
    last_name = last_name_.title().strip()
    dob = dob_
    full_name = first_name_ + " " + last_name_
    address = address_
    gender = gender_


# Print method
def toString():
    return "Case Num: {} | Name: {} | DOB: {} | Address: {}".format(case_number, full_name, dob, address)
