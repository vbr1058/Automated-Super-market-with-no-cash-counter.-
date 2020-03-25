# Read the instruction properly accordingly give the input

from peewee import *
from app import *
from SMS import *
user=1
total=0

while(user==1 or total ==0):
	print("Select the choice: \n\
		1. Customer Login\n\
		2. Customer Sign up\n\
		3. Marchent (Only for the workers in he Market) \n\
		4. List of items present in the market\n\
		5. Exit out of the Market")
	choice=int(input("-->"))
	if(choice==1):
		user=str(Login())
		if(int(user)==1):
			while(int(user)==1):
				customers=customer()
				if(customers):
					total=total+customers
				print("Press 0 to Log_out or press 1 to continue: \n")
				user=int(input())
				if(user==0):
					c=int(count_list())
					for i in range(1,c+1):
						delete(i)
			sms=send_sms(total)
			while(not(sms)):
				print("Enter the currect email:\n")
				sms=send_sms(total)
			print("Thanks for the shooping the total amount of "+str(total)+" Rupee will be debited from your account\n\
				Have a great day!")
	if(choice==2):
		Sign_up()
	if(choice==3):
		Marchent()
	if(choice==4):
		List()
	if(choice==5):
		break
