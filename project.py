# Each contact needs a unique identifier as the outer key so either (name,phone,email)
# inner key needs to have all our values 
def new_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter your phone number")
    email = input("Enter your email")
    additional_info = input("any additonal information")
    contacts[email] = {name, phone, email, additional_info} # email outer key and inner has all the values 
    print("new contact added")

def edit_contact(contacts): # we are trying to edit a value that exist 
    email = input("enter the email you would like to edit") 
    if email in contacts:
        print("What is the new email?")
        new_contact(contacts)
        print("your contact has been changed")
    else:
        print("information not found")


def delete_contact(contacts): # delete function
    email = input("Enter the phone number you would like to delete: ")
    if email in contacts:
        del contacts[email]
        print("it has been deleted")
    else:
        print("nothing was found to delete")

def search_contact(contacts): # search function
    email = input("Enter the email you would like to find: ")
    if email in contacts:
        print("email has been found")
        print(contacts[email])
    else:
        print("nothing was found")

def display_contact(contacts): #display our contacts and set contact in the value
    print("for all contact! ")
    for contact in contacts.value():
        print(contact)

def main():
    contacts = {}
    print("Welcome to the Contact Management System!")
    while True:
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Quit")

        option = input("enter your action based on the number between 1-6: ")

        if option == '1':
            new_contact(contacts)
        elif option == '2':
            edit_contact(contacts)
        elif option == '3':
            delete_contact(contacts)
        elif option == '4':
            search_contact(contacts)
        elif option == '5':
            display_contact(contacts)
        elif option == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()


    




 
