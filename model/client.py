
# Client class
# Stores client info from parsed Request Log item


class Client:

    # Constructor
    def __init__(self, case_num='', first_name='', last_name='', dob='', address=''):
        
        # Set client  variables 
        self.case_number = case_num
        self.first_name = first_name.title().strip()
        self.last_name = last_name.title().strip()
        self.dob = dob
        self.full_name = self.first_name + " " + self.last_name
        self.address = address
        self.gender = ''
    
    # Print method
    def toString(self):
       return "Case Num: {} | Name: {} | DOB: {} | Address: {}".format(self.case_number, self.full_name, self.dob, self.address)
