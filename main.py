from operation import rent,rentReturn,getLandDict
from read import readLand
from write import rentedBill


def user_input():

    print("Welcome to Megha's Land Rental System ")
    readLand()
    search = input("Please select any option:\n1. Rent\n2. Return\n3.Exit\nYour Input: ")

    if search =="1" or search.lower()=="rent":
        info= rent()
        rentedBill(info)

    elif search =="2" or search.lower()=="return":       
        rentReturn()

    elif search =="3" or search.lower()=="exit":
        print("Thank you for using our service.Kindly rate us.")
    else:
        print("Invalid input.")


user_input()