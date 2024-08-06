import list_managment as man
import file_managment as fil

def main():
    contact_list = []
    while True:
        try:
            option = int(input('''\nWelcome to the Contact Management System! 
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file *BONUS*
8. Quit'''))
        except:
            print("Error, please enter a valid number.")
        else:
            if option <= 4:
                contact = input("What is the name of the contact?")
                if option == 1:
                    man.add_contact(contact,contact_list)
                elif option == 2:
                    contact_list = man.edit_contact(contact,contact_list)
                elif option == 3:
                    man.remove_contact(contact,contact_list)
                else:
                    man.search_contact(contact,contact_list)
            else:
                if option == 5:
                    man.display_contacts(contact_list)
                elif option == 6:
                    fil.export_contacts(contact_list)
                elif option == 7:
                    file_name = input('what is the path to the file to import from?')
                    contact_list = fil.import_contacts(file_name)
                else:
                    break

if __name__ == "__main__":
    main()