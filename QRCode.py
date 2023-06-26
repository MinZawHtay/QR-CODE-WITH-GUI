import qrcode
import os
from PIL import Image
import pyfiglet
from pathlib import Path

os.system('cls')

logo_text = "QR CODE"
font = "slant"  # You can choose different font styles, such as "slant", "isometric1", "block", etc.

ascii_art = pyfiglet.figlet_format(logo_text, font=font)
print(ascii_art)

def generate_vcard_qrcode(person_details, company_info, latitude, longitude, filename):
    vcard_data = f"BEGIN:VCARD\n" \
                 f"VERSION:3.0\n" \
                 f"N:{person_details['first_name']}\n" \
                 f"ORG:{company_info['name']}\n" \
                 f"TEL;TYPE=work,voice:{person_details['phone']}\n" \
                 f"ADR;TYPE=work:;;{company_info['address']}\n" \
                 f"EMAIL:{person_details['email']}\n" \
                 f"TITLE:{person_details['title']}\n" \
                 f"END:VCARD"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard_data)
    qr.make(fit=True)
    # color = input("Enter your QR CODE COLOR :")
    qr_code_img = qr.make_image(fill_color='black', back_color="white")

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    filename = os.path.join(folder_path, f'{person_details["first_name"]}.png')
    
    qr_code_img.save(filename)
# Example usage
person_name =input("Enter Your name : ").upper()
person_phone = int(input("Enter Your phone : "))
Title = input('Enter your Department : ')
email = input('Enter your email : ').lower()
person_details = {
    'first_name': person_name,
    'title': Title,
    'phone': person_phone,
    'email': email
}
company_name = input("Enter Your company_name: ")
if company_name == "":
    company_name = "Regis International Co, LTD."


company_address= input("Enter Your company_address : ")
if company_address == "":
    company_address = "Building A, Union Financial Centre, 07-01"
company_info = {
    'name': company_name,
    'address': company_address
}
latitude = 16.774722  # Example latitude (decimal format)
longitude = 96.167667  
pictures_folder = Path.home() / "Pictures"
folder_path = fr'{pictures_folder}\qrcode_folder' 
print('QR Code generating.....')

# if company_address in "":
#     company_address= "Building A, Union Financial Centre, 07-01"
generate_vcard_qrcode(person_details, company_info, latitude, longitude,folder_path )
finish='QR Code generated!'
secondfont = "slant" 
done = pyfiglet.figlet_format(finish, font=secondfont)
print(done)
image = Image.open(fr'C:\Users\Ko Ko Aung\Pictures\qrcode_folder\{person_details["first_name"]}.png' )

# Show the image
image.show()
