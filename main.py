import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from csv import DictWriter




def addnewitem():  
    itemID = int(input("Enter item id: "))
    itemName = input("Enter item name: ")
    itemCost = int(input("Enter item cost: "))
    cat = input("Enter category: ")
    quantity = int(input("Enter Quantity: "))

    field_names = ['item_id', 'item_name', 'item_cost','category', 'quantity']
    dict = {'item_id': itemID, 'item_name': itemName, 'item_cost': itemCost,'category': cat, 'quantity': quantity}
    with open('./data/item-detail.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
        dictwriter_object.writerow(dict)
        f_object.close()
    print("")
    print("Appended Data Successfully")
    df = pd.read_csv('./data/item-detail.csv') 
    print(df)

def additemstatus(): 
    itemID = int(input("Enter item id: "))
    itemName = input("Enter item name: ")
    itemCost = int(input("Enter item cost: "))
    staffid = int(input("Enter staff id: "))
    itemStatus = input("Enter item status: ")
    field_name = ['item_id', 'item_name', 'item_cost','staff_id','item_status']
    dict = {'item_id': itemID, 'item_name': itemName, 'item_cost': itemCost,'staff_id': staffid, 'item_status': itemStatus}
    with open('./data/item-status.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=field_name)
        dictwriter_object.writerow(dict)
        f_object.close()
    print("")
    print("Appended Data Successfully")
    df = pd.read_csv('./data/item-status.csv')
    print(df)

def searchitem():
    item_name = input("Enter name of item: ")
    idf = pd.read_csv('./data/item-detail.csv')
    searchdf = idf.loc[idf["item_name"] == item_name]
    if searchdf.empty:
        print("No item with this name")
    else:
        print("Item details are: ")
        print(searchdf)

def removeitem():
    item_id = int(input("Enter item id: "))
    idf = pd.read_csv('./data/item-detail.csv')
    idf_status = pd.read_csv('./data/item-status.csv')
    idf_status = idf_status.drop(idf_status[idf_status["item_id"] == item_id].index)
    idf = idf.drop(idf[idf["item_id"] == item_id].index)
    idf.to_csv('./data/item-detail.csv', index = False)
    idf_status.to_csv('./data/item-status.csv', index = False)
    print("Item removed successfully")
    print(idf)

def showitem():
    idf = pd.read_csv('./data/item-detail.csv')
    print(idf)


def addstaff():
    staffID = int(input("Enter staff id: "))
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    post = input("Enter post: ")
    phone = input("Enter phone number: ")
    staffScore = int(input("Enter staff score: "))
    field_name = ['staff_id','first_name','last_name','post','phone_no','staff_score']
    dict = {'staff_id': staffID, 'first_name': firstName, 'last_name': lastName,'post': post, 'phone_no': phone, 'staff_score': staffScore}
    with open('./data/staff.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=field_name)
        dictwriter_object.writerow(dict)
        f_object.close()
    print("")
    print("Appended Data Successfully")
    df = pd.read_csv('./data/staff.csv')
    print(df)


def searchstaff():
    staffid = int(input('Enter staff id: '))
    isdf = pd.read_csv('./data/staff.csv')
    df = isdf.loc[isdf["staff_id"] == staffid]
    if df.empty:
        print("No staff found with given id")
    else:
        print(df)


def removestaff():
    staffid = int(input("Enter staff id: "))
    isdf = pd.read_csv('./data/staff.csv')
    isdf = isdf.drop(isdf[isdf["staff_id"] == staffid].index)
    isdf.to_csv('./data/staff.csv', index = False)
    print("Staff removed successfully")
    print(isdf)


def showdetail():
    isdf = pd.read_csv('./data/staff.csv')
    print(isdf)

def chart():
    print("Press 1 - Item and their cost")
    print("Press 2 - Staff and delivery")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        idf = pd.read_csv('./data/item-detail.csv')
        idf = idf[["item_name", "item_cost"]]
        idf.plot("item_name", "item_cost", kind='bar')
        plt.xlabel('Item Name ------->')
        plt.ylabel('Item Cost ------->')
        plt.show()
    elif choice == 2:
        idf = pd.read_csv('./data/staff.csv')
        idf = idf[["staff_id", "staff_score"]]
        idf.plot("staff_id","staff_score", kind='bar')
        plt.xlabel('Staff ID ----->')
        plt.ylabel('Staff Score ----->')
        plt.show()

    else:
        print("Invalid choice")



def showmenu():
    print("Press 1 - Add new item")
    print("Press 2 - Add item status")
    print("Press 3 - Search for an item")
    print("Press 4 - Remove an item")
    print("Press 5 - Show all item")
    print("Press 6 - Add new staff")
    print("Press 7 - Search for staff")
    print("Press 8 - Remove staff")
    print("Press 9 - Show details of staff")
    print("Press 10 - To view chart")
    print("Press 11 - To exit")
    choice = int(input("Enter your choice:  "))
    if choice == 1:
        addnewitem()
    elif choice == 2:
        additemstatus()    
    elif choice == 3:
        searchitem()
    elif choice == 4:
        removeitem()
    elif choice == 5:
        showitem()
    elif choice == 6:
        addstaff()
    elif choice == 7:
        searchstaff()
    elif choice == 8:
        removestaff()
    elif choice == 9:
        showdetail()
    elif choice == 10:
        chart()
    elif choice == 11:
        exit()



def code():
    print("--------------------------------------------------------------")
    print("                    WELCOME TO IMS ADMIN PANEL                ")
    print("--------------------------------------------------------------")
    showmenu()
    
    while True:
        print("--------------------------------------------------")
        print("Press 1 to run again")
        print("Press 2 to exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            showmenu()
        elif choice == 2:
            exit()
        else:
            print("Invalid Selection")

    
    

    

    exit()  #exit() should be in last line
    

    
