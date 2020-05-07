import os
import json
import random


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STAFF_FILE = os.path.join(BASE_DIR, 'staff.txt')
CUSTOMER_FILE = os.path.join(BASE_DIR, 'customer.txt')

start_message = "\nEnter : \n\t1. Staff Login \n\t2. Close App\n>>"
# login_message = "\nEnter username and password separated by ',':\n\tE.G\n>> amaka, 1234\n>> "
loged_in_message = """\nSelect from options:
    1. Create new bank account
    2. Check Acoount Details
    3. Logout"""

def open_acct(acct_name, acct_bal, acct_type, acct_email, acct_num):
    with open(CUSTOMER_FILE, 'r') as temp:

        data = json.load(temp)
        data[acct_num] = []
        data[acct_num].append({
            'acct_name': acct_name,
            'acct_bal': acct_bal,
            'acct_type': acct_type,
            'acct_email': acct_email,
            'acct_num': acct_num
        })
    
    with open('temp.json', 'w') as cos_file:
        json.dump(data, cos_file, indent=4)
        os.rename('temp.json', CUSTOMER_FILE)

# open_acct('Moses Oghene', 2000, 'savings', 'larry@gmail.com', '0025524505')
# open_acct('Joe Doe', 2000, 'current', 'johndoe@gmail.com', '1059367457')
# print(STAFF_FILE)
def load_staff():
    with open(STAFF_FILE, 'r') as  database:
        staffs = json.load(database)
        return staffs


while True:
    try:        
        prompt_resoponse = int(input(start_message))
        print(type(prompt_resoponse))
        if prompt_resoponse == 1:
            username = input("\nEnter Username\n>> ").lower()
            password = int(input("\nEnter Password\n>> "))
            # staff_database = load_staff()
            with open('staff.txt', 'r') as  database:
                staffs = json.load(database)
            print(staffs)
            
            # print(login_data[0].lower() and login_data[1] in staff_database[0])
            for data in staffs:
                # print(data['staff1']['username'])
                if password and username in data:
                    print(data['name'])
            
    except KeyboardInterrupt:
        print(">> Loading...App closed")
        break
    # except ValueError:
    #     print(f"Invalid input, please try again")