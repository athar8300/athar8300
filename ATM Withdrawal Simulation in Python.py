# The ATM checks that User Withdraw amount is availble on not.
# The Enter amount is multiple of 500 or not.
# if amount is greater then 50k then ATM will give cash in note of 5000.
# if amount is greater then 10k then ATM will give cash in note of 1000.
# if amount is less then 10k then ATM will give cash in note of 500.
# if amount is entered 50500 then back-end will mange it's cash by - 10 notes form cash_5000 and 1 note form cash_500
cash_5000 = 13
cash_1000 = 200
cash_500 = 300
user_withdraw = int(input("Please Enter Your Amount"))
if user_withdraw >= 50000:
    if user_withdraw % 5000 == 0:
        withdraw = user_withdraw // 5000
        if withdraw <= cash_5000:
            print(f"Your Transaction of {user_withdraw} has been Completed")
            cash_5000 = cash_5000 - withdraw
        else:
            print("The Amount is not Availbe, Enter Amount less then 50000")
    elif user_withdraw % 500 == 0:
        withdraw_5000 = user_withdraw // 5000
        cash_5000 = cash_5000 - withdraw_5000
        withdraw_500 = user_withdraw % 5000
        cash_500 = cash_500 - withdraw_500
        print(f"Your Transaction of {user_withdraw} has been Completed")
    else:
        print("Please Enter the Amount Multiple of 500") 
elif user_withdraw >= 10000:
    if user_withdraw % 1000 == 0:
        withdraw = user_withdraw // 1000
        if withdraw <= cash_1000:
            print(f"Your Transaction of {user_withdraw} has been Completed")
            cash_1000 = cash_1000 - withdraw
        else:
            print("The Amount is not Availbe, Enter Amount less then 20000")
    elif user_withdraw % 500 == 0:
        withdraw_1000 = user_withdraw // 1000
        cash_1000 = cash_1000 - withdraw_1000
        withdraw_500 = user_withdraw % 5000
        cash_500 = cash_500 - withdraw_500
        print(f"Your Transaction of {user_withdraw} has been Completed")
    else:
        print("Please Enter the Amount Multiple of 500")   
elif user_withdraw >= 5000:
    if user_withdraw % 500 == 0:
        withdraw = user_withdraw // 500
        if withdraw <= cash_500:
            print(f"Your Transaction of {user_withdraw} has been Completed")
            cash_500 = cash_500 - withdraw
        else:
            print("The Amount is not Availbe, Enter Amount less then 5000")
    elif user_withdraw % 500 == 0:
        withdraw_500 = user_withdraw // 500
        cash_500 = cash_500 - withdraw_500
        withdraw_500 = user_withdraw % 500
        cash_500 = cash_500 - withdraw_500
        print(f"Your Transaction of {user_withdraw} has been Completed")
    else:
        print("Please Enter the Amount Multiple of 500")
elif user_withdraw > 500:
    if user_withdraw % 500 == 0:
        withdraw = user_withdraw // 500
        if withdraw <= cash_500:
            print(f"Your Transaction of {user_withdraw} has been Completed")
            cash_500 = cash_500 - withdraw
        else:
            print("The Amount is not Availbe, Enter Amount less then 50000")
    else:
        print("Please Enter the Amount Multiple of 500")
else:
    print("Please Enter the amount alteast 500")
