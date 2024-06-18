from datetime import datetime, date
from random import randint
from read import getLandDict,spacing

fileName = "landinfo.txt"

def rentedBill(info):
    lands = getLandDict()
    name = info[0]
    phone = info[1]
    rentingList = info[2]
    rentingDuration = info[3]

    invoiceID = randint(8000,780000)
    
    for i in range(len(rentingList)):
        rental_rate = int(lands[rentingList[0]][3])
        total = int(rentingDuration[0]) * rental_rate
        kittaNumber = str(rentingList[0])
        duration = str(rentingDuration[0])
        location = lands[rentingList[0]][0]
        direction = lands[str(rentingList[0])][1]
        anna = lands[str(rentingList[0])][2]
        rent = lands[str(rentingList[0])][3]

    with open('bill.txt', 'w') as file:
            file.write(
        "----------------------------------------------------- Invoice ----------------------------------------------------"
    )
            file.write("\n\n\n")

            file.write("      Invoice ID:  "+ spacing(str(invoiceID), 88) + "Date: "+str(date.today()) )
            
            file.write(
        "\n\n    " + spacing("Customer Name: " + name, 70) )
            file.write(
        "\n\n    " + spacing("Phone Number: " + phone, 70) )
            file.write(
        "\n\n    " + spacing("10% will be charged as fine, if given duration exceeds.", 70) )
            
            file.write(
        "\n\n   ----------------------------------------------------------------------------------------------   \n\n"
    )
            file.write(
        "|    KittaNo.   |    Location   |  Direction  |  Anna  |    Rent   |   Duration    |     Total    | \n\n"
    )  
            file.write("|  "+spacing(str(anna),6))
            
            file.write("|  "+spacing(str(kittaNumber),13))
            file.write("|  "+spacing(str(location),13))
            file.write("|  "+spacing(str(direction),11)) 
            file.write("|  "+spacing(str(rent),9))
            file.write("|  "+spacing(str(duration),13))
            file.write("|  "+spacing(str(total),12) +"|")

            file.write(
        "\n\n   ----------------------------------------------------------------------------------------------   \n\n")



def returnedBill(kittaNo):
    a = getLandDict()
    invoiceID = randint(8000,780000)

    name = a[kittaNo][5]
    returned_on = date.today()
    # Parsing the rented_on date from the data
    rented_on = datetime.strptime(a[kittaNo][7],'%Y-%m-%d').date()


    if str(kittaNo) not in a:
        return "Invalid property ID."
    
    with open('bill.txt', 'w') as file:
            file.write(
        "----------------------------------------------------- Invoice ----------------------------------------------------"
    )
            file.write("\n\n\n")

            file.write("      Invoice ID:  "+ spacing(str(invoiceID), 88) + "Date: "+ str(returned_on))
            
            file.write(
        "\n\n    " + spacing("Customer Name: " + name, 70) )
            
            file.write(
        "\n\n   ----------------------------------------------------------------------------------------------   \n\n"
    )
            file.write(
        "|    KittaNo.   |    Location   |  Direction  |  Anna  |    Rent   |   Duration    |   Extra_duration  |    Fine    |     Total    | \n\n"
    )
            each = kittaNo

            kittaNumber = str(each)
            location = str(a[each][0])
            direction = str(a[each][1])
            anna = str(a[each][2])
            rent = int(a[each][3])
            duration = int(a[each][6])

            rental_rate = int(a[str(kittaNo)][3])
            rental_period = (returned_on - rented_on).days #calculates the difference in months using relativedelta.
            rented_period_in_month = round(rental_period / 30)
            total_rental_cost = rental_rate * rented_period_in_month
          
            late_months = max((rented_period_in_month  - int(duration)), 0)

            if duration < rental_period:
                fine_per_month = 1.1  # 10% fine
                total_fine =round(fine_per_month * rental_rate)
                total_cost = round(total_rental_cost + total_fine)
            else: 
                total_fine = 0
                total_cost = duration* int(str(a[str(kittaNo)][3]) )# no matter what, the cost will be according to the contract

            
            file.write("|  "+spacing(str(kittaNumber),13))
            file.write("|  "+spacing(str(location),13))
            file.write("|  "+spacing(str(direction),11))   
            file.write("|  "+spacing(str(anna),6))
            file.write("|  "+spacing(str(rent),9))
            file.write("|  "+spacing(str(duration),13))
            file.write("|  "+spacing(str(late_months),17))
            file.write("|  "+spacing(str(total_fine),10))
            file.write("|  "+spacing(str(total_cost),12) +"|")

            
    file.close()
# billCalculation('101','202201', '202208')


def writeNewData(d):

    fileex = open("landinfo.txt", "w")
        
    for each in d:
        fileex.write(each )
        for j in d[str(each)] :
            fileex.write(","+(str(j)).strip())
        fileex.write("\n")
   
    
    fileex.close()


t = getLandDict()
writeNewData(t)

def changeStatus(kittaNo, name, month, status):
    """
    Function to change the status of a land (Available/Not Available) and update customer details and renting duration.
    It will take :
        1) id (str): The ID of the land.
        2) cust (str): The name of the customer.
        3) month (int): The renting duration in months.
        4) status (str): The status of the land (Available/Not Available).
    """
    # Get lands data
    d = getLandDict()
    # Update customer details and renting duration
    d[kittaNo][5]=  name
    d[kittaNo][6]= month
    d[kittaNo][4] =status
    
    if str(status).strip()== "Available": 
        d[kittaNo][7] = "Renting date here"
        d[kittaNo][4] = "Available"
    else : 
       d[kittaNo][4] = "Not Available"
       d[kittaNo][7]= str(datetime.now().date())
    
    # Write updated data to the file
    writeNewData(d)
