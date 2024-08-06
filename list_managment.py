#Searches the contact list for the contact and returns all the information if the conact exists
def search(contact,list):
    for item in list:
        for key in item.keys():
            if key == contact:
                return item

#adds a contact to the contact list
def add_contact(contact,list):
    number = input("What is {contact}'s Phone Number?")
    email = input("What is their E-Mail?")
    additional = input("Is there any additional info you would like to add? (y/n)")
    if additional == 'y':
        additional = input("What have you like to add?")
    else:
        additional = ''
    list.append({contact:[number,email,additional]})

#checks if conact exists and then removes it if it does
def remove_contact(contact,list):
    contact = search(contact,list)
    if not contact:
        print('Not a valid contact, please try again.')
    else:
        list.pop(list.index(contact))

#Takes a contact name and returns all the info about it if it exists
def search_contact(contact,list):
    searched = search(contact,list)
    if not searched:
        print('Contact not found, Please try again.')
    else:
        info = searched[contact]
        print(f'''Contact Name: {contact}
Phone Number: {info[0]}
E-Mail: {info[1]}
Additional Info: {'None' if info[2] == '' else info[2]}''')

#Allows the user to edit all aspects of a contact
def edit_contact(contact,list):
    searched = search(contact,list)
    if not searched:
        print('Contact not found, Please try again.')
    else:
        try:
            option = int(input('''What would you like to edit?
                        1. Name
                        2. Phone Number
                        3. E-Mail
                        4. Additional information'''))
        except:
            print('Not a vlaid number please try again.')
        else:
            if option == 1:
                change = input(f"What would you like to change {contact}'s name to?")
                list[list.index(searched)] = {change:[searched[contact][0],searched[contact][1],searched[contact][2]]}
            elif option == 2:
                print(f"{contact}'s Phone Number is currently: {searched[contact][0]}")
                change = input("What would you like to change it to?")
                list[list.index(searched)] = {contact:[change,searched[contact][1],searched[contact][2]]}
            elif option == 3:
                print(f"{contact}'s E-Mail is currently {searched[contact][1]}")
                change = input('What would you like to change it to?')
                list[list.index(searched)] = {contact:[searched[contact][0],change,searched[contact][2]]}
            elif option == 4:
                print(f"{contact}'s Additional Information is currently {searched[contact][2]}")
                change = input('What would you like to change it to?')
                list[list.index(searched)] = {contact:[searched[contact][0],searched[contact][1],change]}
        finally:
            return list

#displays all of the current contacts in a formatted and neat way
def display_contacts(list):
    for item in list:
        for key, value in item.items():
            print(f'''\nContact Name: {key}
Phone Number: {value[0]}
E-Mail: {value[1]}
Additional Info: {'None' if value[2] == '' else value[2]}''')