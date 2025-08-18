# Contact Management System

import json # for saving and loading data to files
import re # for validating email and phone number
import os # for checking if the files exist

# creating a class

class Contact:
    # To represent each persons information
    
    # creating a constructor
    def __init__(self,name,email,phone,address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
    
    # How will the contact look when we print it
    def __str__(self):
        return f"{self.name}-{self.email}-{self.phone}"
    
    # convert obj data to dict
    def to_dict(self):
        # returning a dictionary
        return {
            'name':self.name,
            'email':self.email,
            'phone':self.phone,
            'address':self.address
        }
    # create a obj from a dict
    @staticmethod
    def from_dict(contact_dict):
        return Contact(
            contact_dict['name'],
            contact_dict['email'],
            contact_dict['phone'],
            contact_dict['address'],
        )
    
# This is where I will store my contacts
# objs stored in this global variable
contacts = []
    
def save_contacts():
    # saves contact information to JSON file
    try:
        # convert contact objs into dict
        obj_dict = [contact.to_dict() for contact in contacts]
        
        with open("contacts.json","w") as file:
            file.dump(obj_dict,file,indent=2)
        
        print("Contacts saved")
    except Exception as e:
        print(f"Error saving contact: {e}")
    
    
def load_contacts():
    global contacts
    try:
        # check if the file exists
        if not os.path.exists("contacts.json"):
            contacts = []
            return 
        
        # Load contact from JSON file and convert to Contact Objects
        with open("contact.json",'r') as file:
            contact_dicts = json.load(file)
            contacts = [Contact.from_dict(cd) for cd in contact_dicts]
            
        print(f"File loaded {len(contacts)} contacts")
    except Exception as e:
        print(f"File error loading contact {e}")
        contacts = []
            

def add_contact():
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    phone = input("Enter phone: ").strip()
    address = input("Enter address: ").strip()    
    
    # create and add contact
    contact = Contact(name,email,phone,address)
    contacts.append(contact)
    save_contacts()
    
    print("Contact added successfully")
    
def search_contacts():
    if not contacts:
        print("No contacts to search")
        return
    print(" Search Contacts")
    print("1. Name (partial match)")
    print("2. Email domain")
    print("3. Phone area code")
    print("4. All fields")
    
    try:
        option = int(input("Search Option: "))
    except ValueError:
        print("Please enter a number!")
        return 
    
    found_contacts = []
    
    if option == 1:
        search_name = input("Enter name to search: ").lower()
        found_contacts = [c for c in contacts if search_name in c.name.lower()]
        
    elif option == 2:
        domain = input("Enter email domain: ").lower()
        found_contacts = [c for c in contacts if domain in c.email.lower()]
    
    elif option == 3:
        area_code = input("Enter area code: ")
        found_contacts = [c for c in contacts if area_code in c.phone]
        
    elif option == 4:
        search_term = input("Search all fields: ")
        found_contacts = [c for c in contacts if 
                          search_term in c.name.lower() or
                          search_term in c.email.lower() or
                          search_term in c.phone or
                          search_term in c.address.lower()]
        
    else:
        print("Invalid Option")
        return

    if found_contacts:
        print(f"Found {len(found_contacts)} contact(s)")
        for i,info in enumerate(found_contacts,1):
            print(f"{i}. {info}")
            print(f"Address: {info.address}")
    else:
        print("No Contacts Found.")
    
    
def display_all_contacts():
    if not contacts:
        print("No contacts saved!")
        return 
    print(f" All Contacts ")
    for i,contact in enumerate(contacts,1):
            print(f"{i}. {contact}")
            print(f"Address: {contact.address}")
        

           
def delete_contact():
    if not contacts:
        print("No contacts to delete!")
    
    print("Delete Contact")
    
    for i,contact in enumerate(contacts,i):
        print(f"{i}. {contact}")
    
    try:
        choice = int(input(f"Enter contact number to delete (1-{len(contacts)}): "))
        
        # validate choice
        if 1 <= choice <= len(contacts):
            deleted_contact = contacts.pop(choice - 1)
            save_contacts()
            print(f"Deleted: {deleted_contact.name}")
                    
        else:
            print("Invalid contact number!")
    
    except ValueError:
        print("Please enter a valid number")
        
def main_menu():
    """
    Main program loop
    
    while True creates infinite loop
    break exits the loop
    continue skips to next iteration
    """
    print(" Contact Management System")
    
    while True:
        print("1. Add Contact")
        print("2. Search Contacts")
        print("3. Display All Contacts")
        print("4. Delete Contact")
        print("5. Show Statistics")
        print("6. Exit")
        
        try:
            choice = int(input("Choose option: "))
            
            if choice == 1:
                add_contact()
            elif choice == 2:
                search_contacts()
            elif choice == 3:
                display_all_contacts()
            elif choice == 4:
                delete_contact()
            elif choice == 5:
                show_statistics()
            elif choice == 6:
                print("👋 Goodbye!")
                break
            else:
                print(" Invalid option! Please choose 1-6.")
        
        except ValueError:
            print(" Please enter a valid number!")
        except KeyboardInterrupt:
            print("\n Goodbye!")
            break

def main():
    """
    Main function - entry point of program
    
    This runs when you execute the script
    """
    load_contacts()  # Load existing contacts from file
    main_menu()      # Start the main program

# This runs only when script is executed directly (not imported)
if __name__ == "__main__":
    main()
