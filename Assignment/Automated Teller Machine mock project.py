import datetime

username = input("Input Name to Register : ")
user_pin = int(input("Create a Pin : "))
user = {}
user_db = []


def register():
    user['name'] = username
    user['password'] = user_pin
    user['balance'] = 1000.0
    user_db.append(user)


def show_date_and_time():
    now = datetime.datetime.now()
    print(f"Current Date and Time is :")
    print(now.strftime("%y -%m -%d %H:%M:%S"))


user_input = int(input("Select 1, 2 or 3 FOR compliant to perform any transaction : "))


def user_selection(choice):
    try:
        while choice != -1:
            if choice == 1:
                user_dto = int(input("Enter your pin : "))
                user_withdrawal_amount = float(input("How would you like to Withdraw? : "))
                withdrawal(user_dto, user_withdrawal_amount)
                break
            elif choice == 2:
                user_dtoo = int(input("Enter your pin ; "))
                user_deposit_amount = float(input("how would like to deposit? : "))
                deposit_cash(user_dtoo, user_deposit_amount)
                break
            elif choice == 3:
                my_compliant = input("What issue will you like to report? ")
                compliant(my_compliant)
                break
            else:
                choice = int(input(
                    "Wrong Choice. Why u no dey get sense.Select 1 or 2 to perform any transaction joor. U dey Craze : "))
    except ValueError:
        print("Invalid Selection.... Get Sense OGA!!!")


def withdrawal(user_pin_code, amount):
    try:
        current_user = {}
        user_found = False
        for user_details in user_db:
            if user_details['password'] == user_pin_code:
                current_user = user_details
                user_found = True
                break
        if user_found:
            if 0 <= amount < current_user['balance']:
                current_user['balance'] -= amount
                print("take cash")
            else:
                print("Insufficient Funds")
        else:
            print("wrong Pin")
    except ValueError:
        print("OGa GetSense now....Please Enter a Valid Number as Amount")


def deposit_cash(user_pin_code, amount):
    print('hjk')
    try:
        _user = {}
        user_reached = False
        for user_details in user_db:
            if user_details['password'] == user_pin_code:
                _user = user_details
                user_reached = True
                break
        if user_reached:
            if amount > 0:
                _user['balance'] += amount
                print(f"You have  been credited with {amount}, your current balance is {user['balance']}")
            else:
                print("Unable to Deposit. Try again after 60 seconds")
        else:
            print('Wrong Pin')
    except ValueError:
        print("OGa GetSense now....Please Enter a Valid Number as Amount")


def compliant(issues):
    collected_issues = issues
    print("Thank you for contacting us.")


def main():
    register()
    show_date_and_time()
    user_selection(user_input)


if __name__ == '__main__':
    main()
