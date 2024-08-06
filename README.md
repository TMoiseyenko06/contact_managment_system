# Contact Manegment System Project 

A simple Contact Managment system Built on python that supports a variety of functions with more on the way!

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)


## Installation 
1. Clone the repository:
```
    git clone https://github.com/TMoiseyenko06/contact_managment_system
```

## Usage 

- Make sure that all of the files and directories are in the same directory orelse none of the functions will work!
- Running [main.py](/main.py) will start the progam in the command line.

## Functions 

- [Add_Contact](#add-contact)
- [Remove_Contact](#remove-contact)
- [Edit_Contact](#edit-a-contact)
- [Search_Contact](#search-contact)
- [Export_Contacts](#export-contacts)
- [Import_Contacts](#import-contacts)

    ### Add Contact
    
    The Program asks you to enter a Name, a Phone number, an Email, and additional info about the contact and then appends it to the contacts list.

    ### Remove Contact

    The Program asks you to enter the Name of a contact, it then tries to delete it from your list. If no contact ahs the name it will do nothing and tell you to try again.

    ### Edit a contact

    The programs once again asks you for the name of a contact, it then asks you what you would like to edit and edits it. If no contact with that name exist it will do nothing and tell you to try again.

    ### Search Contact

    The program asks you for the name of the contact and it will show you all of that contacts information. If no contact is found it will tell you to try again.

    ### Export Contacts

    The programs exports all of your current contacts into a text file named [contacts.txt]. 
    The data is formatted in the following way:
        
        Name1,Phone1,email1,additional1
        Name2,Phone2,email2,additional2
        etc...

    ### Import Contacts

    The prgams asks you for the path to a file you would like to import from and imports all of the contacts.

    The file MUST be in the following format:

        Name1,Phone1,email1,additional1
        Name2,Phone2,email2,additional2
        etc...
