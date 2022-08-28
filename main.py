#from admin import Admin
from user_function import User_register
from admin_function import Admin_function

class Foodmain:
    def __init__(self,admin_foodmain_obj,user_foodmain_obj):
        self.admin_foodmain_obj=admin_foodmain_obj
        self.user_foodmain_obj=user_foodmain_obj

    def admin_foodmain(self,x):
        while True:
            print("----------------------")
            print("    Admin Page      \n")
            print("----------------------")
            print("\n 1. Admin Register \n 2. Admin Login \n 3. Exit \n")
            x=int(input("Enter choice :"))
            print()
            if x==1:
                self.admin_foodmain_obj.admin_register_function()
            elif x==2:
                if self.admin_foodmain_obj.admin_login_function()==True:
                    while True: 
                    
                        print("\n1. Add Food Item \n2. Edit Food Item\n3. View Food Item\n4. Delete Food Item\n5. Exit \n")
                        
                        x=int(input("Enter choice :"))
                        print()
                        if x==1:
                            print("\n Add Foods \n")
                            self.admin_foodmain_obj.add_food()
                        elif x==2:
                            print("\n Edit foods \n")
                            self.admin_foodmain_obj.edit_food_item()
                        elif x==3:
                            print("\n food Items \n")
                            self.admin_foodmain_obj.view_food()
                        elif x==4:
                            print("\n Delete Food Items \n")
                            self.admin_foodmain_obj.delete_food()
                        else:
                            break    
            elif x==3:
                break

    def user_foodmain(self,x):
        while True:
                print("----------------------")
                print("        User Page \n")
                print("----------------------")
                print("\n 1. User Register \n 2. User Login \n 3. Exit \n")
                x=int(input("Enter choice :"))
                print()
                if x==1:
                    self.user_foodmain_obj.user_register_function()
                elif x==2:
                    if self.user_foodmain_obj.user_login_function()==True:
                            while True:
                                print("\n 1. Place New Order \n 2. Order History \n 3. Update Profile \n 4. Exit \n")
                                x=int(input("Enter choice :"))
                                print()
                                if x==1:
                                      self.user_foodmain_obj.place_order()
                                elif x==2:
                                    self.user_foodmain_obj.order_history()
                                elif  x==3:
                                    self.user_foodmain_obj.update_profile()
                                elif x==4:
                                    break
                elif x==3:
                    break
if __name__=="__main__":
    admin_function_obj=Admin_function()
    user_function_obj=User_register()
    object=Foodmain(admin_function_obj,user_function_obj)

while True:
    print("\n 1. Admin \n 2. User \n 3. Exit \n")
    choice=int(input("Enter your Choice :"))
    print()
    if choice==1:
        object.admin_foodmain(choice)
    elif choice==2:
        object.user_foodmain(choice)
    elif choice==3:
        print("Thanks!!")
        break
    else:
        print("please take valid input")
        print()
        
