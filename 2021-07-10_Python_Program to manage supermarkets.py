#Python program to manage supermarkets
# UK supermarkets

items =[]

while True:

    print("----------------Welcome to the SuperMarket-------")
    print("1. View Items\n2. Add Items for Sale\n3. Purchase Items\n4. Search Items\n5. Edit Items\n6. Exit")
    option = input("Enter the Number of your Option:")

    if option == "1":
        #----------------------View Items-------------------------
        print("Total Inventory in the Store are:",len(items))
        while len(items) !=0:
            print("Stock Available in the Supermarket.")
            for item in items:
                for key, value in item.items():
                    print(key, ":", value)
            break

    elif option == "2":
        #---------------------------Add Items-----------------------
        print("To add an Item , Please fill in the form ")
        item = {}
        item["name"] = input("Item Name:")
        while True:
            try:
                item["quantity"] = int(input("Item Quantity: "))
                break
            except ValueError:
                print("Enter Numeric Digits")
        while True:
            try:
                item["price"] = int(input("Price £ : "))
                break
            except ValueError:
                print("Enter Numeric Digits")
        print("Successfully Added.")
        items.append(item)

    elif option == "3":
        #-------------------Purchase Items----------------------------
        print(items)
        purchase_item = input("Which Item do you want to purchase? Enter Name:")
        for item in items:
            if purchase_item.lower()== item["name"].lower():
                if item["quantity"] !=0:
                    print("Pay",item["price"],"at checkout counter.")
                    item["quantity"] -= 1
                else:
                    print("Item out of Stock.")

    elif option == "4":
        #-------------------------Search Items---------------------------
        find_item = input("Enter the Items\'s name to search in inventory : ")
        for item in items:
            if item["name"].lower() == find_item.lower():
                print("The Item Named:" + find_item + " is displayed below with its details")
                print(item)
            else:
                print("Item not Found.")

    elif option == "5":
        #------------------------------Edit Items----------------------------
        item_name = input("Enter the Name of the Item that you want to Edit:")
        for item in items:
            if item_name.lower() == item["name"].lower():
                print("Current Details of" + item_name)
                print(item)
                item["name"] = input("Item Name:")
                while True:
                    try:
                        item["price"]= int(input("Price £ :"))
                        break
                    except ValueError:
                        print("Enter Numeric Digits")
                print("Successfully Updated.")
                print(items)
            else:
                print("Item Not Found")

    elif option == "6":
        #---------------------------Exiting---------------
        break
    else:
        print("Invalid Option")
                
                
            
                    
                                           
        

                
    
