class User:
    # initializing the variables
    name = ""
    phone = ""
    password = ""

    # defining constructor
    def __init__(self, name,password="",phone=""):
        self.name = name
        self.phone = phone
        self.password = password

    # getter method
    def get_name(self):
        return self.name

    # setter method
    def set_name(self, name):
        self.name = name

        # getter method

    def get_phone(self):
        return self.phone

        # setter method

    def set_phone(self, phone):
        self.phone = phone

    # getter method
    def get_password(self):
        return self.password

    # setter method
    def set_password(self, password):
        self.password = password



