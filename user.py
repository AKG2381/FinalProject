import admin as ad
import ast

with open('Userdetail.txt') as f:    #getting login and user details from the text file as a dictionary
    data = f.read()
f.close()
logininfo = ast.literal_eval(data)
def createuserid(): 
    print("Please complete the registration")
    
    name=input("Enter  your full name :")
    address=input('enter your address:')
    phoneno=int(input("Enter  your mobile number :"))
    emailid=input("enter your emailid :")
    userind=True
    while userind:       
        U=input("create a username you want :")
        if U in logininfo:
            print("username already there")
        else:
            username=U
            userind=False   
    password=input("Create a Password: ")
    details={username:{'name':name,'address':address,'phoneno':phoneno,"emailid":emailid,'username':username,'password':password}
                 }
    logininfo.update(details)
    a=open('Userdetail.txt','w+')
    a.write(str(logininfo))
    a.close()
with open("menu.txt") as f:
    data=f.read()
f.close()
global d
menu=ast.literal_eval(data)
d=menu
class User(object):
    login_info = {}

    def __init__(self,name,address, emailid ,phoneno,username, password):
        self.name = name
        self.address = address       
        self.emailid = emailid
        self.phoneno = phoneno
        self.username=username
        self.password = password
        User.login_info[self.username] = self.password
        self.profile={'Name: ',name}
        self.order_history = {}
    

    @classmethod
    def login(cls, username, password):
        if cls.login_info.get(username) == password:
            return True
        else:
            return False

    def update(self):
        updatetf=True
        while updatetf:
            updateidup=int(input('''What do you want to change?
                           1.Name
                           2.Address
                           3.Phone no
                           4.Email
                           5.Password
                           6.Exit
                           enter no.'''))
            #updateidup=updateid.upper()
            
            if updateidup==1:
                newname=input('New Name: ')
                self.name=newname
                print("name updated successfully")
            elif updateidup==2:
                newad=input('New Address: ')
                self.address=newad
                print("Address updated successfully")
            elif updateidup==3:
                newph=input('Enter Phone Number: ')
                self.phoneno=newph
                print("phoneno updated successfully")
            elif updateidup==4:
                newemail=input('Enter Mail ID: ')
                self.emailid=newemail
                print("emailid updated successfully")
            elif updateidup==5:
                newpwd=input('Enter New Password: ')
                self.password=newpwd
                print("password updated successfully")
            elif updateidup==6:
                print('Exiting update tab.')
                updatetf=False
            else:
                print('Wrong input.')
            
    def place_order(self):
        menu=d
        print(menu)
        print("What you want to order here in the Inventory")
        print(ad.show_menu())
        user_choice = int(input("If you want to order then select 1.YES 2.NO"))
        if user_choice == 1:
            n=int(input("Enter how many  food items do you want to Order:"))
            x,y,n,m=0,0,0,0
            for i in range(n):           
                    foodid = int(input("Enter the Food id here: "))
                    quan = int(input("Enter the quantity of the food: "))
                    n=menu[foodid]["Price"] * quan
                    m=menu[foodid]["Discount"] * quan
                    x += menu[foodid]["Price"] * quan
                    y+=menu[foodid]["Discount"] * quan
                    self.order_history[foodid] = {
                        "Food Name": menu[foodid]["FoodName"],
                        "Price": menu[foodid]["Price"],
                        "Discount":menu[foodid]["Discount"],
                        "Quantity": quan,
                        "total cost": n-m
                    }
                    
                       
            again_ask = int(input("Are you still want to order this Enter 1.YES or 2.NO: "))
            if again_ask == 1:
                print("It costs you",x,"but you got a total Discount of",y,"Hence You need to pay only",x-y,"INR in total")
                print("You're all set for this order")
                print("You're order is successfully placed")
            elif again_ask == 2:
                print("This Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("You select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")
