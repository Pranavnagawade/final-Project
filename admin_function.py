from admin import Admin
from food_item import Food_items
from user_function import User_register
class Admin_function:
    admin_list=[] 
    food_ID=3  
    food_list=[]

#admin Register 
    def admin_register_function(self): 
        full_name =input("Enter Your Full Name :")
        phone_no =int(input("Enter Your your Phone Number :"))
        email_id=input("Enter Your Email :")
        address =input("Enter Your Address :")
        password=input("Enter Your password :")
        admin_obj=Admin(full_name,phone_no,email_id,address,password)
        self.admin_list.append(admin_obj) 
        print("\n Admin Register succesfully ! \n")
    
    def admin_login_function(self):
        email_id=input("Enter Your Email :")
        password=input("Enter Your password :")
        for i in self.admin_list:
            if i.email_id == email_id and i.password == password:
                print("\n Admin Login Sucessfully !\n")
                return True       
        else:
            print("\nPlease Enter Valid Email ID or Password \n")
            return False

#add food 
    def add_food(self):
                food_name=input("Enter Food Name: ")
                quantity_food=input("Enter Quantity of food :")
                price_food=(input("Enter the price of Food :"))
                discount_food=(input("Enter Discount Amount in Only Rs :"))
                stock_food=(input("Amount left in stock in the restaurant :"))
                self.food_ID=self.food_ID+1
                food_id=self.food_ID
                food=Food_items(food_id,food_name,quantity_food,price_food,discount_food,stock_food)
                a=food_name + " " + "(" + quantity_food + ")" + " " + "[" + "INR" + " " + price_food + "]"+ " " + "(" + "Discount amount" +  " " + discount_food + ")"
                User_register.menu[food_id]=a
                self.food_list.append(food)
                print()
                print("\n food added sucessfully \n")

    def edit_food_item(self):
        edit_input=int(input("Enter Food Id For Edit Food Items :"))
        print()
        for food in self.food_list:
            if edit_input == food.get_food_id():
                    food_name=input("Enter Food Name: ")
                    quantity_food=input("Enter Quantity of food :")
                    price_food=float(input("Enter the price of Food :"))
                    discount_food=float(input("Enter Discount Amount in Only Rs :"))
                    stock_food=int(input("Amount left in stock in the restaurant :"))
                    food.set_food_name(food_name)
                    food.set_quantity_food(quantity_food)
                    food.set_price_food(price_food)
                    food.set_discount_food(discount_food)
                    food.set_stock_food(stock_food) 
                    print("Food Edit sucessfullly !") 
                    break                  
        else:
            print("Food is Not Listed ")        

    def view_food(self):
        if self.food_list:
            for i in self.food_list:
                print(i)
                print()           
        else:
            print("\n No food items \n")

    def delete_food(self):
        input_delete=int(input("Enter food Id for Delete food"))
        print()
        for food in self.food_list:
            if input_delete == food.get_food_id():
                self.food_list.remove(food)
                print("Food Delete sucessfully ! \n")
                break
        else:
            print("\n Food Id Not Found \n")
