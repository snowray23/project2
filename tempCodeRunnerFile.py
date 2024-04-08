def new_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter your phone number")
    email = input("Enter your email")
    additional_info = input("any additonal information")
    contacts[email] = {name, phone, email, additional_info}
    print("new contact added")

 
