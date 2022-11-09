#Creating contact list

ExistingContacts = {
    1 : {
        "name" : "Emil",
        "number" : 219818,
        "address" : "76 Buttonwood Street Valdosta"
    },
    2 : {
        "name" : "Tobias",
        "number" : 2871238,
        "address" : "566 Panama City, FL 32404"
    },
    3 : {
        "name" : "Linus",
        "number" : 12323,
        "address" : "76 Bellevue St. Beaver Falls"
    }
}


def addtoContact():
    #get the last key from the contacts

    ContactinOrder = list(ExistingContacts.keys())[-1] + 1

    #get input from  the user to be saved

    while True:
        try:
            name = str(input('Enter contact name: '))
            number = int(input('Enter contact number: '))
            address = str(input('Enter contact address: '))

            ExistingContacts[ContactinOrder] = {
                "name" : "{}".format(name),
                "number" : number,
                "address" : "{}".format(address)
            }

            print("Contact " + name + " added succesfully! \n")
            break
        except ValueError:
            print("wrong input. Please enter format correctly. \n")
            break








