from models import *
import getpass
from peewee import *
from datetime import datetime
db.connect()

def Sign_up():
	user_name=input("Enter the New user Name: ")	
	exists=len(user.select().where(user.user_name==user_name))
	if(not(exists)):
		passward=input("Enter the New Passward: ")
		user.create(user_name=user_name,passward=passward)
		print("user created Successffully:\n")
	else:
		print("User name already exists try another user name")

def Login():
	user_name=input("Enter your user name: ")
	login_check=user.select().where(user.user_name==user_name)

	if(len(login_check)):
		passward=getpass.getpass(prompt="Enter the passward")
		login_check=user.get()

		if(login_check.passward==passward):
			print("\nLogin Successffully: \n")
			return login_check.get()
		else:
			print("Invalid Passward: \n")
			return 0

	else:
		print("User name does not exists please try to Sign_up first: \n")
		return 0

def Marchent():
	item_name=input("Enter the item name: ")
	exists=len(Marchent_item.select().where(Marchent_item.item_name==item_name))
	if(not(exists)):
		item_cost=float(input("Enter the item cost: "))
		Marchent_item.create(item_name=item_name,item_cost=item_cost)
		print("Item Successffully added to the rack: \n")
	else:
		print("Item is already there in the rack: ")
	
def customer():
	C_item_name=input("Enter the item name: ")
	exists=Marchent_item.select().where(Marchent_item.item_name==C_item_name)
	if(len(exists)):
		exists=exists.get()
		customer_item.create(item_name=exists.item_name,item_cost=exists.item_cost)
		print("{} added Successffully!".format(C_item_name))
		return exists.item_cost
	else:
		print("The item that yor are entered is not present in our market: ")

def count_list():
	return int(customer_item.select().count())
def List():
	print("\n\nList of item preset in the market is as follows: \n\
Item name 	-->	Item cost\n\
-----------------------------------")
	for item in Marchent_item.select():
		print("{}		-->		{}".format(item.item_name,str(item.item_cost)))
	print("\n")
def delete(count):
	q=customer_item.get(customer_item.id == count)
	q.delete_instance()
