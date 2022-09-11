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
welcomeMessage = f'Welcome to Love Pizza, Please may we take your order {userName}'
print(userName)
print(welcomeMessage)


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
User option to place order and selecting what Pizza they require
"""
