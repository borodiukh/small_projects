import random

def generate_password(length, chars):
    password = ''.join(random.sample(chars, length))
    return password

def yes_or_no(answer):
    if answer == 'yes' or answer == 'no':
        return False
    else:
        return True

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

how_many_passwords = input('Кількість паролів для генерації: ')
while not how_many_passwords.isdigit():
    print('Ви ввели не цифру')
    how_many_passwords = input('Кількість паролів для генерації: ')

len_of_password = input('Довжина пароля: ')
while not len_of_password.isdigit():
    print('Ви ввели не цифру')
    len_of_password = input('Довжина пароля: ')

digits_should = input('Включать ли цифры 0123456789? "yes" or "no": ')
while yes_or_no(digits_should):
    digits_should = input('Включать ли цифры 0123456789? "yes" or "no": ')
if digits_should == 'yes':
    chars = chars + digits

lowercase_letters_should = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? "yes" or "no": ')
while yes_or_no(lowercase_letters_should):
    lowercase_letters_should = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? "yes" or "no": ')
if lowercase_letters_should == 'yes':
    chars = chars + lowercase_letters

uppercase_letters_should = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?  "yes" or "no": ')
while yes_or_no(uppercase_letters_should):
     uppercase_letters_should = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?  "yes" or "no": ')
if uppercase_letters_should == 'yes':
    chars = chars + uppercase_letters

punctuation_should = input('Включать ли символи !#$%&*+-=?@^_?  "yes" or "no": ')
while yes_or_no(punctuation_should):
    punctuation_should = input('Включать ли символи !#$%&*+-=?@^_?  "yes" or "no": ')
if punctuation_should == 'yes':
    chars = chars + punctuation

for i in range(int(how_many_passwords)):
    password = generate_password(int(len_of_password), chars)
    print(password)