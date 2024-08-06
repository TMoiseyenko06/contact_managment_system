import os 

#exports all of the current contacts into a .txt file
def export_contacts(contacts):
    with open('contacts.txt', 'w') as file:
        for item in contacts:
            for key, value in item.items():
                file.write(f"{key},{value[0]},{value[1]},{'None' if value[2] == '' else value[2]}")
            
#imports text from a .txt file and notifies the user if there has been an error
def import_contacts(file_path):
    try:
        contacts = []
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip().split(',')
                contacts.append({line[0]:[line[1],line[2],line[3]]})
    except Exception as e:
        print(f'An error accured while importing: {e}')
    else:
        return contacts