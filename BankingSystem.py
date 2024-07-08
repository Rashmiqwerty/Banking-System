current_amount=0
def withdraw():
    global current_amount
    print("Enter amount you want to withdraw: ")
    debited=int(input())
    if current_amount>debited:
        current_amount-=debited
    print(debited,"amount  successfully debited")
    print("Your Current Amount is :",current_amount)
    print("Thank You!!!")

def deposit():
    global current_amount
    print("Enter amount you want to deposit:")
    deposit=int(input())
    current_amount+=deposit
    print("Your Current Amount is :",deposit)
    print("Thank you!!!")

def checkbalance():
    global current_amount
    print("Your Current amount is: ",current_amount)
    print("Thank You!!!")
    
def main():   
    
    while(True):
        print("1.Withdraw:/n ")
        print("2.Deposit:/n")
        print("3.Check Balance:/n")
        print("4.Exit: ")
        print("Enter Your Choice: ")
        a=int(input())

        if a==1:
            withdraw()
        elif a==2:
            deposit()
        elif a==3:
            checkbalance()
        else:
            print("Exit.......")
            break

    
if __name__=='__main__':
    main()
