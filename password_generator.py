import random


def generate_password(length, chars):
    password = ''.join(random.sample(chars, length))
    return password


def yes_or_no(answer):
    if answer == 'yes' or answer == 'no':
        return False
    return True


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

how_many_passwords = input('The number of passwords to generate: ')
while not how_many_passwords.isdigit():
    print('You did not enter a number')
    how_many_passwords = input('The number of passwords to generate: ')
if how_many_passwords == '0':
    print('Ok. You do not need any password')
    exit()

len_of_password = input('Password length: ')
while not len_of_password.isdigit() or len_of_password == '0':
    print('You did not enter a number, or entered a zero')
    len_of_password = input('Password length: ')


digits_should = input('Should the digits 0123456789 be included? "yes" or "no": ')
while yes_or_no(digits_should):
    digits_should = input('Should the digits 0123456789 be included? "yes" or "no": ')
if digits_should == 'yes':
    chars = chars + digits

lowercase_letters_should = input('Should lowercase letters abcdefghijklmnopqrstuvwxyz be included? "yes" or "no": ')
while yes_or_no(lowercase_letters_should):
    lowercase_letters_should = input('Should lowercase letters abcdefghijklmnopqrstuvwxyz be included? "yes" or "no": ')
if lowercase_letters_should == 'yes':
    chars = chars + lowercase_letters

uppercase_letters_should = input('Should uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ be included? "yes" or "no": ')
while yes_or_no(uppercase_letters_should):
     uppercase_letters_should = input('Should uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ be included? "yes" or "no": ')
if uppercase_letters_should == 'yes':
    chars = chars + uppercase_letters

punctuation_should = input('Should symbols !#$%&*+-=?@^_? be included? "yes" or "no": ')
while yes_or_no(punctuation_should):
    punctuation_should = input('Should symbols !#$%&*+-=?@^_? be included? "yes" or "no": ')
if punctuation_should == 'yes':
    chars = chars + punctuation


for i in range(int(how_many_passwords)):
    password = generate_password(int(len_of_password), chars)
    print(password)