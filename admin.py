class Admin:
    def __init__(self,full_name,phone_no,email_id,address,password): #
        self.full_name=full_name
        self.phone_no=phone_no
        self.email_id=email_id
        self.address=address
        self.password=password
   
    def __str__(self):
        return f"\nFull Name :{self.full_name} \nPhone Number :{self.phone_no} \nEmail ID: {self.email_id} \nAddress :{self.address} \nPassword :{self.password}"
   
    def set_full_name(self,full_name):
        self.full_name=full_name
    def get_full_name(self):
        return self.full_name

    def set_phone_no(self,phone_no):
       self.phone_no=phone_no
    def get_phone_no(self):
        return self.phone_no
    
    def set_email_id(self,email_id):
        self.email_id=email_id
    def get_email_id(self):
        return self.email_id

    def set_address(self,address):
        self.address=address
    def get_address(self):
        return self.address

    def set_password(self,password):
        self.password=password
    def get_password(self):
        return self.password

