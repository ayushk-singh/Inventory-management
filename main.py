from os import read
from pickle import FALSE
import pandas as pd
import numpy as np

def addnewitem():
    print("Add item working")

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
    print("show item working")

def addstaff():
    print("add staff working")

def searchstaff():
    print("search staff working")

def removestaff():
    print("remove staff working")

def showdetail():
    print("show detail working")

def chart():
    print("chart working")



def showmenu():
    print("Press 1 - Add new item")
    print("Press 2 - Search for an item")
    print("Press 3 - Remove an item")
    print("Press 4 - Show all item")
    print("Press 5 - Add new staff")
    print("Press 6 - Search for staff")
    print("Press 7 - Remove staff")
    print("Press 8 - Show details of staff")
    print("Press 9 - To view chart")
    print("Press 10 - To exit")
    choice = int(input("Enter your choice:  "))
    if choice == 1:
        addnewitem()
    elif choice == 2:
        searchitem()
    elif choice == 3:
        removeitem()
    elif choice == 4:
        showitem()
    elif choice == 5:
        addstaff()
    elif choice == 6:
        searchstaff()
    elif choice == 7:
        removestaff()
    elif choice == 8:
        showdetail()
    elif choice == 9:
        chart()
    elif choice == 10:
        exit()



def code():
    print("--------------------------------------------------------------")
    print("                    WELCOME TO IMS ADMIN PANEL                ")
    print("--------------------------------------------------------------")
    showmenu()
    
    

    

    exit()  #exit() should be in last line
    

    
