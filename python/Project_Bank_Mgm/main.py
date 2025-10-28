import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []         #dummy data loaded with json data

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
    except Exception as err:
        print(f"an exception occured as {err}")

    @staticmethod
    def __update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k = 3)
        spchar = random.choices("!@#$%^&*" , k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)


    def createAccount(self):
        info = {
            "name": input("Tell your name"),
            "age" : int(input("Tell your age")),
            "email" : input("Tell your email"),
            "pin" : int(input("Tell your pin")),
            "accountNo" : Bank.__accountgenerate(),
            "balance" : 0
        }
        if info['age'] < 18 or len(str(info['pin']))!=4:
            print("sorry you cannot create your account")
        else:
            print("Account created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number")

            Bank.data.append(info)

            Bank.__update()


    def depositmoney(self):
        accnumber = input("Please tell your account number")
        pin = int(input("Enter your pin"))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Sorry! No data found")
        else:
            amount = int(input("How much you want to deposit"))
            if amount > 10000 or amount < 0:
                print("Sorry the amount is more than 10000. You can deposit below 10000 and above 0")
            
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print(f"Amount deposited successfully and current balance is {userdata[0]['balance']}")
                

    def withdrawmoney(self):
        accnumber = input("Please enter your account number")
        pin = int(input("please enter pin"))
        
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        if not userdata:
            print("Sorry! No data found")
        else:
            amount = int(input("How much money you want to withdraw"))
            if amount > 10000 or amount < 0:
                print("Sorry you can't withraw money more than 10000 and less than 0")
            if amount > userdata[0]['balance']:
                print("Balance not sufficient to withdraw")
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print(f"Amount withdraw successfully and current balance is {userdata[0]['balance']}")


    def showdetails(self):
        accnumber = input("Enter your account number")
        pin = int(input("Enter pin"))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Sorry! No User Found")
        else:
            # print(f"Name: {userdata[0]['name']}")
            # print(f"Age: {userdata[0]['age']}")
            # print(f"email: {userdata[0]['email']}")
            # print(f"Balance: {userdata[0]['balance']}")
            print("Your infromation is -")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accnumber = input("Enter your account number")
        pin = int(input("Enter pin"))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("No user found")
        else:
            print("you cannot change the age,account number,balance")

            print("Fill the details for change or leave it if no change")

            newdata = {
                "name": input("please enter new name or press enter to skip"),
                "email": input("please enter new email or press enter to skip"),
                "pin": input("please enter new pin or press enter to skip")
            }
            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
            
            newdata['age'] = userdata[0]['age']
            newdata['accountNo'] = userdata[0]['accountNo']
            newdata['balance'] = userdata[0]['balance'] 

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            
            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
            
            Bank.__update()
            print("details updated successfully")
                

    def delete(self):
        accnumber = input("Enter your account number")
        pin = int(input("Enter pin"))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("No user found")
        else:
            check = input("Press y if you actually want to delete the account or press n")

            if check == 'n' or check == 'N':
                print("Bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted successfully")
                Bank.__update()


user = Bank()

print("Press 1 for creating an account")
print("Press 2 for Deposit Money")
print("Press 3 for Withdraw money")
print("Press 4 for Details")
print("Press 5 for Update details")
print("Press 6 for deleting account")

check = int(input("tell your response"))

if check == 1:
    user.createAccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 5:
    user.delete()