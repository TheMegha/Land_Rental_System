from read import getLandDict, spacing
from write import returnedBill,rentedBill
from write import changeStatus
from datetime import date



def rent():
    lands = getLandDict()
    name = input("Enter your name :")
    phone = input("Enter your phone number: ")
    rentingList = []
    rentingDuration = []

    while True:

        try:
            # Get land ID
            landID = input("\nEnter kitta no. of the land: ")

            if landID not in lands.keys():

                print("\nEnter a valid land id.")

                continue

            elif landID in rentingList:

                print(
                    "\nThis land is already added to your invoice. Please select another one."
                )

                continue

            elif lands[landID][4] == " Not Available":

                print("\nThis land is already rented. Please select another one.")

                continue

            else:

                rentingList.append(landID)

        except:

            print("\nEnter a valid land id  e.")

        # Get renting duration
        while True:

            try:

                duration = int(input("\nFor how many months the land will be  rented? : "))

                if duration < 1 or duration > 360:

                    print("\nEnter months between 1 and 360 months.")

                    continue

                else:

                    rentingDuration.append(duration)

                    break

            except:

                print("\nEnter valid number of months.")

    # Updating status of rented lands
        for i in range(len(rentingList)):

            changeStatus(rentingList[i], name, rentingDuration[i],"Not Available")

        
        return [name, phone, rentingList, rentingDuration]


def rentReturn():
    d = getLandDict()
    
    returningLands = []

    # Loop to select land to return
    while True:
        landID = input("\nEnter kitta number of the land to return : ")
        if landID not in d:
            print("\nPlease choose a valid kitta number.")
            continue
        
        if d[landID][4] == "Available":
            print("\nThis land has not been rented yet. Please select another land.")
            continue    
        else:
            
            if landID in returningLands:
                print("\nThis land is already added to the bill. Please select another land.")
                continue

            else :
                returningLands.append(landID)
                break

    returnedBill(returningLands[0])

    changeStatus(returningLands[0],"None",0,"Available")
    
    return returningLands[0]