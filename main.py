import admin as aa
from user import User
import user
import ast
    
inp = int(input(" !welcome! Where You want to login select 1.Admin and 2.User and 3.Exit"))

if inp == 1:
    Username = input("Enter the username of admin: ")
    Password = input("Enter the password of admin: ")
    if aa.admin_keys[Username] == Password:
        print("*****You're successfully logged inn*****")
        with open("menu.txt") as f:
            data=f.read()
        f.close()
        menu=ast.literal_eval(data)
        print(menu)
        admin_crawler = True
        while admin_crawler:
            adm_choice = int(input("Choose the options of admin panel 1.ADD NEW ITEM 2.EDIT ITEM 3.VIEW INVENTORY 4.REMOVE ITEM 5.EXIT"))
            if adm_choice == 1:
                aa.add_new_food()
            elif adm_choice == 2:
                aa.edit_from_food()
            elif adm_choice == 3:
                aa.show_menu()
            elif adm_choice == 4:
                aa.remove_food()
            elif adm_choice ==5:
                print(f"You're Exit to the admin panel {Username}")
                admin_crawler = False
            else:
                print("This is the wrong selection please select valid option")
        else:
            exit()
    else:
        print("These are the wrong credentials! SORRY!!!")
elif inp == 2:
    userprofile=True
    while userprofile:
        
        ip=int(input("Welcome to the user panel choose 1 or 2--1.New user or 2.Registered User"))
        if ip==1:
            print('create Your Account')
            user.createuserid()
            print("account created successfully")
            userprofile=False
        elif ip==2:
            userprofile=False
                          
        else:
            ("Entered wrong credentials,Enter again")
    print("enter log in details ")
    username = input("Enter your username : ")
    usernameN=username
    password = input("Enter the password here: ")
    with open('Userdetail.txt') as f:   
        data = f.read()
    f.close()
    logininfo = ast.literal_eval(data)
    if username in logininfo:
        username=User(logininfo[username]['name'],logininfo[username]['address'],logininfo[username]['emailid'],logininfo[username]['phoneno'],logininfo[username]['username'],logininfo[username]['password'])
   
    if User.login(usernameN, password):
        print(f"You are logged in successfully {usernameN}")
        user_crawler = True
        while user_crawler:
            usr_choice = int(input(f"{username}, Enter the option 1.Place new order 2.Order history 3.update profile 4.Exit"))
            if usr_choice == 1:
                username.place_order()
            elif usr_choice == 2:
                print(f"Here is your order history, {username}")
                print(username.order_history)
            elif usr_choice == 3:
                username.update()
            elif usr_choice == 4:
                user_crawler = False
                print("You're Successfully looged out")
            else:
                print("You choose the invalid option")       
    else:
        print("These are the wrong credentials! SORRY!!!")
        
else:
    print("exiting the program")
    exit()

