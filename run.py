import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_pizza')

"""
Welcoming user with name input and a welcome message
"""

userName = input('Please enter your name: ')

addressUser = input('Please enter your house number followed by your firstline of address: ')

postcodeUser = input('Please enter your postcode: ')

print('*'*65)
print(f'Welcome {userName} to our Love Pizza Store. We make fresh, tasty pizza' )
print(f'Delivery Address: {addressUser} {postcodeUser}')
print('*'*65)

"""
Linking worksheet to program and displaying menu for user
"""

order_str = SHEET.worksheet('order_list')
data = order_str.get_all_values()

selectMenu = f'Please select from the menu below'
print(selectMenu)
for pizza in data:
    print(pizza)

"""
Prompting user option to place order and selecting which Pizza they require
"""
while True:
    noPurchase = input('Would you like to continue ordering? (yes/no): ')
    if noPurchase.lower()=='yes':
        # call function to order pizza
        break
    elif noPurchase.lower()=='no':
        print('Sorry you did not like our selection of our delicious freshly made Pizza , maybe next time')
        # function to close 
        quit()
    else:
        print('Invalid Input you must enter yes / no')
   
