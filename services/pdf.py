# Imports 
from fpdf import FPDF
from datetime import datetime
from model.client import client_info
import os 


# Generic PDF header
def create_header(pdf, vendor):

    # Set the font
    pdf.set_font("Arial", size=12, style='B')

    # Add header
    pdf.cell(200, 10, txt="Family Services", ln=1, align="C")
    pdf.cell(
        200, 10, txt="After Hours Service Authorization- Accommodations", ln=1, align="C")
    pdf.cell(200, 10, txt="(1-866-559-6778 or hcc@gov.mb.ca)", ln=1, align="C")

    # Set the font
    pdf.set_font("Arial", size=12)

    # Dated -- Todays date
    pdf.cell(200, 10, txt="Dated: {}".format(
        datetime.today().strftime('%m/%d/%Y')), ln=1, align="L")

    # Vendor line
    pdf.cell(200, 10, txt="Vendor: {}".format(vendor), ln=1, align="L")

# Generic PDF footer


def create_footer(pdf):

    # Billing
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(200, 10, txt="Billing", ln=1, align="L")

    pdf.set_font("Arial", size=12)
    pdf.multi_cell(
        200, 10, txt="Please send an itemized account with a copy of this form to:\nManitoba Family Services and Housing")

    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(200, 10, txt="In Winnipeg:", ln=1, align="L")

    pdf.set_font("Arial", size=12)
    pdf.cell(
        200, 10, txt="eiaafterhoursbilling@gov.mb.ca or Fax 204-948-4048 ", ln=1, align="L")

    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(200, 10, txt="Outside Winnipeg:", ln=1, align="L")

    pdf.set_font("Arial", size=12)
    pdf.cell(
        200, 10, txt="Milena.king@gov.mb.ca or Fax 1-204-726-6539", ln=1, align="L")


# Create a PDF template for an auth form filled out with all the info
def create_auth_form_sa(nights):

    # Instantiate a PDF object
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Add the generic header
    create_header(pdf, vendor="Salvation Army")

    # Set the font
    pdf.set_font("Arial", size=12)

    # Email contact
    pdf.cell(
        200, 10, txt="Email address: xdu@wpgboothcentre.ca & or Boothcentre@wpgboothcentre.ca", ln=1, align="L")

    # Client name
    pdf.cell(200, 10, txt="Client Name: {}".format(
        client_info['full_name']), ln=1, align="L")

    # Client case number
    pdf.cell(200, 10, txt="Case Number: {}".format(
        client_info['case_number']), ln=1, align="L")

    # Client DOB
    pdf.cell(200, 10, txt="DOB: {}".format(
        client_info['dob']), ln=1, align="L")

    # Nights required
    pdf.cell(200, 10, txt="We require 1 room(s) for the following persons for {} night(s):".format(
        nights), ln=1, align="L")

    # Create the table
    data = [["First Name", "Last Name", "Gender"], [
        client_info['first_name'], client_info['last_name'], client_info['gender']]]

    # Set dimensions
    col_width = pdf.w / 4.5
    row_height = pdf.font_size + 1

    # Plot the table
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height, txt=item, border=1, align="C")
        pdf.ln(row_height)

    # PO Notes
    po_notes = """This is to verify that this PO is only for accommodation for the people listed above and the maximum rate for meals is $0. Charges are NOT to include additional charges like Pay per View Movies; liquor; video games; access to water parks, recreation facilities (if applicable)."""

    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(200, 10, txt="PO Notes", ln=1, align="L")

    pdf.set_font("Arial", size=12)

    pdf.multi_cell(150, 10, txt=po_notes, align="L")

    # Create the generic footer
    create_footer(pdf)

    # Output the PDF
    output_file(pdf, client_info['full_name'] + " - Salvation Army")

# Create a PDf of a food voucher
def create_food_voucher(amount, food, diapers, fuel, location, fax, id):

    # Instantiate a PDF object
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Create generic header
    create_header(pdf, location)
    
    # Voucher number
    pdf.cell(200, 10, txt="Voucher Number: {}".format(id), ln=1, align="L")

    # Fax number
    pdf.cell(200, 10, txt="Fax Number: {}".format(fax), ln=1, align="L")

    # Client name
    pdf.cell(200, 10, txt="Client Name: {}".format(
        client_info['full_name']), ln=1, align="L")

    # Client case number
    pdf.cell(200, 10, txt="DOB: {}".format(
        client_info['dob']), ln=1, align="L")

    # Client DOB
    pdf.cell(200, 10, txt="Address: {}".format(
        client_info['address']), ln=1, align="L")

    # Gender 
    pdf.cell(200, 10, txt="Gender: {}".format(
        client_info['gender']), ln=1, align="L")

    # Authorized amount and items
    pdf.multi_cell(
        200, 10, txt="\nApproved for goods and Services as described below (no Tobacco; Lottery or Liquor Products):")

    # Lambda
    def yesno(x): return "Yes" if x else "No"

    # Food
    pdf.cell(200, 10, txt="Food: {}".format(yesno(food)), ln=1, align="L")

    # Diapers
    pdf.cell(200, 10, txt="Diapers ($15.00 Only): {}".format(
        yesno(diapers)), ln=1, align="L")

    # Diapers
    pdf.cell(
        200, 10, txt="Fuel (Gasoline/Diesel Only): {}".format(yesno(fuel)), ln=1, align="L")

    # Amount authorized
    pdf.multi_cell(
        200, 10, txt="\nAuthorized up to a Total Amount (including taxes where applicable)")

    if food and diapers:
        pdf.multi_cell(
            200, 10, txt="${:.2f} (For food only) + $15.00 (For diapers only)".format(round(amount - 15, 2)))

    elif not food and diapers:
        pdf.multi_cell(
            200, 10, txt="${} (For diapers only)".format(round(amount, 2)))

    else:
        pdf.multi_cell(
            200, 10, txt="${} (For food only)".format(round(amount, 2)))

    # Billing info
    pdf.set_font("Arial", size=10, style='B')
    pdf.multi_cell(
        200, 10, txt="\nBilling:  Please send an itemized account with a copy of this form to Manitoba Family Services and Housing")
    pdf.multi_cell(
        200, 10, txt="In Winnipeg:\neiaafterhoursbilling@gov.mb.ca or Fax 204-948-4048 \nOutside Winnipeg:\nMilena.king@gov.mb.ca or Fax 1-204-726-6539")

    # Output the PDF
    output_file(pdf, client_info['full_name'] + " - Voucher")

# Create a PDF of a Son Rise auth form
def create_auth_form_sr(spouse, children, nights):

    # Instantiate a PDF object
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set the font
    pdf.set_font("Arial", size=12, style='B')

    # Add header
    pdf.cell(200, 10, txt="Family Services", ln=1, align="C")
    pdf.cell(
        200, 10, txt="After Hours Service Authorization- Accommodations", ln=1, align="C")
    pdf.cell(200, 10, txt="(1-866-559-6778 or hcc@gov.mb.ca)", ln=1, align="C")

    # Set the font
    pdf.set_font("Arial", size=12,)

    # Dated -- Todays date
    pdf.cell(200, 10, txt="Dated: {}".format(
        datetime.today().strftime('%m/%d/%Y')), ln=1, align="L")

    # Vendor line
    pdf.cell(200, 10, txt="Vendor: SonRise Village", ln=1, align="L")

    # Email contact
    pdf.cell(
        200, 10, txt="Email address: xdu@wpgboothcentre.ca & or Boothcentre@wpgboothcentre.ca", ln=1, align="L")

    # Client name
    pdf.cell(200, 10, txt="Client Name: {}".format(
        client_info['full_name']), ln=1, align="L")

    # Client case number
    pdf.cell(200, 10, txt="Case Number: {}".format(
        client_info['case_number']), ln=1, align="L")

    # Client DOB
    pdf.cell(200, 10, txt="DOB: {}".format(
        client_info['dob']), ln=1, align="L")

    # Nights required
    pdf.cell(200, 10, txt="We require 1 room(s) for the following persons for {} night(s):".format(
        nights), ln=1, align="L")

    # Create the table
    data = [["First Name", "Last Name", "Gender"], [
        client_info['first_name'], client_info['last_name'], client_info['gender']]]

    # Add spouse to the list if a spouse is true
    if spouse:
        data.append(["Spouse", '', ''])

    # Add children if any
    if children > 1:
        data.append(["{} Children".format(children), '', ''])

    elif children == 1:
        data.append(["1 Child", '', ''])

    # Set dimensions
    col_width = pdf.w / 4.5
    row_height = pdf.font_size + 1

    # Plot the table
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height, txt=item, border=1, align="C")
        pdf.ln(row_height)

    # PO Notes
    po_notes = """This is to verify that this PO is only for accommodation for the people listed above and the maximum rate for meals is $0. Charges are NOT to include additional charges like Pay per View Movies; liquor; video games; access to water parks, recreation facilities (if applicable)."""

    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(200, 10, txt="PO Notes", ln=1, align="L")

    pdf.set_font("Arial", size=12)

    pdf.multi_cell(150, 10, txt=po_notes, align="L")

    # Create the generic footer
    create_footer(pdf)

    # Output the file
    output_file(pdf, client_info['full_name'] + " - SonRise")


def output_file(pdf, filename):

    # Output the PDF --Use client name as the file name

    # Make a folder in the desktop if it does not exist already
    path = "C:/Users/{}/Desktop/Auth Forms".format(os.getlogin())

    # Output file to the folder if it already exists
    if os.path.exists(path):
        filename = path + "/{}.pdf".format(filename)
        pdf.output(filename)

    # Make the folder if it does not exist then save it in there
    else:
        os.mkdir(path)
        filename = path + "/{}.pdf".format(filename)
        pdf.output(filename)
