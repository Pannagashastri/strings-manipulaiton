val1=input("enter the alpahbet: ")
val2=input("enter the second alphabe: ")
val3=input("enter the third alphabet: ")
if ((val1.isdigit()==False)):
	while(True):
		
		print("menu \n")
		print("1=Repetition \n")
		print("2=concatination \n")
		print("3=reversing \n")
		print("4=range slicing \n")
		print("5=slicing \n")
		print("6=string membership \n")
		print("7=ierating \n")
		print("8=countin \n")
		print("9capitalize \n")
		print("10=splititn \n")
		print("11==exit \n")
		rece=int(input("enter the choice: \n"))
		if (rece==1):
			print(val1*2)
		elif (rece==2):
			print(val1+val2)
		elif (rece==3):
			print(val1[::-1])
		elif (rece==4):
			sl1=int(input("enter the starting slice number: "))
			sl2=int(input("enter the ending slice number: "))
			print(val1[sl1:sl2])
		elif (rece==5):
			slicing=int(input("enter the slicing number:  "))
			print(val1[slicing])
		elif (rece==6):
			meme=str(input("enter the character:  "))
			print(meme in val1)
		elif (rece==7):
			ite=str(input("enter the string: "))
			for i in  ite:
				print(i)
			for j in val1:
				print(j)
		elif (rece==8):
			cout=str(input("enter the alphabet to be counted: "))
			print(val1.count(cout))
		elif (rece==9):
			print(val1 .upper())
		elif (rece==10):
			print(val1.split())
		else:
			break
else:
	print("invalid input you entered")
