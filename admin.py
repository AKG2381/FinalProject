import ast
admin_keys = {"Ajeet": "Ajeet@123"}
with open("menu.txt") as f:   #accessing inventory from text file and opening it as dictionary
  data=f.read()
f.close()
menu=ast.literal_eval(data)

def add_new_food():
    global t
    t=max(menu.keys())+1
    foodid=t
    foodname = input("Enter the food name: ")
    price = int(input("Enter the price of the food: "))
    discount=int(input("Enter the discount on the food: "))
    Y=True
    while Y:
        if discount<price :
            Y=False
        else:
            ("discount must be less than price")
            discount=int(input("Enter the discount on the food again: "))
            if discount<price:
                Y=False
            else:
                Y=True           
    stock = int(input("Enter the stock value of food: "))
    if foodname in menu.keys():
        print(" food  is Present Already ")
    else:
        menu[foodid] = {
                    "FoodName": foodname,
                    "FoodID": foodid,
                    "Price": price,
                    "Discount":discount,
                    "Stock": stock
                    }
        a=open("menu.txt",'w')
        a.write(str(menu))
        a.close()
        print("The Food",foodname, "is successfully added")
    return menu



def edit_from_food():
    print(menu)
    foodid = int(input("Enter the foodid which you want to edit: "))
    foodinmenu=True
    if foodid in menu:
        foodinmenu=False
    else:
        print("food id  is not in menu")
        
    a = input("Enter the food name: ")
    b = int(input("Enter the price of food: "))
    d = int(input("Enter the discount on  the food: "))
    c = int(input("Enter the stock of the food: "))
    X = True
    while X:
        if b>d:
            menu[foodid]["FoodName"] = a
            menu[foodid]["Price"] = b
            menu[foodid]["Discount"]=d
            menu[foodid]["Stock"] = c
            X=False
        else:
            print("discount value is more than price")
            print("Enter Valid Values")
    a=open("menu.txt",'w+')
    a.write(str(menu))
    a.close()
    print("*****Edited item successfully*****")
    return menu

def show_menu():
    print("*****HERE IS THE LIST OF Food*****")
    for i in menu.values():
        print(i)
        

def remove_food():
    rem=True
    while rem:
        d = int(input("Enter the Food id which you want to remove: "))
        if d in menu:
          rem=False
        else:
          print('food ID not present in the inventory.')
          show()
    
    menu.pop(d)
    a=open("inventoryfile.txt",'w')
    a.write(str(menu))
    a.close()
    print('Removed food Successfully')
    return menu
