#import contact list from the contact_list.py

from Contact_list import ExistingContacts    
from Contact_list import addtoContact

#Creating a menu view

def DisplayMenu():

    print("========================================================")
    print("   Welcome to Contact Books. What do you want to do?   |")
    print("========================================================")
    print("1. View contact                                        |")
    print("2. Change contact                                      |")
    print("3. Add contact                                         |")
    print("4. Delete contact                                      |")
    print("5. Exit                                                |")
    print("========================================================")

DisplayMenu()



def DisplayContacts():

    numCounter = 1
    print("================================================================================")
    print("|No.| Name            | Number           | Address:                            |")
    print("================================================================================")


    for eachContact in ExistingContacts.values():



        print("|{no} .| {name:<15} | {number:<13}  | {address:<35} |"
        .format(no = numCounter, name = eachContact["name"], number = eachContact["number"],
            address = eachContact["address"]))

        numCounter = numCounter + 1

    print("================================================================================")

#DisplayContacts()



def Update_Contact():   #Updates the contact

    isUpdate = False
    DisplayContacts()

    ExistedContact = str(input('Enter contact name you would like to edit: '))


    for contact in ExistingContacts.values():     #loops through the existed contact from the contact_list.py
        if ExistedContact in contact.values():
            print(ExistedContact + 'found and can be edited!')

            try:
                newName = str(input("Enter contact new name: "))
                newNumber = int(input("Enter contact number: "))
                newAddress = str(input("Enter contact address: "))

                contact.update({"name" : "{}". format(newName)})
                contact.update({"number" : newNumber})
                contact.update({"address" : "{}". format(newAddress)})
                isUpdate = True
                print("Data '{}' succesfully changed to '{}'.\n".format(ExistedContact, newName))

            except ValueError:
                print("Format error. Please enter a correct number.")

        if isUpdate == False:
            print("Data not found. Please enter a correct name\n")
            DisplayMenu()




def Delete_Contact():
    isDelete = False
    DisplayContacts()

    name = str(input("Enter contact's name you want to delete: "))

    for contactPlace, contactInfo in list(ExistingContacts.items()):
        if contactInfo["name"] == name:
            del ExistingContacts[contactPlace]
            DisplayContacts()
            print("Data ''{}'' deleted Succesfully!\n".format(name))
            isDelete = True
    if isDelete == False:
        print("Data not found!\n")


def SelectOption():
    repeat = True
    while  repeat == True:
        try:
            ChooseOption = int(input('Please an option between 1 to 5: '))
        except ValueError:
            print("Only integers are allowed, so please enter any integer between 1 and 5")

        #ChooseOption = 0
        #if ChooseOption > 0 and ChooseOption < 6:
          #  repeat = False


        if ChooseOption == 1:
            DisplayContacts()
            DisplayMenu()



        elif ChooseOption == 2:
            print("\n==============")
            print("Change Contact")
            print("==============")
            Update_Contact()
            DisplayMenu()



        elif ChooseOption == 3:
            print("\n===========")
            print("Add Contact")
            print("===========")
            addtoContact()
            DisplayMenu()



        elif ChooseOption == 4:
            Delete_Contact()
            DisplayMenu()
            print("4 selected -- Delete contact")


        elif ChooseOption == 5:
            print("Bye!! -- Exit")
            break
        else:
            print("Sorry this option is not available")

SelectOption()




