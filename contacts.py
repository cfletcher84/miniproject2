import re
contact_list = {}

def main_menu():
    while True:    
        try:
            print("""

Fletchers Contacts Organizer! 

Menu:
    
1. Add a contact
2. Edit an existing contact
3. Delete a contact
4. Search contacts
5. Display contacts
6. Export contacts to a text file
7. Quit
                              
""")
            user_navigation = int(input("What would you like to do? Select 1-7 : "))
            if user_navigation == 7:
                print("Thank you for using the app!")
                break
            elif user_navigation == 6:
                export_contact()
            elif user_navigation == 5:
                display_contact()
            elif user_navigation == 4:
                search_contact()
            elif user_navigation == 3:
                del_contact()
            elif user_navigation == 2:
                edit_contact()
            elif user_navigation == 1:
                add_contact()
        except ValueError:
            print("That was not a number, please select again.")

def add_contact():

    name = input("\nWhat is the contacts name? (Back) ")
    address = input('\nWhat is your address? : ')
    email = ""

    if name == 'Back' or address == 'Back' or email == 'Back':
        main_menu()
    else:
        while True:
            email = input("\nWhat is your contacts email adress? (Back) ")
            valid_email = re.search(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-z]{2,}', email)
            if valid_email:
                break
            else:
                print("Invalid email. Please try again.")

    contact_list[email] = [name, address]
    
    # contact_list[email] = {'name': name,'address': address}

    
    another_contact = input('\nWould you like to add another? (y/n) : ')
    
    if another_contact == 'y':
        add_contact()



def edit_contact():
    user_input = input('What is the name of the contact you would like to edit? : ')
    try:
        for k, v in contact_list.items():
            if v[0] == user_input:
                key = k
                break
        else:
            print(f'{user_input} does not exist in the list.')
            return
        edit = input('\nWhat would you like to edit? (name, address, email) : ')
        if edit == 'name':
            name = input('What is the new name> : ')
            contact_list[key][0] = name
            print(f'You successfully changed the name to {name}')
        elif edit == 'address':
            address = input('\nWhat is the new address? : ')
            contact_list[key][1] = address
        else:
            email = input('\nWhat is the new email?')
            contact_list[key] = email

    except Exception as e:
        print(f'You have an error at: {e}')

    edit_another = input("\nwould you like to edit another contact? (y/n): ")
    if edit_another == "y":
        edit_contact()


def del_contact():
    user_input = input(f'Who would you like to delete from your contact list? : ')
    try:
        for k, v in contact_list.items():
            if v[0] == user_input:
                key = k
        del contact_list[key]
        print(f'You succesfully deleted {user_input} from your contact list. ')

    except Exception as e:
        print(f'There was an error at: {e}')

def search_contact():
    user_input = input(f'Who would you like to search for from your contact list? : ')
    try:
        for k, v in contact_list.items():
            if v[0] == user_input:
                name = v[0]
                address = v[1]
                print(f'You found {name} who lives at {address} witt the following email: {k}')
    except Exception as e:
        print(f'There was an error at: {e}')

def display_contact():
    print('\nHere are your current contacts!')
    for k, v in contact_list.items():
        print(f'\n{v[0]} lives at {v[1]}. Email: {k}')

def export_contact():
    with open('contact_list.txt', 'w') as file:
        for k, v in contact_list.items():
            name = v[0]
            address = v[1]
            email = k
            file.write(f'\nName: {name}: Address: {address} Email: {email}')


main_menu()
print(contact_list)