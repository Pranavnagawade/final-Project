from User import User  
import datetime as dt

#user Register
class User_register:
    user_list=[] 
    orders=[]
    user_id=1
    current_user=0
    menu={1:"Tandoori Chicken (4 pieces) [INR 240]" , 2:"Vegan Burger (1 Piece) [INR 320]" , 3:"Truffle Cake (500gm) [INR 900]"}
    
    def user_register_function(self):
        full_name =input("Enter Your Full Name :")
        phone_no =int(input("Enter Your your Phone Number :"))
        email_id =input("Enter Your Email Address :")
        address =input("Enter Your Address :")
        password =input("Enter Your Password :")
        admin_obj1=User(self.user_id,full_name,phone_no,email_id,address,password)
        self.user_list.append(admin_obj1)
        print("User Register succesfully !")
        self.user_id+=1
    
    def user_login_function(self):
        email_id=input("Enter Your Email :")
        password=input("Enter Your password :")
        for i in self.user_list:
            if i.email_id == email_id and i.password== password:
                print()
                print("User  Login Sucessfully ! \n")
                self.current_user=i.get_user_id()
                return True
        else:
            print("\n Please Enter Valid Email ID or Password ")
            return False
    
    def place_order(self):

            for menuItem in self.menu.items():
                print(menuItem)
                print()
            foodId=input("Enter the Food ID you want to order separated by comma:").split(",")
            print()
            temp =[]
            for id in foodId :
             
                if self.menu.keys().__contains__(int(id)) :
                    temp.append(self.menu[int(id)])
                else :
                    print("Invalid Food Item " ,id)
            if len(temp) > 0 :
                print("Current Order : \n")
                print(temp)
                inputTwo = int(input("\n 1. Confirm and place the Order \n 2. Exit \n"))
                print()
                if inputTwo == 1 : 
                    current_date = dt.datetime.now()
                    temp.append("Order placed at : " + current_date.__str__())
                    self.orders.append(temp)
                    print("Your order has been placed successfully \n!")  
                else : print("Order cancelled!!")
                
    def order_history(self):
        for order in self.orders :
            print("****************")
            for singleOrder in order : 
                print(singleOrder)
            print("****************")

    def update_profile(self):
        for i in self.user_list:
            if i.get_user_id()==self.current_user:
                full_name =input("Enter Your Full Name :")
                phone_no =int(input("Enter Your your Phone Number :"))
                email_id =input("Enter Your Email Address :")
                address =input("Enter Your Address :")
                password =input("Enter Your Password :")
                 
                i.set_full_name(full_name)
                i.set_phone_no(phone_no)
                i.set_email_id(email_id)
                i.set_address(address)
                i.set_password(password)
                print("profile Updated Sucessfully !")
                break
        else:
            print("No Profile Found")



             
               

