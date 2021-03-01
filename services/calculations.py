#Service(s) for calculating values, i.e food voucher amounts 

def calculate_food_amount(days=0, adults=0, children=0, food=False, fuel=False, diapers=False):

    # Approved amount 
    approved_amount = 0

    # Begin calculation 
    # If food has been selected 
    if food:

        #Calculate amount of only 1 adult selected
        if adults == 1:
            approved_amount += days * 6.41 + (children * 3.85)
        else:
            approved_amount += days * 11.34 + (children * 3.85)

    # Add diaper amount if it has been selected 
    if diapers:
        approved_amount += 15

    # Format amount to 2 decimal places
    approved_amount = round(approved_amount, 2)

    #Return approved amount
    return approved_amount
    