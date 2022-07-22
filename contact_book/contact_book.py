from database_function import *
from user import *


def right_phone_number(phone_number):
    while not phone_number.isdigit() or len(phone_number) != 9:  # only polish numbers
        print('Only digits and 9 characters long')
        phone_number = input('Input number: ')
    return phone_number


def are_phone_number_in_database(phone_number):
    cursor_object.execute(f'select 1 from User where phone_number={phone_number}')
    if cursor_object.fetchone():  # if phone number is in database
        return True
    return False


def validate_data(digits, valid_digits='1234'):  # check input for edit function
    while True:  # after this loop we have validate data
        if len(digits) < 1 or len(digits) > 4:
            print('Min one digit, max four digits"')
            digits = input()
            continue

        for digit in digits:
            if digit not in valid_digits:
                print('Only "1234"')
                digits = input()
                continue
        else:
            break

    return digits


def create_set_for_edit_function(digits):

    for_sql = []
    for char in digits:  # will be update attributes
        if char == '1':
            new_name = input('Input name: ')
            for_sql.append(f'name = "{new_name}"')
        if char == '2':
            new_phone_number = right_phone_number(input('Input number: '))
            if are_phone_number_in_database(new_phone_number):
                print('This phone number already in database.Error')
                break
            else:
                for_sql.append(f'phone_number = "{new_phone_number}"')
        if char == '3':
            new_address = input(f'Input address: ')
            for_sql.append(f'address = "{new_address}"')
        if char == '4':
            new_email_address = input('Input email_address: ')
            for_sql.append(f'email_address = "{new_email_address}"')

    # good format
    question = ''
    for line in for_sql:
        question += line + ' ,'

    return question


def add_contact():
    name = input('Input name: ')
    phone_number = right_phone_number(input('Input number: '))
    if are_phone_number_in_database(phone_number):
        print('This phone number already in database.Error')
        return

    details = input('Would you like to add address and email_address? Press "yes" or "no": ')
    while details != 'yes' and details != 'no':
        print('Input "yes" or "no"')
        details = input('Would you like to add address and email_address? Press "yes" or "no": ')

    if details == 'yes':
        address = input('Input address: ')
        email_address = input('Input email_address: ')
        user = User(name, phone_number, address, email_address)
    else:
        user = User(name, phone_number)

    user = user.user_information()

    sql = '''INSERT INTO USER(name, phone_number, address, email_address)
                 VALUES(?,?,?,?) '''
    cursor_object.execute(sql, user)
    connection_object.commit()


def edit_contact():
    phone_number = right_phone_number(input('Enter number of contact which you would like to edit: '))

    if are_phone_number_in_database(phone_number):  # if contact is in database

        print('''Enter all digits in one line without separators that correspond to the data you would like to edit:
"1" - name 
"2" - phone_number
"3" - address
"4" - email_address''')

        digits = validate_data(input())  # get which attribute should update
        # print(digits)

        question = create_set_for_edit_function(digits)

        sql = f'UPDATE User SET {question[:-2]} where phone_number={phone_number}'
        # print(sql)

        cursor_object.execute(sql)
        connection_object.commit()
    else:
        print('This phone number is not in the database.Error')


def delete_contact():
    phone_number = right_phone_number(input('Enter number of contact which you would like to delete: '))

    if are_phone_number_in_database(phone_number):  # if contact is in database
        sql = f'DELETE FROM User WHERE phone_number={phone_number}'
        cursor_object.execute(sql)
        connection_object.commit()
    else:
        print('This phone number is not in the database.Error')


def see_contacts():
    cursor_object.execute('select * from User')
    rows = cursor_object.fetchall()
    for row in rows:
        print(row)


def contact_book():
    while True:
        print()
        print('Enter "0" for exit')
        print('Enter "1" to add new contact')
        print('Enter "2" to edit contact')
        print('Enter "3" to delete contact')
        print('Enter "4" to see details of all contacts')

        button = input('Enter digit: ')

        if button == '1':
            add_contact()
        elif button == '2':
            edit_contact()
        elif button == '3':
            delete_contact()
        elif button == '4':
            see_contacts()
        elif button == '0':
            break
        else:
            print('Wrong button')
            continue


main()  # connection to the database

connection_object = create_connection('contact_book.db')
cursor_object = connection_object.cursor()


contact_book()  # main loop
