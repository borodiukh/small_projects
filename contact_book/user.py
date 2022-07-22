class User():
    def __init__(self, name, phone_number, address=None, email_address=None):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email_address = email_address

    def user_information(self):
        return self.name, self.phone_number, self.address, self.email_address


