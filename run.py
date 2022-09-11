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

#Introducing the Customer and a Welcome Message.  
#userName = input('Please enter your name: ')
#welcomeMessage = f'Welcome to Love Pizza, Please may we take your order {userName}'
#print(userName)
#print(welcomeMessage)

#read data from file 

order_list = SHEET.worksheet('order_list')

data = order_list.get_all_values()

print(data)
