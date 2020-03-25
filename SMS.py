import smtplib 
def send_sms(cost):
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls()
	message="Dear Sir/Madam\n\
Your Account xxxxxxxx043526xx has been DEBITED for Rs."+str(cost)+"/-\n\
\n\
If this Transaction is not initiated by you,Kindly conact our customer care  Centre- 18004251444 immediately. \n\
\n\n\
Yours faithfully,\n\
Karnataka Bank,\n\
CCC, Bangalore."
	s.login("vbr3906@gmail.com", "vinay@95130")
	try:
		s.sendmail("vbr3906@gmail.com", input("Enter Your E-mail: "), message) 
		return 1
	except:
		print("E-mail doesn't exixt please Enter proper E-mail: ")
		return 0
	s.quit() 


























