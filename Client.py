#Form Creator 
#Created by: Kurt Palo 
#For: HCC (MHRC)

#Client class 
#Stores client info from parsed Request Log item 

class Client: 

    #Constructor
    def __init__(self, caseNum, firstName, lastName, dob, address):
        
        #Set client  variables 
        self.caseNum = caseNum
        self.firstName = firstName.title().strip()
        self.lastName = lastName.title().strip()
        self.dob = dob
        self.fullName = self.firstName + " " + self.lastName
        self.address = address
        self.gender = ''
    
    #Print method
    def toString(self):
       return "Case Num: {} | Name: {} | DOB: {} | Address: {}".format(self.caseNum, self.fullName, self.dob, self.address)